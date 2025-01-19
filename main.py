#print("hello world")

def main():
    txt_path = "books/frankenstein.txt"
    txt = book_text(txt_path)
    num_words = word_count(txt)
    let_count = count_letters(txt)
    sort_count = sort_letters(let_count)
    print(f"--- Begin report of text at {txt_path} ---")
    print(f"There are {num_words} words in this text")
    print(f"Letters in text are as follows: ")
    for i in range(len(sort_count)):
        print(f"The letter '{sort_count[i]["letter"]}' appears {sort_count[i]["num"]} times")
       

def word_count(book_text):
    return len(book_text.split())

def book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_letters(book_text):
    let_cnt = {} 
    text = book_text.lower()
    for i in text:
        if i in let_cnt:
            let_cnt[i] += 1
        else:
            let_cnt[i] = 1
    return let_cnt

def sort_on(dict):
    return dict["num"]

def sort_letters(letters):
    sort = []
    for i in letters:
        if i.isalpha():
            sort.append({"letter" : i, "num" : letters[i]})
    sort.sort(reverse=True, key=sort_on)
    return sort

main()