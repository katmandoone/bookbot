# imports the text
def get_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

# counts words in text
def count_words(text):
    word_count = len(text.split())
    return word_count

# creates a dictionary of character counts for the given text
def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# returns the number of characters for sorting
def sort_on(items):
    return items["num"]

# returns a sorted report of alphabetical character counts
def char_sort(char_dict):
    dict_list = []
    for char in char_dict:
        if char.isalpha():
            dict_list.append({"char": char, "num": char_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list