import sys
from stats import num_words, char_count, build_report

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    word_count = num_words(file_path)
    letter_count = char_count(file_path)
    built_list = build_report(file_path)

    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {file_path}...")
    print("-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {word_count} total words")
    print("-" * 15 + " Character Count " + "-" * 15)

    for char, count in built_list:
        print(f"{char}: {count}")

    print("=" * 13 + " END " + "=" * 13)

main()
