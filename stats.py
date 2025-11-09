def number_of_words(book_text):
    words = len(book_text.split())
    return words

def character_counter(text):
    counts = {}
    lower_char = text.lower()
    for chars in lower_char:
        if chars in counts:
            counts[chars] = counts[chars] + 1
        else:
            counts[chars] = 1
    return counts

def sort_on(d):
    value = d["num"]
    return value


def dictionary_sorter(counts):
    sorted_list = []
    for char, num in counts.items():
        formated_dict = {}
        formated_dict["char"] = char
        formated_dict["num"] = num

        sorted_list.append(formated_dict)

    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list



    
