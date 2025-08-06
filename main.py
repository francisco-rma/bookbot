import sys
from stats import count_chars, count_words


def get_book_text(path:str):
    with open(path) as f:
        contents = f.read()
        return contents


def main(book_path:str):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    contents = get_book_text(book_path)

    print("----------- Word Count ----------")
    total_words = count_words(contents)
    print(f"Found {total_words} total words")
    
    print("--------- Character Count -------")
    char_count:dict[str,int] = count_chars(contents)
    print("\n".join([f"{char}: {count}" for char, count in char_count.items()]))
    
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    main(book_path=sys.argv[1])