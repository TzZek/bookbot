def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
def count():
    with open("books/frankenstein.txt") as f:
        text = f.read()

        lines = text.split()
        count_words = 0
        count_words += len(lines)

        print(count_words)


main()
count()
