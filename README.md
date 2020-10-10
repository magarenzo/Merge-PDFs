# Merge PDFs

Merge multiple PDFs into a single document

## About

I needed to combine some PDFs and didn't have a program handy, nor did I want to risk putting sensitive information online using some a website, so I quickly put together this script instead!

## Usage

* Replace the String value of the `path` variable with the path to your PDF documents, ending with a "/"

* Note that this script relies on your documents to already be in alphanumeric order, as that is the order in which the files will be merged

## Dependencies

* [glob](https://docs.python.org/3/library/glob.html)

* [PyPDF2](https://github.com/mstamy2/PyPDF2)

  * I installed PyPDF2 with [pip](https://pypi.org/project/pip/) using `pip install PyPDF2`

## Owner

Michael A. Agarenzo
