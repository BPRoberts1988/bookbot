def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(letter_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letters(letter_count):
    letter_dictionary = {}
    for i in letter_count:
        lowercase = i.lower()
        if lowercase in letter_dictionary:
            letter_dictionary[lowercase] += 1
        else:
            letter_dictionary[lowercase] = 1
    return letter_dictionary


main()