from random import choice
from time import sleep
import colorama
from colorama import Fore
colorama.init(autoreset=True)

a1=("d e d e d e d e d e").split(" ")
a2=("1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p x").split(" ")

b=("a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0").split(" ")

c=(". . . . . . . . . . . . . . . . . . . . . . . . . . . .   . .    . . . . . . . . . .    . . . . . 1 2 3 4 5 6 7 8 9 0 . . . . . .   . . . . . . . .   . . . . . . . A B C D E F G H   I J K L M N O P   Q R S T U V W X Y Z . . . . . . . . . .   . . . . . . . . . . . . .   . . . . . . . . . . . . . . a b c d e f   g h i j k l m n o   p q r s t u v w x y z . . . . . . . . . . . . . . . . ! @ # $ % & * ( ) _ + = - . . . . . . . . . . . . . . . . . .           ").split(" ")

i=0
while True:
    if i%8==0 or i%3==0:
     z=Fore.RED
     y=Fore.WHITE
    else:
     z=Fore.WHITE
     y=Fore.CYAN
    print(f"00001{choice(a1)}0   {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {z}{choice(b)}{choice(b)} {choice(b)}{choice(b)} {y}{choice(b)}{choice(b)} {choice(b)}{choice(b)} {choice(b)}{choice(b)} {Fore.WHITE}{choice(b)}{choice(b)} {choice(b)}{choice(b)}   {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {Fore.RED}{choice(c)}{choice(c)} {Fore.GREEN}{choice(c)}{choice(c)} {choice(c)}{choice(c)} {Fore.WHITE}{choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} {choice(c)}{choice(c)} ")
    sleep(0.02)
    i+=1