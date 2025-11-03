#imports
import sys
from stats import count_words
from stats import count_char
from stats import sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


#variables
path=sys.argv[1]



#functions
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        file_content=file_content.lower()
    return file_content


#main    
def main():
    booktext=get_book_text(path)
    number=count_words(booktext)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    
    character_dict=(count_char(booktext))
    sorted_list=sort(character_dict)
    for items in sorted_list:
        if items["key"].isalpha():
            print(f"{items["key"]}: {items["value"]}")
        else:
            continue
    
#call main
main()
