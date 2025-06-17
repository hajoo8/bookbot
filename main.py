import sys
from stats import get_word_count, get_char_count, sort_char_res

def get_book_text(f_path):
    with open(f_path) as f:
        f_contents = f.read()
    return f_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        f_path = sys.argv[1]
    contents = get_book_text(f_path)
    w_result = get_word_count(contents)
    c_result = get_char_count(contents)
    sorted_result = sort_char_res(c_result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f_path}...")
    print("----------- Word Count ----------")
    print(f"Found {w_result} total words")
    print("--------- Character Count -------")
    for res in sorted_result:
        c = res.get("char")
        n = res.get("num")
        print(f"{c}: {n}")
    print("============= END ===============")

main()