choice1 = input("You are driving to work in your wifes car when you realise you forgot your lunch. Do you TURN around and go home and get it or do you CONTINUE driving to work?         ") 
if  choice1.lower() == 'turn':
    choice2 = input("As you are driving home you have an accident in her car. Do you phone your WIFE first to tell har about the accident or do you phone our BOSS to tell her you won't be coming in today?     ")
    if  choice2.lower() == 'wife':
        choice3 = input("Your wife swears at you for wrecking her car. Do you SWEAR back at her or do you tell her you are SORRY?         ")
        if  choice3.lower() == 'swear':
            print("You had better get home and sort this out with your wife!")
        elif choice2.lower() == 'sorry':
            print("Your wife forgives you and you tell your boss you are taking the day off!")    
        else:
            print ('If you did submit an answer please resubmit because I did not understand')
    elif choice2.lower() == 'boss':
        print("Your boss tells you to go home and settle things with your wife") 
    else:  
        print ('If you did submit an answer please resubmit because I did not understand')
elif  choice1.lower() == 'continue':
    choice2 = input("As you are driving home you have an accident in her car. Do you phone your WIFE first to tell har about the accident or do you phone our BOSS to tell her you won't be coming in today?     ")
    if  choice2.lower() == 'wife':
        choice3 = input("Your wife swears at you for wrecking her car. Do you SWEAR back at her or do you tell her you are SORRY?         ")
        if  choice3.lower() == 'swear':
            print("You had better get home and sort this out with your wife!")
        elif choice2.lower() == 'sorry':
            print("Your wife forgives you and you tell your boss you are taking the day off!")    
        else:
            print ('If you did submit an answer please resubmit because I did not understand')
    elif choice2.lower() == 'boss':
        print("Your boss tells you to go home and settle things with your wife") 
    else:  
        print ('If you did submit an answer please resubmit because I did not understand')
    
    
    choice2 = input("You get to work and then realize that you have two dollars to buy lunch. Do you go WITHOUT lunch or do you BORROW ten dollars from your boss so you can buy a sandwich?      ")
else:
    print ('If you did submit an answer please resubmit because I did not understand')
            
         
         
         
         






if  choice2.lower() == 'without':
    choice3 = input("You take your two dollars to the vending machine at lunchtime and buy a CHOCOLATE bar or a bag of CHIPS. Which do you choose?        ")
if  choice3.lower() == 'chips':
    choice4 = input("Regardkess of what you chose from the vending machine you are not going to feel as good as would have had you had your lunch.  ")
if  choice3.lower() == 'chocolate':
    choice4 = input("Regardkess of what you chose from the vending machine you are not going to feel as good as would have had you had your lunch.  ")
if  choice2.lower() == 'borrow':
    choice3 = input("Your boss gives you twenty dollars and tells you to work an EXTRA hour or pay it bqck to her TOMORROW? Which option do you choose?     ")



