def main():
    path="books/frankenstein.txt"
    book_text=get_book_text(path)
    words=count_words(book_text)
    print(f"Found {words} total words")


def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
    return content


def count_words(text):
    words = text.split()
    return (len(words))


main()