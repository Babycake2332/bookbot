
def get_book_text(path: str):
    with open(path) as f:
        return f.read()

def get_word_count(book: str):
    counter = 0
    listed_book = list(book.split())

    for _ in listed_book:
        counter += 1
    return counter

def get_character_count(book: str):
    char_count = {}

    for _, char in enumerate(book.lower()):
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1
    return char_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_character_count(text)

    # REPORT #-------------------------------------------------
    list_of_dicts = [{k: v} for k, v in char_dict.items()]
    sorted_list = sorted(list_of_dicts, key=lambda d: list(d.values())[0], reverse = True)

    print(f"--- Begin report of {book_path} ---\n")
    print(f"{num_words} words were found in the document.\n")

    for index in sorted_list:
        for key in index:
            if key.isalpha(): 
                print(f"The '{key}' character was found {index[key]} times.")
    
    print("\n--- End report ---")
    # END REPORT #---------------------------------------------

if __name__ == "__main__":
    main()