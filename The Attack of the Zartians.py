import random
robots = False
key = False
dragonshead = False
MartiansHelp = "None"
MartianWeapon = "None"
SpaceshipWeapon = "None"
print("Welcome to THE ATTACK OF THE ZARTIANS!!!")
print("You have been assigned to find water on Mars. You are totally not qualified for the job. What could possibly go wrong?")    
        #global variable here. give them options for blaster and sword in Spaceship for dragon fight.
def Spaceship():
    global SpaceshipWeapon
    print("You are in the Spaceship!")
    answer = input("What weapon do you want to bring: A. Blaster B. Sword C. None: ")
    if answer == "A.":
        SpaceshipWeapon = "Blaster"
        print("The Blaster is in your inventory!")
    elif answer == "B.":
        SpaceshipWeapon = "Sword"
        print("The Sword is in your inventory!")
    else:
        print("The inventory is empty!")           
    answer = input("Where do you want to go? A. Martian River B. Sand Dunes: ")
    if answer == "A.":
        MartianRiver()
    else:
        SandDunes()
def MartianRiver():
    global key
    answer = input("Where do you want to go next? A. Go upstream B. Go Explore C. Go downstream D. Cross the River E. Leave: ")
    if answer == "A.":
        MartianPalace()
    elif answer == "B.":
        answer = input("You found a key! Where do you want to go next? A. Upstream B. Downstream C. Cross the River D. Leave: ")
        key = True
        if answer == "A.":
            MartianPalace()
        elif answer == "B.":
            SandDunes()
        elif answer == "C.":
            StrangesLab()
        else:
            Spaceship()
    elif answer == "C.":
        SandDunes()
    elif answer == "D.":
        StrangesLab()
    else:
        Spaceship()

def MartianPalace():
    global MartianWeapon
    global MartiansHelp
    print(dragonshead)
    if dragonshead == False:
        number = random.randrange(1, 11)
        if number <= 5:
            print("The Martians thought you were an enemy, and they killed you!")
            Spaceship()
        else:
            print("The Martians want to make a deal with you. If you kill the dragon, they will help you get the Andromeda Stone back. Hint: The dragon is hidden in one of the caves. ")
            answer = input("Decide if you want to take the deal or not. YES or NO (put it in all caps): ")
            if answer == "YES":
                print("They await you with the dragon's head.")
            answer = input("Where do you want to go? A. Sand Dunes B. Zartian Nest C. Leave: ")
            if answer == "A.":
                SandDunes()
            elif answer == "B.":
                ZartianNest()
            else:
                Spaceship()
    elif dragonshead == True:
        print("You return to the Palace with the head of the Dragon. The Martians thank you for your service.")
        answer = input("What would you like the Martians to do for you? A. Help you defeat the Zartians B. Distract the Zartians C. Ask for a weapon: ")
        if answer == "A.":
            MartiansHelp = "troops"
            print("You gain the Martians' help.")
            ZartianNest()
        elif answer == "B.":
            print("The Martians will follow you to the Zartian Nest and help distract the Zartians.")
            MartiansHelp = "distraction"
            ZartianNest()
        else:
            print("You have asked for a weapon.")
            answer = input("Which weapon would you like? (Warning: You are immediately sent to the Zartian Nest once you choose a weapon) A. Martian Rocket Propelled Grenade B. Lightsaber C. Martian Bow and Arrow: ")
            if answer == "A.":
                MartianWeapon = "RPG"
                print("The Martians understand that you need to go to the Zartian Nest. They provide you with transportation.")
                ZartianNest()
            elif answer == "B.":
                MartianWeapon = "lightsaber"
                print("The Martians understand that you need to go to the Zartian Nest. They provide you with transportation.")
                ZartianNest()
            else:
                MartianWeapon = "bow"
                print("The Martians understand that you need to go to the Zartian Nest. They provide you with transportation.")
                ZartianNest()

def StrangesLab():
    global robots
    if key == False:
        print("You have arrived at Strange's Lab")
        answer = input("What do you want to consume? A. Sandwich B. Potion: ")
        if answer == "A.":
            print("You are not hungry anymore.")
            answer = input("Where do you want to go? A. Zartian Nest B. Martian Palace C. Leave: ")
            if answer == "A.":
                ZartianNest()
            if answer == "B.":
                MartianPalace()
            else:
                Spaceship()
        else:
            print("You drank a poisonous potion and died.")
            Spaceship()
    if key == True:
        print("Strange recognized the key in your hand. He says that if you give him the key, he will give you robots that will defeat the Zartians immediately.")
        robots = True
        answer = input("Where do you want to go? A. Zartian Nest B. Martian Palace C. Leave: ")
        if answer == "A.":
            ZartianNest()
        elif answer == "B.":
            MartianPalace()
        else:
            Spaceship()
