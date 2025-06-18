# import libraries
from stats import get_no_words, count_letters, sort_dict
import sys


def get_book_text(filepath):
    """
      return book text as string

      inputs:
      filepath: Path to file

      return:
      file: a string of the file from filepath provided

    """

    with open(filepath, 'r') as file:
        file_string = file.read()

    return file_string



def main():

#    frank_path = "/Users/kjha/code/bootdev/bookbot/books/frankenstein.txt"

    # get bookpath from command line
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        frank_path = sys.argv[1]
    
        

    
    book_text = get_book_text(frank_path)
    n_words = get_no_words(book_text)
    dict_count = count_letters(book_text)
    sorted_dict_count = sort_dict(dict_count)
    
    # Print Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frank_path}...")
    print("----------- Word Count ----------")
    print(f"Found {n_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_dict_count.items():
        print(f"{key}: {value}")
    print("============= END ===============")
    


if __name__ == "__main__":
    main()
