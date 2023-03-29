def lottoGenerator():
    import random
    randNum = 0
    for i in range(5):
        i = i + 1
        randNum = random.randint(1,100)
        print(str(i) + ') Lucky number: ' + str(randNum))
    if i == 5:
        print('Try again? Y/N')
        restart = input()
    if restart  == 'y' or restart == 'yes' or restart == 'Y' or restart == True or restart == 'Yes' or restart == 'YES':
        lottoGenerator()
    else:
        print('Goodbye')
lottoGenerator()
