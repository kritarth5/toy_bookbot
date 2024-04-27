# import libraries
from pathlib import Path 
import pdb
import string

def get_text_from_book(book_path):
    with open(book_path) as f:
        return f.read()

def get_words_from_text(text):
    return text.split()

def get_letter_count(text):
    """
    Get count of each letter in the corpus of words
    """
    # initialise an empty dictionary to store 'letter': 'count' 
    letters = {x: 0 for x in string.ascii_lowercase}

    # convert text to lower case
    text = text.lower()

    # loop over every letter in text and add a counter for it
    for i in range(0,len(text)):
        try:
            letters[text[i]] += 1
        except:
            continue

    # return letters dictionary
    return letters

def sort_on(dict):
    """
    Helper function to sort a dictionary on the count key
    """
    return dict["count"]

def print_to_console(words, letters):
    """
    Print words and letters to the console in a nice format
    """

    # convert letters dictionary into a list of dictionaries
    letters_dict = [{'letter':key, 'count':value} for key, value in letters.items()]

    # sort letters_dict by counts
    letters_dict.sort(reverse=True, key=sort_on)

    # print out a nice header
    print("--- Begin report of books/frankenstein.txt ---\n")

    # print out number of words
    print(f"{len(words)} words found in the document\n")

    # loop over dictionary list and print to console
    for letter_dict in letters_dict:
        print(f"The '{letter_dict['letter']}' character was found {letter_dict['count']} times")

    # add a footer
    print("--- End Book Summary ---")
    

def main():
    # get words from books
    book_path = Path("/Users/kjha/ddl/kjha/tutorials/bootdev/toy_bookbot/books/frankenstein.txt")
    text = get_text_from_book(book_path)
    words = get_words_from_text(text)

    # get a dictionary to count all the letters in the text
    letters = get_letter_count(text)

    # Function to print words and letters to console
    print_to_console(words, letters)
    
    
main()

    
