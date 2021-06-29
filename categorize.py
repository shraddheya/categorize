import sys
import traceback
from os import path
# from __future__ import annotations


__supportFormat = ".tsv"
__doc__ = """Usage :
        python categorize.py [filename]

    Filetypes supported : {}

""".format(__supportFormat)


def get_file_name() -> str:
    """Get file names from command line arguments"""
    fileName = sys.argv[1:]
    if len(fileName) != 1:
        raise ValueError("Exactly one Input filename is expected")

    return fileName[0]


def check_file_valid(fileName: str) -> None:
    """Checks if the fileName provided is valid and exists"""
    if not path.isfile(fileName):
        raise ValueError('No such file "{}" exists'.format(fileName))

    if path.splitext(fileName)[-1] != __supportFormat:
        raise ValueError('Only "{}" files are supported'
                         .format(__supportFormat))


def get_data(fileName: str) -> list[str]:
    """Read the file and get all data"""
    with open(fileName, 'r') as f:
        return f.readlines()


def process_count_categories(allBooks: list[str]) -> dict:
    """Read the file and get all data"""
    categories = {}
    for bookDetail in allBooks:
        bookData = bookDetail.strip().split("\t")
        bookCategories = bookData[2].split(',')
        for category in bookCategories:
            if category not in categories:
                categories[category] = 0

            categories[category] += 1

    return categories


def main():
    """Main function to bundle all functionlity"""
    try:
        fileName = get_file_name()
        check_file_valid(fileName)
        allBooks = get_data(fileName)[1:]
        categories = process_count_categories(allBooks)
        print (categories)

    except ValueError as e:
        traceback.print_exc()
        print ("\nRefer to the usage manual\n", __doc__)


if __name__ == '__main__':
    main()
