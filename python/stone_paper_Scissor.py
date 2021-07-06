import random
def stone_paper_scissor(choice):
    list1 = ['stone', 'paper', 'scissor']
    dict1 = dict(enumerate(list1))
    y = random.randint(0,2)
   # y1 =dict1[y]
    if choice == dict1[y]:
        print('no winner', f'your choice = {choice} and my choice = {dict1[y]}')
    elif choice == 'stone' and dict1[y] == 'paper':
        print ('I am the winner', f'your choice = {choice} and my choice = {dict1[y]}')
    elif choice == 'stone' and dict1[y] == 'scissor':
        print ('you are winner', f'your choice = {choice} and my choice = {dict1[y]}')
    elif choice == 'paper' and dict1[y] == 'stone':
         print ('you are winner', f'your choice = {choice} and my choice = {dict1[y]}')
    elif choice == 'paper' and dict1[y] == 'scissor':
         print ('computer winner', f'your choice = {choice} and my choice = {dict1[y]}')
    elif choice == 'scissor' and dict1[y] == 'stone':
         print ('computer winner', f'your choice = {choice} and my choice = {dict1[y]}')
    else:
         print ('you are winner', f'your choice = {choice} and my choice = {dict1[y]}')
    return


def main():
    choice = eval(input("enter 'stone', 'paper', or 'scissor'"))
    if choice == 'stone' or 'paper' or 'scissor':
        print(f'you entered {choice}. Proceed? \n yes to proceed no to cancel')
        confirmation = eval(input())
        if confirmation == 'y' or 'Y' or 'yes' or 'yes' or 'YES':
            stone_paper_scissor(choice)
        else:
            print('exit')
    else:
        print('wrong input, exiting')
    return

if __name__ == '__main__':
    main()