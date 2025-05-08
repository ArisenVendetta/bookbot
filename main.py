import sys
from stats import count_words, count_characters, generate_sorted_count

def get_book_text(filepath: str = None) -> str:
    if filepath is None or filepath == "":
        return None
    file_contents = ""
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except Exception as e:
        raise
    return file_contents

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        try:
            content = get_book_text(book)
            words = count_words(content)
            characters = count_characters(content)
            sorted_characters = generate_sorted_count(characters)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {book}...")
            print("----------- Word Count ----------")
            print(f"Found {words} total words")
            print("--------- Character Count -------")
            for entry in sorted_characters:
                if entry["char"].isalpha():
                    print(f"{entry["char"]}: {entry["num"]}")
            print("============= END ===============")
        except Exception as e:
            print(f"Error: {repr(e)}")

main()