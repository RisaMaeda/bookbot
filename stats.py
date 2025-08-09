def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    text = text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_sorted_char_count_list(char_counts):
    sorted_list = []
    for char, num in char_counts.items():
        sorted_list.append({"char": char, "num": num})
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(item):
    return item["num"]

    