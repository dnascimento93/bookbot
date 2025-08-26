from stats import count_words, count_characters, sort_by_count
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts.sort(reverse=True, key=sort_by_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words")
    print("-------- Character Count -------")
    for char_count in char_counts:
        if char_count["char"].isalpha():
            char = char_count["char"]
            num = char_count["num"]
            print(f"{char}: {num}")
    print("============= END ===============")


if __name__ == "__main__":
    main()