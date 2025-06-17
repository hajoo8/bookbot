def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)

def get_char_count(book_contents):
    results = {}
    contents = book_contents.lower()
    for char in contents:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results

def sort_on(source):
    return source["num"]

def sort_char_res(char_res):
    list = []
    for res in char_res:
        if res.isalpha():
            list.append({"char": res, "num": char_res[res]})
    list.sort(reverse=True, key=sort_on)
    return list