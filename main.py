import sys
from stats import get_book_text, word_count, char_cout, chars_dict_to_sorted_list


def main():
    print(f"Script name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"First argument: {sys.argv[1]}")
    else:
        print("Usage: python3 main.py <path_to_book>")

    print(f"All arguments: {sys.argv}")
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("=========BOOKBOT===================")
    #print(f"Analyzing book found at {}...")
    print("----------- Word Count ----------")
    word_count(text)
    print("--------- Character Count -------")
    charCount = char_cout(text)
    chars_sorted_list = chars_dict_to_sorted_list(charCount)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    




main()
    