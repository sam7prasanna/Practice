text = "Python is simple and Python is powerful"

l = len(text)
print(f"Total number of letters in the word is: {l}")


def word_count():

    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print(f"The total count of words is: {word_count}")

def char_count():

    char_count = {}
    char_count_w_space = {}

    for char in text:
        if char != " ":   # ignore spaces
            char_count[char] = char_count.get(char, 0) + 1

    for char in text:
        char_count_w_space[char] = char_count_w_space.get(char, 0) + 1

    print(f"Total count of letters without space is: {char_count}")
    print(f"Total count of letters without space is: {char_count_w_space}")

word_count()
char_count()