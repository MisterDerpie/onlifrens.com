# OnliFrens

## Build

This website is built using [Hugo](https://gohugo.io/).

```
$ hugo version
hugo v0.92.2+extended linux/amd64 BuildDate=2023-01-31T11:11:57Z VendorInfo=ubuntu:0.92.2-1ubuntu0.1
```

In addition, it uses two themes:

- [potato-dark](https://github.com/surajmandalcell/potato-dark) (modified)
- [hugo-shortcode-gallery](https://github.com/mfg92/hugo-shortcode-gallery)

To build it, simply run

```
$ hugo
Start building sites … 
hugo v0.92.2+extended linux/amd64 BuildDate=2023-01-31T11:11:57Z VendorInfo=ubuntu:0.92.2-1ubuntu0.1

                   | EN  
-------------------+-----
  Pages            | 11  
  Paginator pages  |  0  
  Non-page files   |  0  
  Static files     | 23  
  Processed images |  0  
  Aliases          |  2  
  Sitemaps         |  1  
  Cleaned          |  0  

Total in 14 ms
```

and the output will be put in the folder `public/`.

## Add new Images

The helper `generate_images.py` can be used to move an 
image/a set of images into the desired place.

```
$ python3 generate_images.py --input /path/to/input/{dir/file} [--output /path/to/output/dir]
```

By default, `output` points to `content/posts/gallery/images` and is thus optional.