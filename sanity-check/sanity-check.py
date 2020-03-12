import os


def read_list_in_directive(file, directive):
    with open(file.path, encoding="utf-8") as f:
        reading_tags = False
        empty_lines = 1
        tags_array = []
        for line in f.readlines():
            if directive in line:
                reading_tags = True
            if reading_tags and '' is line.strip():
                empty_lines -= 1
            if reading_tags and empty_lines == 0 and '' is not line.strip():
                try:
                    tags_array.append(line.split('*')[1].strip())
                except:
                    print('ERROR: invalid entry in file: ' + f.name + '=> \'' + line.strip() + '\'')
            if reading_tags and empty_lines < 0:
                return {'file': file, 'array': tags_array}
        return {'file': file, 'array': tags_array}


def check_for_invalid_elements(files, valid_list, element):
    print('\nList of the invalid ' + element + 's:\n')
    for ft in files:
        for tag in ft['array']:
            if tag not in valid_list:
                print('=> Invalid ' + element + ': ' + '{:20}'.format(tag) + '=> ' + ft['file'].path)


def scan_images(file):
    with open(file, encoding="utf-8") as f:
        images = []
        for line in f.readlines():
            line_chards = line.split()
            for chard in line_chards:
                if chard.startswith('/images/'):
                    images.append(chard)
        return images


with open('tags.txt', encoding="utf-8") as f:
    valid_tags = f.read().splitlines()
with open('products.txt', encoding="utf-8") as f:
    valid_products = f.read().splitlines()
with open('languages.txt', encoding="utf-8") as f:
    valid_languages = f.read().splitlines()

blog_posts = []
with os.scandir('../source/article') as f:
    for file in f:
        blog_posts.append(file)
with os.scandir('../source/how-to') as f:
    for file in f:
        blog_posts.append(file)
with os.scandir('../source/quickstart') as f:
    for file in f:
        blog_posts.append(file)

file_tags = []
file_products = []
file_languages = []
images_used = set()

for file in blog_posts:
    file_tags.append(read_list_in_directive(file, '.. tags::'))
    file_products.append(read_list_in_directive(file, '.. products::'))
    file_languages.append(read_list_in_directive(file, '.. languages::'))

blog_posts_and_authors = list(blog_posts)

with os.scandir('../source/includes/authors') as f:
    for file in f:
        blog_posts_and_authors.append(file)

for file in blog_posts_and_authors:
    images_used.update(scan_images(file))

check_for_invalid_elements(file_tags, valid_tags, 'tag')
check_for_invalid_elements(file_products, valid_products, 'product')
check_for_invalid_elements(file_languages, valid_languages, 'language')

all_images = []
for (dirpath, dirnames, filenames) in os.walk('../source/images'):
    all_images += [os.path.join(dirpath, file).replace('../source', '').replace('\\', '/') for file in filenames]

print('\nList of images not used:\n')
for img in all_images:
    if img not in images_used:
        print('=> ' + img)

print('\nList of images not found:\n')
for img in images_used:
    if img not in all_images:
        print('=> ' + img)
