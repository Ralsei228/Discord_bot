import random
import string


def gen_pass(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    
    return password

print(gen_pass(12)) 



def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
