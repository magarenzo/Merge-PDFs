# Merge PDFs

Merge multiple PDFs into a single document

## About

I needed to combine some PDFs and didn't have a program handy, nor did I want to risk putting sensitive information online using some random website, so I quickly put together this script instead

## Usage

* Replace the empty String value of the `path` variable with the path to your PDF documents, ensuring the value ends with `/`

* Note that this script relies on your documents to all be located in `path` and aligned in alphanumeric order to match the order you want the files to be merged

* The output `merged.pdf` will be written to `path`

## Dependencies

* [glob](https://docs.python.org/3/library/glob.html)

* [PyPDF2](https://github.com/mstamy2/PyPDF2)

## Owner

Michael A. Agarenzo
