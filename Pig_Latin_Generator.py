def pig_latin(word):
    vowels = "aeiouAEIOU"
    
    if word[0] in vowels:
        return word + "ay"
    else:
        first_letter = word[0]
        return word[1:] + first_letter + "ay"

def translate_to_pig_latin(sentence):
    words = sentence.split()
    translated_words = [pig_latin(word) for word in words]
    return " ".join(translated_words)

x = str(input("Please enter a sentence: "))
pig_latin_sentence = translate_to_pig_latin(x)
print(pig_latin_sentence)
