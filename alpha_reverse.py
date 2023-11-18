alhabet={"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}




word=input("enter the word: ")
word_lower=word.lower()

word_new=""

for i in word_lower:
    word_new+=alhabet.get(i,' ')


print(word_new)