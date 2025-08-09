import sys
import stats


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = stats.get_word_count(text)
    char_count = stats.get_char_count(text)
    sorted_chars = stats.get_sorted_char_count_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():  # Skip non-alphabetical characters
            print(f"{char}: {num}")
            
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
