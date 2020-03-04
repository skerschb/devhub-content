# Sanity Check

## What is it?

This small python script scans the blog posts for invalid: 
- tags,
- products,
- languages,
- unused images from the `source/images/` folder.

## Use it

```bash
python3 sanity-check.py
```

## Errors

The scripts tells you something like this?

```
ERROR: invalid entry in file: ../source/how-to/stitch-authentication-triggers.txt=> 'Stitch'
```

That's because you forgot the star `*` to make a list under the appropriate directive in this file.

### Do

```
.. products::

   * Stitch
   * Atlas
```

### Don't

```
.. products::

   Stitch
   Atlas
```

## Example output

```
/usr/bin/python3.7 /home/polux/Work/devhub-content/sanity-check/sanity-check.py
ERROR: invalid entry in file: ../source/how-to/stitch-authentication-triggers.txt=> 'Stitch'
ERROR: invalid entry in file: ../source/how-to/stitch-authentication-triggers.txt=> 'Atlas'

List of the invalid tags:

=> Invalid tag: Releases            => ../source/article/stitch-triggers.txt
=> Invalid tag: Stitch              => ../source/article/stitch-triggers.txt
=> Invalid tag: Technical           => ../source/article/enterprise-operator-kubernetes-openshift.txt
=> Invalid tag: Ops Manager         => ../source/article/enterprise-operator-kubernetes-openshift.txt
=> Invalid tag: Technical           => ../source/article/srv-connection-strings.txt
=> Invalid tag: Technical           => ../source/article/active-active-application-architectures.txt
=> Invalid tag: Technical           => ../source/how-to/data-enrichment-stitch.txt
=> Invalid tag: Technical           => ../source/how-to/data-streaming-kafka-consumer.txt
=> Invalid tag: javascript          => ../source/how-to/nextjs-building-modern-applications.txt
=> Invalid tag: nodejs              => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid tag: python              => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid tag: ruby                => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid tag: go                  => ../source/how-to/golang-alexa-skills.txt
=> Invalid tag: aws                 => ../source/how-to/golang-alexa-skills.txt
=> Invalid tag: Stitch              => ../source/how-to/stitch-shell.txt
=> Invalid tag: Deploy              => ../source/how-to/stitch-hosting.txt
=> Invalid tag: Technical           => ../source/how-to/transactions-c-dotnet.txt
=> Invalid tag: Developer           => ../source/how-to/transactions-c-dotnet.txt
=> Invalid tag: Full-Text Search    => ../source/how-to/search-engine-using-atlas-full-text-search.txt
=> Invalid tag: Stitch              => ../source/how-to/stitch-authentication-triggers.txt
=> Invalid tag: Technical           => ../source/how-to/stitch-authentication-triggers.txt
=> Invalid tag: javascript          => ../source/how-to/graphql-support-atlas-stitch.txt
=> Invalid tag: graphql             => ../source/how-to/graphql-support-atlas-stitch.txt
=> Invalid tag: Releases            => ../source/how-to/storing-large-objects-and-files.txt
=> Invalid tag: iot                 => ../source/how-to/capture-iot-data-stitch.txt
=> Invalid tag: AWS                 => ../source/how-to/stitch-aws-rekognition-images.txt
=> Invalid tag: Java                => ../source/quickstart/java-mapping-pojos.txt
=> Invalid tag: Java                => ../source/quickstart/java-change-streams.txt
=> Invalid tag: Java                => ../source/quickstart/java-aggregation-pipeline.txt
=> Invalid tag: BSON                => ../source/quickstart/bson-data-types-decimal128.txt
=> Invalid tag: Python              => ../source/quickstart/python-acid-transactions.txt
=> Invalid tag: BSON                => ../source/quickstart/bson-data-types-objectid.txt
=> Invalid tag: ObjectId            => ../source/quickstart/bson-data-types-objectid.txt
=> Invalid tag: Python              => ../source/quickstart/python-change-streams.txt
=> Invalid tag: Java                => ../source/quickstart/java-setup-crud-operations.txt
=> Invalid tag: Node                => ../source/quickstart/nodejs-crud-video.txt

List of the invalid products:

=> Invalid product: MongoDB Atlas       => ../source/how-to/nextjs-building-modern-applications.txt
=> Invalid product: MongoDB Atlas       => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid product: MongoDB Atlas       => ../source/how-to/golang-alexa-skills.txt

List of the invalid languages:

=> Invalid language: JavaScript          => ../source/how-to/data-enrichment-stitch.txt
=> Invalid language: nodejs              => ../source/how-to/nextjs-building-modern-applications.txt
=> Invalid language: react               => ../source/how-to/nextjs-building-modern-applications.txt
=> Invalid language: nodejs              => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid language: python              => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid language: ruby                => ../source/how-to/nodejs-python-ruby-atlas-api.txt
=> Invalid language: go                  => ../source/how-to/golang-alexa-skills.txt
=> Invalid language: javascript          => ../source/how-to/stitch-shell.txt
=> Invalid language: c#                  => ../source/how-to/transactions-c-dotnet.txt
=> Invalid language: .NET                => ../source/how-to/transactions-c-dotnet.txt
=> Invalid language: javascript          => ../source/how-to/search-engine-using-atlas-full-text-search.txt
=> Invalid language: javascript          => ../source/how-to/stitch-authentication-triggers.txt
=> Invalid language: javascript          => ../source/how-to/graphql-support-atlas-stitch.txt
=> Invalid language: javascript          => ../source/how-to/capture-iot-data-stitch.txt
=> Invalid language: javascript          => ../source/how-to/stitch-aws-rekognition-images.txt
=> Invalid language: nodejs              => ../source/quickstart/nodejs-crud-video.txt

List of images not used:

=> /images/hero-node.png
=> /images/awsroutes5.png
=> /images/hero-computers.png
=> /images/hero-developer.jpg
=> /images/hero-dark-lines.png
=> /images/hero-misc.png
=> /images/starlette/stitch-dashboard.png
=> /images/starlette/stitch.png
=> /images/bios/bio-karen.jpg
=> /images/bios/bio-max.jpg
=> /images/bios/bio-generic.jpg
=> /images/bios/bio-naomi.png
=> /images/atf-images/illustrations/community-card.png
=> /images/atf-images/illustrations/docs.png
=> /images/atf-images/illustrations/dev-tools.png
=> /images/atf-images/photos/meetup.png
=> /images/atf-images/photos/fun-events.png
=> /images/atf-images/photos/nodejs.png
=> /images/atf-images/photos/age-gap.png
=> /images/atf-images/generic/green.png
=> /images/atf-images/logos/Unity.png
=> /images/atf-images/quickstart/ruby.png

Process finished with exit code 0
```