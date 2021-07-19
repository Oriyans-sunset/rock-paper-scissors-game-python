import random, sys



def convert(user_input):
    if(user_input == 'R'):
        return 1
    if(user_input == 'P'):
        return 2
    if(user_input == 'S'):
        return 3
    if(user_input == 'Q'):
        print('Game has been quit')
        sys.exit()    

while True:
    
    print('Enter R(rock-1), P(paper-2), S(scissors-3) or Q(quit)')
    user_input = convert(input())    
    random_user_input = random.randint(1,3)
    
    if(user_input == 'Q'):
        print('Game has been quit')
        sys.exit()
    if(user_input == 1 and random_user_input == 1):
        print(random_user_input)
        print('Play Again')
    if(user_input == 2 and random_user_input == 1):
        print(random_user_input)        
        print('You Won')
    if(user_input == 3 and random_user_input == 1):
        print(random_user_input) 
        print('Computer Won')
    if(user_input == 1 and random_user_input == 2):
        print(random_user_input)        
        print('Play Again')
    if(user_input == 2 and random_user_input == 2):
        print(random_user_input)        
        print('Play Again')
    if(user_input == 3 and random_user_input == 2):
        print(random_user_input)        
        print('You Won')
    if(user_input == 1 and random_user_input == 3):
        print(random_user_input)        
        print('You Won')
    if(user_input == 2 and random_user_input == 3):
        print(random_user_input)       
        print('Computer Won')
    if(user_input == 3 and random_user_input == 3):
        print(random_user_input)       
        print('Play Again')    
        

            

