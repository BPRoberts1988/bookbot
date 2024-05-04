def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_dict_list = get_num_letters(text)
    print(f"--- Begin Report of {book_path} ---")
    print("")
    print(f"{num_words} words found in the document")
    print("")
    for item in sorted_dict_list:
        print(f"Character {item['Letter']} was found {item['Count']} times!!!")
    print("")
    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letters(letter_count):
    letter_dictionary = {}
    for i in letter_count:
        if i.isalpha():
            lowercase = i.lower()
        if lowercase in letter_dictionary:
            letter_dictionary[lowercase] += 1
        else:
            letter_dictionary[lowercase] = 1
    list_of_dict = [{"Letter": key, "Count": value} for key, value in letter_dictionary.items()]
    sorted_dict_list = sorted(list_of_dict, key = lambda x: x["Count"], reverse = True)
    return sorted_dict_list
    

main()