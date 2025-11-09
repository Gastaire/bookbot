from stats import number_of_words
from stats import character_counter
from stats import dictionary_sorter
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    text = get_book_text(filepath)
    word_count = number_of_words(text)
    counts = character_counter(text)
    sorted_chars = dictionary_sorter(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        
        if item["char"].isalpha():
             print(f"{item['char']}: {item['num']}") 

    print("============= END ===============")

main()