file_path = "books/frankenstein.txt"

def num_words(file_path):
    full_text = get_book_text(file_path)
    words = full_text.split()
    return len(words)

def get_book_text(file_path):
    read_file = ""
    with open(file_path) as f:
        read_file = f.read()
    file_as_string = read_file
    return read_file

def char_count(file_path):
    words = get_book_text(file_path)
    words = words.lower()
    dictionary = {}
    for l in words:
        if l.isalpha():
            dictionary[l] = dictionary.get(l, 0) + 1
    return dictionary

def build_report(file_path):
    # get dictionary
    char_dictionary = char_count(file_path)
    char_list = list(char_dictionary.items())
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict[1]
