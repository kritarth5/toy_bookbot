from collections import Counter

def get_no_words(file_string):
    """
      Function that accepts a string object and returns how many words are there in it
    """

    words = file_string.split()
    n_words = len(words)
    return n_words

def count_letters(file_string):
    """ Function to count the number each letter appears in the string"""
    clean_string = "".join(file_string.split())
    return dict(Counter(clean_string.lower()))

def sort_dict(your_dict):
    """ Sort dictionary by values  """
    return dict(sorted(your_dict.items(), key=lambda x: x[1], reverse=True))


