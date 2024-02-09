#!/usr/bin/env python3

"""Retrieve and print words from any URL

Usage: 
    python3 words.py <URL>


Notes: on mac/unix systems run `chmod +x words.py` to mark as executable
"""

import sys
from urllib.request import urlopen

default_url = "http://sixty-north.com/c/t.txt"


def fetch_words(url):
    """Fetch a list of words from a url

    Args:
        url: The URL of a UTF-8 document.

    Returns:
        A list of strings containing the words from the document.

    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    """Given a list of items, it prints each item per line

    Args:
        items: a list of items


    """
    for item in items:
        print(item)


def main(url):
    if url is None:
        url = default_url
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    """
    if __name__ == main means it's being executed as a script,
    otherwise being imported into another module.

    Modules: convenient import with API
    Script: convenient execution from commandline
    Program: perhaps composed of many modules
    """
    main(sys.argv[1])
