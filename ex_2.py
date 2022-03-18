def reverse(sentence, reverse_word):
    check_sentence = isinstance(sentence, str)
    check_reverse_word = isinstance(reverse_word, str)
    try:
        type(sentence) == str
        type(reverse_word) == str
        countReverseWord = sentence.count(reverse_word)
        replacedReverseWord = reverse_word[::-1]
    except:
        print("invalid input")
    else:
        if countReverseWord == 0:
            return print("The word was not found")
        else:
            lengthWord = len(reverse_word)
            loc = sentence.find(reverse_word)
            sentenceNew = sentence[loc + lengthWord:]

            return print(sentence[:loc] + replacedReverseWord + sentenceNew )