def SandDunes():
    print("You have made it to the Sand Dunes!")
    answer = input("Where do you want to go? A. Go south B. Go North C. Leave: ")
    if answer == "A.":
        Oasis()
    elif answer == "B.":
        print("You died in quicksand!")
        Spaceship()
    else:
        Spaceship()
def Oasis():
    print("You have found the Oasis!")
    answer = input("Where do you want to go? A. Mossy Cave B. Mythos Cave C. Leave: ")
    if answer == "A.":
        MossyCave()
    elif answer == "B.":
        MythosCave()
    else:
        Spaceship()
def MossyCave():
    answer = input("What do you want to do? A. Explore the East B. Explore the West C. Leave: ")
    if answer == "A.":
        number = random.randrange(1, 11)
        if number <= 8:
            print("You step on a sea urchin and die.")
            Spaceship()
    elif answer == "B.":            
        print("Explore s e w t - Hint: Unscramble the letters to know where to go next.")
        answer = input("Enter your guess: ")
        while answer.lower() != "west":
            print("Wrong! Guess Again.")
            answer = input("Enter your guess: ")
        answer = input("What do you want to do next? A. Keep exploring the East B. Explore the West C. Leave: ")
        if answer == "A.":
            print("You were bitten by a Zartian spider. You died!")
            Spaceship()
        elif answer == "B.":
            print("You explore the West and accidentally stumbled into the Zartian Nest.")
            ZartianNest()
        else:
            Spaceship()
    else:
        Spaceship()
                
def MythosCave():
    global dragonshead
    print("You have arrived at the Mythos Cave!")
    answer = input("What do you want to do? A. Eat Green Seaweed B. Eat Red Seaweed: ")
    if answer == "A.":
        print("You got poisoned and died.")
        Spaceship()
    else:
        print("Nothing Happened.")
        answer = input("What do you want to do next? A. Explore B. Leave: ")
        if answer == "A.":
            print("You explore and find the dragon!")
            answer = input("The dragon fires a fireball at you. What do you do? A. Stab dragon B. Try to dodge C. Try to run D. Leave: ")
            if answer == "A.":
                print("You got burnt to a crisp and died.")
                Spaceship()
            elif answer == "B.":
                print("You rolled out of the way, and a rock falls onto the dragon. The dragon is stunned")
                answer = input("You have a chance to kill the dragon! Do you want to: A. Stab the dragon B. Blast dragon C. Run D. Leave: ") 
                if answer == "A.":
                    print("You cut of the dragon's head")
                    dragonshead = True
                    MartianPalace()
                elif answer == "B.":
                    print("You blasted it, and the dragon's heart was burnt to a crisp. You cut off its head.")                   
                    dragonshead = True    
                    MartianPalace()
                elif answer == "C.":
                    print("You try to run out of the cave, but the dragon blocks the exit. The dragon eats you.")
                    Spaceship()
            elif answer == "C.":
                print("You try to run out of the cave, but the dragon blocks the exit. The dragon eats you.")
                Spaceship()
            else:
                Spaceship()
        else:
            Spaceship()
