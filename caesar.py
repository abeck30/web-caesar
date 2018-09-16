import string
alpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabet_position(letter):
    if letter.isalpha():
        if letter.isupper():
            alpha_new = letter.lower()
            alpha_num = alpha.index(alpha_new)
            return alpha_num
        elif letter.islower():
            alpha_num = alpha.index(letter) 
            return alpha_num
    else:
        alpha_num = letter  
        return alpha_num          

def rotate_character (char,rot):
    if char.isalpha(): 
        new_letter = alphabet_position(char) + rot
        if new_letter < 26:
            new_char = alpha[new_letter]
        else:
            newer_letter = new_letter % 26
            new_char = alpha [newer_letter]

        if char.isupper():
            return new_char.upper()
        elif char.islower():
            return new_char.lower()

    elif char in string.punctuation:
        return char

    elif char.isdigit():
        return char 

    elif char ==" " :   
        return char
        
def encrypt (text,rot):
    encrypted = ''
    for each_char in text:
        if each_char == '':
            encrypted = encrypted + ''
        else:
            each_char = rotate_character(each_char,rot)
            encrypted = encrypted + each_char
    return encrypted        
      
def main():
    question1 = "Type a message:"
    user_text = input(question1)
   
    question2 = "Rotate by:"
    user_rot = input(question2)
    user_int = int(user_rot)
    

    print (encrypt(user_text,user_int))

if __name__ == "__main__":
    main()   