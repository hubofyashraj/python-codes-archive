def ceas_chiph(text,s):
    ciphed = "" 
   
    for i in range(len(text)): 
        char = text[i]
        if (char==" "):
            ciphed+=" "
      #for uppercase
        elif (char.isupper()): 
            ciphed += chr((ord(char) + s-65) % 26 + 65) 
  
      #for lowercase
        else: 
            ciphed += chr((ord(char) + s - 97) % 26 + 97) 
  
    return ciphed 
   
text = input("Enter text to cipher : ")
s =int( input("Shift By : "))
print("\nText  : \n" , text) 
print("\nShift : \n " , int(s)) 
print("\nCipher: \n" ,ceas_chiph(text,s))