#not done
def ZartianNest():
    global MartiansHelp
    global MartianWeapon
    if MartiansHelp == "None":
        print("You have arrived at the Nest!")
        answer = input("Where do you want to go? A. Control Room B. Throne Room C. Meeting Room: ")
        if answer == "A.":
            print("You didn't have any protection. You died.")
            Spaceship()
        elif answer == "B.":
            print("You didn't have any protection. You died.")
            Spaceship()
        else:
            print("You didn't have any protection. You died.")
            Spaceship()
    if MartiansHelp == "troops":
        print("You have arrived at the Nest!")
        answer = input("Where do you want to go? A. Control Room B. Throne Room C. Meeting Room: ")
        if answer == "A.":
            print("The Martians cannot go into the Control Room. You must go in by yourself.")
            print("You go in by yourself. Zartians attack you and you die.")
            Spaceship()       
        if answer == "B.":
            print("You and the Martians go into the Throne Room. Hundreds of Zartians are there, and they are ready for battle. You and the Martians attack and kill all of the Zartians. YOU HAVE WON!!")
            answer = input("You have won over the Zartians. What would you like to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            else:
                print("You have finished the game.")
        if answer == "C.":
            print("You and the Martians are in Meeting Room. The Queen Zartian is in there with her Zartian soldiers. The Martians go and attack the Zartians while you go behind and kill the Queen. YOU HAVE WON!!")
            answer = input("You have won and are the new Zartian leader. What would you like to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            if answer == "B.":
                print("You have finished the game.")
    if MartiansHelp == "distraction":
        print("You have arrived at the Nest!")
        answer = input("Where do you want to go? A. Control Room B. Meeting Room C. Throne Room: ")
        if answer == "A.":
            print("The Martians distract the other Zartians while you go into the Control Room. You kill the Zartian Soldiers and are now in control of all the Zartians. YOU HAVE WON THE GAME!!")
            answer = input("What do you want to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            if answer == "B.":
                print("You have finished the game.")
        if answer == "B.":
            print("The Martians distract the surrounding Zartians while you go into the Meeting Room. You realize the Zartians outnumber you and they kill you. You died.")
            Spaceship()
        if answer == "C.":
            print("The Martians are outside the Throne Room to distract the other Zartians. You go into the Throne Room and there are hundreds of Zartian soldiers. They attack and kill you quickly. You're dead.")
            Spaceship()
    if MartianWeapon == "RPG":
        print("You have arrived at the Nest!")
        answer = input("Where do you want to go? A. Control Room B. Meeting Room C. Throne Room: ")
        if answer == "A.":
            print("You sneak into the Control Room. The Zartians soldiers are distracted, and you blast them! The main control system blows up with the Zartians soldiers, and you now have control over the Zartians. YOU HAVE WON!!")
            answer = input("What do you want to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            if answer == "B.":
                print("You have finished the game.")
        elif answer == "B.":
            print("You go into the Meeting Room. There are hundreds of Zartians surrounding the Queen Zartian. You blast three RPGs towards them. Some of the Zartian Soldiers are dead, but the rest attack you. You fall right as the first laser hits you. You're dead.")        
            Spaceship()
        else:
            print("You go into the Throne Room. Immediately, the Zartian soldiers notice you! You blast as much RPGs as you could, but nothing worked against them! You're dead.")
            Spaceship()
    if MartianWeapon == "lightsaber":
        print("You have arrived at the Nest!")
        answer = input("Where do you want to go? A. Control Room B. Meeting Room C. Throne Room: ")
        if answer == "A.":
            print("You sneak into the Control Room. The Zartians soldiers are distracted, but they soon notice you as you pull out your lightsaber. You cut through a lot of Zartian soldiers, but not enough. The Zartian soldiers slice you into pieces. You're dead.")
            Spaceship()
        elif answer == "B.":
            print("You go into the Meeting Room. Your lightsaber gives you away with its bright light. The Zartian soldiers automatically surround you by the Queen Zartian's command. You start to swing your lightsaber around you, and it ends up slicing every Zartian in the room without the Queen realizing. You stab the Queen. YOU HAVE WON!!")
            answer = input("What do you want to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            if answer == "B.":
                print("You have finished the game.")
        else:
            print("You go into the Throne Room. The Zartians are distracted. You stab each and every Zartian in the room, but more Zartians rush in. You are immediately beheaded with a Zartian's sword. You are dead.")
            Spaceship()
#The Bow is OP  
    if MartianWeapon == "bow":
        print("You have arrived at the Nest!")
        answer = input("Where do you want to go? A. Control Room B. Meeting Room C. Throne Room: ")
        if answer == "A.":
            print("As you sneak into the Control Room you fire an arrow at the closest Zartian. You thought you shot one arrow, but hundreds of arrows are shot. It kills every Zartian in the Control Room. YOU HAVE WON!!") 
            answer = input("What do you want to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            if answer == "B.":
                print("You have finished the game.")
        elif answer == "B.":
            print("You go into the Meeting Room. Hundreds of Zartians turn toward you. You fire an arrow. Hundreds of arrows come out of that one shot. The arrows kill all of the Zartians. YOU HAVE... More Zartians rush into the Meeting Room. You tried shooting another arrow, but you realize you only had one. The Zartians kill you. You are dead.")
            Spaceship()
        else:
            print("You go into the Throne Room. The Royal Zartian Family is there with their Zartian soldiers. You shoot an arrow and kills every Zartian in the room. YOU HAVE WON!!")
            answer = input("What do you want to do now? A. Restart B. End game: ")
            if answer == "A.":
                Spaceship()
            if answer == "B.":
                print("You have finished the game.")
                            
Spaceship()     