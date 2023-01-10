def check_vovels(word):

    count = 0
    len_word = len(word)

    for x in range(0,len_word):
        if (word[x] == 'a' or word[x] == 'e' or word[x] == 'i' or word[x] == 'o' or word[x] == 'u' or word[x] == 'A' or word[x] == 'E' or word[x] == 'I' or word[x] == 'O' or word[x] == 'U'):
            count += 1
    return count

def check_words(word):

    # strip() is used to remove white spaces begining and ending 
    word = word.strip()
    count = 0
    len_word = len(word)
    for x in range(0,len_word):
        if(word[x] == " "):
            count += 1
    return count + 1


word = input ("Enter a word or senstence : ")
num_vovels = check_vovels(word)
num_words = check_words(word)

print("Number of vovels : {}".format(num_vovels))
print("Number of words : {}".format(num_words))
