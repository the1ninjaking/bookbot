#print("hello world")

def main():
    txt_path = "books/frankenstein.txt"
    txt = book_text(txt_path)
    num_words = word_count(txt)
    let_count = count_letters(txt)
    #print(txt)
    #print(f"{num_words} words in this text")
    #print(f"letters in text are as follows: {let_count}")

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


main()