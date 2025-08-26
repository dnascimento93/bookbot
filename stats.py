def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = {"char": char, "num": 0}
        char_count[char]["num"] += 1
    return list(char_count.values())


def sort_by_count(char_counts):
    return char_counts["num"]