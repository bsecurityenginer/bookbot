def get_book_text(path):
    with open(path) as f:
      return f.read()

def word_count(string):
    count = 0
    word_split = string.split()
    for word in word_split:
        count += 1
    print("Found",count,"total words")

def char_cout(string):
    char_dict = {}
    lower_split = string.lower()
    word_split = string.split()
        #print(word_split)
    for char in lower_split:
        for char in char:
                #print(char)
            if char in char_dict:
                 char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list