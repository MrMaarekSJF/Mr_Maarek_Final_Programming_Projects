import random
import time
#Introductions
print("Your name is Batholomew Fogelburg and you thought it would be easy, but little did you know this would be the toughest case yet.")
#Wait 2 Seconds
#time.sleep(11)
print("\n You are a Norwegian blonde with a handlebar mustache and have the freshest mutton chops in the town, and you live in Chicago, Illinois. You are 6 feet and five inches tall and are extremely thin. You are accompanied by your 4-toed, blue sloth, Bjorn.")
#Beginning of Story
#time.sleep(20)
#Wait 2 seconds
print("\n You have just walked out of a deep dish pizza place after eating a whole Chicago-style pizza. You are walking to your friend’s house. Your friend’s name is Dr. Knut and he is a Despicable Me enthusiast and got his degree in interpretive dance. You arrive at his house that is a spitting image of Gru’s house from Despicable Me. You ring the doorbell and when he does not answer you let yourself in. Dr. Knut comes rushing at you saying ‘Sorry, thought you were a commoner.’ You reply ‘It is alr…,’ but before you could finish you threw up on Dr. Knut. Your barf was salmon pink with blue sloth fur, and it clashed with Dr. Knut’s black suit. You immediately apologize and decide to leave.")
#time.sleep(37)
#Conflict 
#Wait 2 seconds
print("\n You walk a block away and wait at a bench for your Uber driver to arrive. Your Uber decided to take the longest route that took 40 minutes. Just as your Uber arrives, you get a notification telling you that all the socks from Old Navy have been stolen. You are now at a standstill. Will you…")
#time.sleep(21)
print("\n A. Go to the crime scene \n B. Go home and take a nap to ease your stomach \n C. Go get coffee")
#\r = return  \t = tab \n = new line
choice = input("Choose a letter: ")
#Go to crime scene
#A
if choice == 'A':
    print("\n You head to Old Navy, the crime scene, and you inspect the crime scene, but only find the stinkiest puke ever. You notice there are security cameras around the store. As you are heading to the Security Room, the Police stop you saying ‘Please sir come with us.’ You are hesitant. You feel that something is not right, but you continue to go along with the officers. While you go with them, Bjorn decides to spit on one of the officers. The officer snarls at Bjorn, but lets it slide")
    #time.sleep(30)
    print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water. He slides the water over. He says ‘Drink up.’ His voice is raspy and deep, and you decide to please him by drinking the coffee. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months, besides just now.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
    print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go. \n A. You take a left \n B. You take a right")
    choice = input("Choose a letter: ")
#In Sewers
#AA
    if choice == 'A':
        print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
        #time.line(20)
        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
        #time.line(20)
        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
        #time.line(20)
#You run to the police        
        choice = input("Choose a letter: ")
#AAA
        if choice == 'A':
            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
            #time.sleep(15)
            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#AAB
        else:
            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
            choice = input("Choose a letter: ")
#AABA            
            if choice == 'A':
                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                choice = input("Choose a letter: ")
#AABAA                
                if choice == 'A':
                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABAAA                    
                    if choice == 'A':
                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                else:
                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABABA                    
                    if choice == 'A':
                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                        choice = input("Choose a letter: ")
#AABABAA
                        if choice == 'A':
                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                        elif choice == 'B':
                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                        else:
                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
            elif choice == 'B':
                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                choice = input("Choose a letter: ")
#AABBA                
                if choice == 'A':
                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABBAA                   
                    if choice == 'A':
                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                else:
                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABBBA                    
                    if choice == 'A':
                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                        choice = input("Choose a letter: ")
#AABBBAA                        
                        if choice == 'A':
                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                        elif choice == 'B':
                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                        else:
                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
            else:
                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                choice = input("Choose a letter: ")
#AABCA                
                if choice == 'A':
                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABCAA                   
                    if choice == 'A':
                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                else:
                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABCBA                    
                    if choice == 'A':
                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                        choice = input("Choose a letter: ")
#AABCBAA                        
                        if choice == 'A':
                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                        elif choice == 'B':
                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                        else:
                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                        
                        
#AB                
    else:
        print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
        choice = input("Choose a letter: ")
#ABA
#Fight
        if choice == 'A':
            print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
            print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
            #time.line(20)
            print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
            #time.line(20)
            choice = input("Choose a letter: ")
#ABAA            
            if choice == 'A':
                print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                #time.sleep(15)
                print("\n You lose! \n THE END!!!")
            
#Vending Machine
#ABAB
            else:
                print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                choice = input("Choose a letter: ")
#ABABA                
                if choice == 'A':
                    print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                    choice = input("Choose a letter: ")
#ABABAA               
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#ABABAAA                    
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#ABABABA                    
                        if choice == 'A':
                            print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#ABABABAA
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                elif choice == 'B':
                    print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABBA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#AABBBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                else:
                    print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABCA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                            choice = input("Choose a letter: ")
#AABCBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                                
#Run away
#ABB
        elif choice == 'B':
            print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
            print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
            #time.line(20)
            print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
            #time.line(20)
            choice = input("Choose a letter: ")
#ABBA            
            if choice == 'A':
                print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                #time.sleep(15)
                print("\n You lose! \n THE END!!!")
            
#Vending Machine
#ABBB
            else:
                print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                choice = input("Choose a letter: ")
#ABBBA                
                if choice == 'A':
                    print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                    choice = input("Choose a letter: ")
#ABABAA               
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#ABABAAA                    
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#ABABABA                    
                        if choice == 'A':
                            print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#ABABABAA
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                elif choice == 'B':
                    print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABBA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#AABBBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                else:
                    print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABCA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                            choice = input("Choose a letter: ")
#AABCBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                    

#ABC        
        else:
            print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
            print("\n You Lose! \n THE END!!!")
            
#Go home
#B            
elif choice == 'B':
    print("\n You head home. You enter your apartment and...\n A. You turn off all the lights and fall asleep on your bed \n B. You immediately crash on your couch")
    choice = input("Choose a letter: ")
#BA    
    if choice == 'A':
        print("\n You wake up with Bjorn at your side and there is an officer staring at you. She says ‘Mr. Fogelburg, we need you to come with us.’ She then shows you a set of handcuffs. \n A. You make a run for it \n B. You fight \n C. You go with them peacefully")
#Run
#BAA        
        choice = input("Choose a letter: ")
        if choice == 'A':
            print("\n You take Bjorn and shove the officer and rush outside. You ran a block away with no sign of the police. Just as you take a seat on the curb, an officer sneaks up behind you and cuffs you.")
            print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
            print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. You do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
#Sewers            
            choice = input("Choose a letter: ")
#BAAA            
            if choice == 'A':
                print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                #time.line(20)
                print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                #time.line(20)
                print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                #time.line(20)
#You run to the police        
                choice = input("Choose a letter: ")
#BAAAA                
                if choice == 'A':
                    print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                    #time.sleep(15)
                    print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BAAAB                    
                else:
                    print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                    choice = input("Choose a letter: ")
#BAAABA                    
                    if choice == 'A':
                        print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                        choice = input("Choose a letter: ")
#ABABAA               
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#ABABAAA                    
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#ABABABA                    
                            if choice == 'A':
                                print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                choice = input("Choose a letter: ")
#ABABABAA
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                    elif choice == 'B':
                        print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                        choice = input("Choose a letter: ")
#AABBA                
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABBAA                   
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABBBA                    
                            if choice == 'A':
                                print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                choice = input("Choose a letter: ")
#AABBBAA                        
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                    else:
                        print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                        choice = input("Choose a letter: ")
#AABCA                
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABCAA                   
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABCBA                    
                            if choice == 'A':
                                print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                choice = input("Choose a letter: ")
#AABCBAA                        
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

#BAAB                        
            else:
                print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                choice = input("Choose a letter: ")
#Fight
#BAABA                
                if choice == 'A':
                    print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#BAABAA                
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BAABAB                    
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
#BAABABA                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

#Run away
#BAABB                    
                elif choice == 'B':
                    print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#BAABBA                
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
                        
            
#Vending Machine
#BAABBB                    
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
#BAABBBA                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                    
#Launch Bjorn
#BAABC                   
                else:
                    print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                    print("\n You Lose! \n THE END!!!")
            
            
#Fight
#BAB                    
        elif choice == 'B':
            print("\n You take Bjorn and chuck him at the officer’s face, and you swing a punch at another officer who just came into the room, but you miss and fall onto the floor. While you are on the floor, the officer takes advantage of it, and cuffs you. The officer that was attacked by Bjorn lifted Bjorn off her face and put him in a cage. They then take you to the station.")
            print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
            print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. You do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
#Sewers
#BABA            
            choice = input("Choose a letter: ")
            if choice == 'A':
                print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                #time.line(20)
                print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                #time.line(20)
                print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                #time.line(20)
#You run to the police        
                choice = input("Choose a letter: ")
#BABAA                
                if choice == 'A':
                    print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                    #time.sleep(15)
                    print("\n You lose! \n THE END!!!")
            
#BABAB            
                else:
                    print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                    choice = input("Choose a letter: ")
#BABABA                    
                    if choice == 'A':
                        print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                        choice = input("Choose a letter: ")
#ABABAA               
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#ABABAAA                    
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#ABABABA                    
                            if choice == 'A':
                                print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                choice = input("Choose a letter: ")
#ABABABAA
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                    elif choice == 'B':
                        print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                        choice = input("Choose a letter: ")
#AABBA
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABBAA                   
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABBBA                    
                            if choice == 'A':
                                print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                choice = input("Choose a letter: ")
#AABBBAA                        
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                    else:
                        print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                        choice = input("Choose a letter: ")
#AABCA                
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABCAA                   
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABCBA                    
                            if choice == 'A':
                                print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                choice = input("Choose a letter: ")
#AABCBAA                        
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

  #Aligator encounter
#BABB                        
            else:
                print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                choice = input("Choose a letter: ")
#Fight
#BABBA                
                if choice == 'A':
                    print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#BABBAA                
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBAB                    
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
#BABBABA                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

#Run away
#BABBB                    
                elif choice == 'B':
                    print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#BABBBA                
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBBB                   
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
#BABBBBA                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                    
#Launch Bjorn
#BABBC                   
                else:
                    print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                    print("\n You Lose! \n THE END!!!")
                
            
#Peacefully go in
#BAC                
        else:
            print ("\n You put your hands in the air and go with them. They cuff you as a precaution and take you to the station.")
            print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
            print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
#Sewers
#BACA
#WORK HERE            
            choice = input("Choose a letter: ")
            if choice == 'A':
                print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                #time.line(20)
                print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                #time.line(20)
                print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                #time.line(20)
#You run to the police        
                choice = input("Choose a letter: ")
#AAA
                if choice == 'A':
                    print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                    #time.sleep(15)
                    print("\n You lose! \n THE END!!!")
            
#Vending Machine
#AAB
                else:
                    print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                    choice = input("Choose a letter: ")
                    if choice == 'A':
                        print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                        choice = input("Choose a letter: ")
#ABABAA               
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#ABABAAA                    
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#ABABABA                    
                            if choice == 'A':
                                print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                choice = input("Choose a letter: ")
#ABABABAA
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                    elif choice == 'B':
                        print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                        choice = input("Choose a letter: ")
#AABBA                
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABBAA                   
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABBBA                    
                            if choice == 'A':
                                print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                choice = input("Choose a letter: ")
#AABBBAA                        
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                    else:
                        print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                        print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                        choice = input("Choose a letter: ")
#AABCA                
                        if choice == 'A':
                            print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABCAA                   
                            if choice == 'A':
                                print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                        else:
                            print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                            choice = input("Choose a letter: ")
#AABCBA                    
                            if choice == 'A':
                                print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                choice = input("Choose a letter: ")
#AABCBAA                       
                                if choice == 'A':
                                    print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                elif choice == 'B':
                                    print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                else:
                                    print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                            elif choice == 'B':
                                print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                            else:
                                print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                
            else:
                print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                choice = input("Choose a letter: ")
                
                if choice == 'A':
                    print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
                    choice = input("Choose a letter: ")
#ABAA            
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
                
#Vending Machine
#ABAB
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                       
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                
                elif choice == 'B':
                    print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#BABBBA                
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBBB                   
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                       
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                        
                else:
                    print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                    print("\n You Lose! \n THE END!!!")                                

        
            
            
#BB
    else:
        number = random.randrange(1, 3)
#BB1        
        if number == 1:
            print("\n You wake up with Bjorn at your side and there is an officer staring at you. She says ‘Mr. Fogelburg, we need you to come with us.’ She then shows you a set of handcuffs. \n A. You make a run for it \n B. You fight \n C. You go with them peacefully")
            choice = input("Choose a letter: ")
#Run away from police
#BB1A            
            if choice == 'A':
                print("\n You take Bjorn and shove the officer and rush outside. You ran a block away with no sign of the police. Just as you take a seat on the curb, an officer sneaks up behind you and cuffs you.")
                print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
                print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
                choice = input("Choose a letter: ")
#Sewers
#BB1AA                
                if choice == 'A':
                    print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    #time.line(20)
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#AAA
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#AAB
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                       
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                
#BB1AB                
                else:
                    print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                    choice = input("Choose a letter: ")                    
#Fight
#BB1ABA
                    if choice == 'A':
                        print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
                        choice = input("Choose a letter: ")
#ABAA            
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
                
#Vending Machine
#ABAB
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#ABABAA               
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#ABABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                       
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                
                    elif choice == 'B':
                        print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
#You run to the police        
                        choice = input("Choose a letter: ")
#BABBBA                
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBBB                   
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                        
                    else:
                        print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                        print("\n You Lose! \n THE END!!!")                                
       
        
            
#Fight police
#BB1B                    
            elif choice == 'B':
                print("\n You take Bjorn and chuck him at the officer’s face, and you swing a punch at another officer who just came into the room, but you miss and fall onto the floor. While you are on the floor, the officer takes advantage of it, and cuffs you. The officer that was attacked by Bjorn lifted Bjorn off her face and put him in a cage. They then take you to the station.")
                print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
                print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
#Sewers                
                choice = input("Choose a letter: ")
                if choice == 'A':
                    print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    #time.line(20)
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#AAA
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#AAB
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                       
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                
#BB1AB                
                else:
                    print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                    choice = input("Choose a letter: ")                    
#Fight
#BB1ABA
                    if choice == 'A':
                        print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
                        choice = input("Choose a letter: ")
#ABAA            
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
                
#Vending Machine
#ABAB
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#ABABAA               
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#ABABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                       
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                
                    elif choice == 'B':
                        print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
#You run to the police        
                        choice = input("Choose a letter: ")
#BABBBA                
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBBB                   
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#ABABAA               
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#ABABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                       
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                        
                    else:
                        print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                        print("\n You Lose! \n THE END!!!")                                
       
                       
#Peacefully go in
#BB1C                
            else:
                print ("\n You put your hands in the air and go with them. They cuff you as a precaution and take you to the station.")
                print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
                print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
#Sewers                
                choice = input("Choose a letter: ")
                if choice == 'A':
                    print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    #time.line(20)
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#AAA
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#AAB
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                       
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                
#BB1AB                
                else:
                    print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                    choice = input("Choose a letter: ")                    
#Fight
#BB1ABA
                    if choice == 'A':
                        print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
                        choice = input("Choose a letter: ")
#ABAA            
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
                
#Vending Machine
#ABAB
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#ABABAA               
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#ABABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
            

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                       
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                
                    elif choice == 'B':
                        print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
#You run to the police        
                        choice = input("Choose a letter: ")
#BABBBA                
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBBB                   
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#ABABAA               
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#ABABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                       
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                    else:
                        print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                        print("\n You Lose! \n THE END!!!")                                
       
                        
            
#BB2        
        else:
            print("You wake up with Bjorn at your side and there is an officer staring at you. She says ‘Mr. Fogelburg, we need you to come with us.’ She then shows you a set of handcuffs. \n A. You make a run for it \n B. You fight \n C. You go with them peacefully")
#Run away from police
            choice = input("Choose a letter: ")
#BB2A            
            if choice == 'A':
                print("\n You take Bjorn and shove the officer and rush outside. You ran a block away with no sign of the police. Just as you take a seat on the curb, an officer sneaks up behind you and cuffs you.")
                print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
                print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. You do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
                
#Sewers
#BB2AA                
                choice = input("Choose a letter: ")                
                if choice == 'A':
                    print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    #time.line(20)
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
#You run to the police        
                    choice = input("Choose a letter: ")
#AAA
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#AAB
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#ABABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#ABABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#ABABABA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")


                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                       
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                                                


                
#BB1AB                
                else:
                    print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                    choice = input("Choose a letter: ")                    
#Fight
#BB1ABA
                    if choice == 'A':
                        print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
                        choice = input("Choose a letter: ")
#ABAA            
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
                
#Vending Machine
#ABAB
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#ABABAA               
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#ABABAAB                         
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#ABABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#ABABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#ABABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#ABABABAB                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#ABABABAC                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#ABABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#ABABABC                       
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
    

                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                
                    elif choice == 'B':
                        print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
#You run to the police        
                        choice = input("Choose a letter: ")
#BABBBA                
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BABBBB                   
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#AABAA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                        
                    else:
                        print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                        print("\n You Lose! \n THE END!!!")                                
       
                        
            
#BB2B
#Fight  police
            elif choice == 'B':
                print("\n You take Bjorn and chuck him at the officer’s face, and you swing a punch at another officer who just came into the room, but you miss and fall onto the floor. While you are on the floor, the officer takes advantage of it, and cuffs you. The officer that was attacked by Bjorn lifted Bjorn off her face and put him in a cage. They then take you to the station.")
                print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
                print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
                choice = input("Choose a letter: ")
#BB2BA                
                if choice == 'A':
                    print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    #time.line(20)
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
                    choice = input("Choose a letter: ")
#BB2BAA                    
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BB2BAB                    
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
#BB2BABA                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#AABAA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

#BB2BB                    
                else:
                    print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                    choice = input("Choose a letter: ")                    
#Fight
#BB2BBA                    
                    if choice == 'A':
                        print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        #time.line(20)
                        choice = input("Choose a letter: ")
#ABAA            
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
                
#Vending Machine
#ABAB
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#AABAA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

#Run away
#BB2BBB                       
                    elif choice == 'B':
                        print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy.")
                        #time.sleep(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed.")
                        #time.sleep(21)
                        print("It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the person who did it")
                        #time.sleep(21)
#BB2BBC
                        choice = input("Choose a letter: ")
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BB2CAB                    
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#AABAA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


        
                    else:
                        print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                        print("\n You Lose! \n THE END!!!")
#Sewers
#BB2C                        
            else:
                print ("\n You put your hands in the air and go with them. They cuff you as a precaution and take you to the station.")
                print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of water, and slides it over to you. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the water. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
                print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. Do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
                choice = input("Choose a letter: ")
#BB2CA                
                if choice == 'A':
                    print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                    #time.line(20)
                    print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                    #time.line(20)
                    print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                    #time.line(20)
                    choice = input("Choose a letter: ")
#BB2CAA                    
                    if choice == 'A':
                        print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                        #time.sleep(15)
                        print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BB2CAB                    
                    else:
                        print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                        choice = input("Choose a letter: ")
#BB2CABA                        
                        if choice == 'A':
                            print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                            choice = input("Choose a letter: ")
#AABAA               
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABAAA                    
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                elif choice == 'B':
                                    
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABABA                    
                                if choice == 'A':
                                    print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABABAA
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                        elif choice == 'B':
                            print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABBA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABBBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                    choice = input("Choose a letter: ")
#AABBBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                        else:
                            print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                            print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                            choice = input("Choose a letter: ")
#AABCA                
                            if choice == 'A':
                                print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCAA                   
                                if choice == 'A':
                                    print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                       
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                            else:
                                print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                choice = input("Choose a letter: ")
#AABCBA                    
                                if choice == 'A':
                                    print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                    choice = input("Choose a letter: ")
#AABCBAA                        
                                    if choice == 'A':
                                        print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                    elif choice == 'B':
                                        print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                    else:
                                        print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                elif choice == 'B':
                                    print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                else:
                                    print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

#BB2CB                    
                else:
                    print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
                    choice = input("Choose a letter: ")
                    
                    if choice == 'A':
                        print("\n You kick the gator in the mouth, and the aligator staggers back. The gator roars and decides that it is not worth the trouble.It swims away. You laugh frantically. After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        #time.line(20)
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
                        #time.line(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
                        choice = input("Choose a letter: ")
                        
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BB2CBBB                    
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
                            
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#AABAA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                        
               
#Run away
#BB2CBB                       
                    elif choice == 'B':
                        print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
                        #time.sleep(20)
                        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy.")
                        #time.sleep(20)
                        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed.")
                        #time.sleep(21)
                        print("It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the person who did it")
                        #time.sleep(21)                
                        choice = input("Choose a letter: ")
#BB2CBBA                        
                        if choice == 'A':
                            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                            #time.sleep(15)
                            print("\n You lose! \n THE END!!!")
            
#Vending Machine
#BB2CBBB                    
                        else:
                            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                            choice = input("Choose a letter: ")
#BB2CBBBA                       
                            if choice == 'A':
                                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                                choice = input("Choose a letter: ")
#AABAA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABAAA                    
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABABA                    
                                    if choice == 'A':
                                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABABAA
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                            elif choice == 'B':
                                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABBA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABBBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                                        choice = input("Choose a letter: ")
#AABBBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                            else:
                                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                                choice = input("Choose a letter: ")
#AABCA                
                                if choice == 'A':
                                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCAA                   
                                    if choice == 'A':
                                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                                else:
                                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                                    choice = input("Choose a letter: ")
#AABCBA                    
                                    if choice == 'A':
                                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                                        choice = input("Choose a letter: ")
#AABCBAA                        
                                        if choice == 'A':
                                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                                        elif choice == 'B':
                                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                                        else:
                                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                                    elif choice == 'B':
                                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                                    else:
                                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


#BB2CBC                                
                    else:
                        print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
                        print("\n You Lose! \n THE END!!!")
                                       
#Fight
#BB2CBA                                                     
#Coffe shop
#C            
else:
    print("You head to your favorite coffee shop to get some coffee. Just as you open the doors to the coffee shop, you hear the ding that came with it, but then you immediately hear two other dings. You turn around and standing behind you are two officers. You say ‘Hello. How are you.’ They look at you, and by the look they are giving you, you know they are not here to chat. The woman officer asks ‘Are you Mr. Fogelburg?’ You reply ‘So what if I am?’ She answers ‘Sir, you have to come with us.’ You decide to respond with ‘Oh. Well in that case, Mr. Fogelburg is right there.’ While you say this you point to the man working the cash register. The officer takes out a photo of you. She looks at it, and then you. ‘Sir, you have the right to remain silent.’ Is what she tells you, while she is cuffing your hands. She also take Bjorn who is resting on your shoulder, and puts him in a cage.")
    #time.line(20)
    print("\n You are now in an interrogation room with a one sided mirror on the wall to the right of you. The door creaks open and a man comes in. He sets down a cup of coffee. You recognize the coffee, and realize it is your favorite, straight, black coffee. He slides the coffee over. He says ‘Drink up.’ His voice is raspy, and you decide to please him by drinking the coffee. You ask ‘Why am I here?’ He sees you are genuinely confused and says ‘Why, we found your puke at Old Navy after the socks vanished.’ You say ‘That can not be. I have not been to the Old Navy for, for, for months.’ The officer takes another look at you and makes a hand gesture to the mirror. The next thing you know, a woman walks in with Bjorn, and sets him on the table. The man leaves the room with a confused look on his face.")
    print("\n You decide to wait ten minutes and then you use Bjorn’s long claws to pick the lock of the door. It works! You take Bjorn and sneak out of the station. You find a manhole, and lift the cover. You climb down into the sewers. You do not know the sewers well, but you know the land above. You come to a fork in the road, and you forget which way to go.\n A. You take a left \n B. You take a right")
#Sewers go left   
    choice = input("Choose a letter: ")
#CA    
    if choice == 'A':
        print("\n You turn to the left and remember where you are. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
        #time.line(20)
        print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
        #time.line(20)
        print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
        #time.line(20)You run to the police
        choice = input("Choose a letter: ")
#Go to police
#CAA        
        if choice == 'A':
            print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
            #time.sleep(15)
            print("\n You lose! \n THE END!!!")
            
#Vending Maching
#CAB            
        else:
            print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
            choice = input("Choose a letter: ")
            
            if choice == 'A':
                print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                choice = input("Choose a letter: ")
#AABAA                
                if choice == 'A':
                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABAAA                    
                    if choice == 'A':
                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                else:
                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABABA                    
                    if choice == 'A':
                        print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                        choice = input("Choose a letter: ")
#AABABAA
                        if choice == 'A':
                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                        elif choice == 'B':
                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                        else:
                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
            elif choice == 'B':
                print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                choice = input("Choose a letter: ")
#AABBA                
                if choice == 'A':
                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABBAA                   
                    if choice == 'A':
                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                else:
                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABBBA                    
                    if choice == 'A':
                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                        choice = input("Choose a letter: ")
#AABBBAA                        
                        if choice == 'A':
                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                        elif choice == 'B':
                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                        else:
                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                    elif choice == 'B':
                         print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
            else:
                print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                choice = input("Choose a letter: ")
#AABCA                
                if choice == 'A':
                    print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABCAA                   
                    if choice == 'A':
                        print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                else:
                    print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                    choice = input("Choose a letter: ")
#AABCBA                    
                    if choice == 'A':
                        print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                        choice = input("Choose a letter: ")
#AABCBAA                        
                        if choice == 'A':
                            print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                        elif choice == 'B':
                            print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                        else:
                            print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                    elif choice == 'B':
                        print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                    else:
                        print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

                
#Sewers go right
#CB                
    else:
        print("\n You turn to the right and continue for 10 feet when you realize that you are not alone. An alligator springs out of the water. You… \n A. Fight \n B. Run \n C. Launch Bjorn")
        choice = input("Choose a letter: ")
#CBA        
        if choice == 'A':
            print("\n You kick the gator in the mouth, and it dislodges a tooth. The gator roars in agony, and swims away. You pick up its tooth and laugh frantically.")
            print("\n Acquired Item \n Aligator Tooth")
            print("\n SECRET ACHIEVEMENT FOUND! \n 'In Deep Waters'")
            print("After you calm yourself down, you realize you went the wrong way. You retrace your steps to the fork, and this time you go left.  You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
            #time.line(20)
            print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy")
            #time.line(20)
            print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed. It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the culprit")
            #time.line(20)You run to the police
            choice = input("Choose a letter: ")
#Go to police
#CBAA        
            if choice == 'A':
                print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                #time.sleep(15)
                print("\n You lose! \n THE END!!!")
            
#Vending Maching
#CBAB            
            else:
                print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                choice = input("Choose a letter: ")
#CBABA                
                if choice == 'A':
                    print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                    choice = input("Choose a letter: ")
#AABAA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABAAA                    
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABABA                    
                        if choice == 'A':
                            print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#AABABAA
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                elif choice == 'B':
                    print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABBA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#AABBBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                else:
                    print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABCA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                            choice = input("Choose a letter: ")
#AABCBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

            
          
#Run away from Gator
#CBB            
            
        elif choice == 'B':
            print("\n You run back the way you came, and realize you were supposed to go left. You walk for another block and finally decide to plop open a manhole. You climb out and you look around. You are directly in front of Dr.Knut’s house.")
            #time.sleep(20)
            print("\n You stand right outside of his house. You are about to knock when you realize that you don’t want to drag your friend into your problem. You leave. As you are walking you start to think where to go. Bjorn points at your socks and you realize you need to go to the crime scene, Old Navy.")
            #time.sleep(20)
            print("\n You arrive at the crime scene and you walk through the store. You search and search, but you find nothing. Bjorn points at the cameras, but you are not paying attention. He takes matters into his own hands and bites you. You look at him bewildered, and realize he is pointing at the cameras. You think ‘What does Bjorn want with the cameras? You then realize that there are cameras, so there should be a room with the footage of who robbed the store. You find the camera room and break down the door. You rewind the footage to when the store was robbed.")
            #time.sleep(21)
            print("It shows a man with a scarf, gloves, a hat, and a coat on. You think he looks suspicious. You see what looks like puke on his leg. It is salmon colored with blue fur. You come to a conclusion. You take Bjorn and you… \n A. You run to the police \n B. You confront the person who did it")
            #time.sleep(21)
            choice = input("Choose a letter: ")
#CBBA            
            if choice == 'A':
                print("\n You arrive at the police station and tell them that it was none other than your friend Dr. Knut. The police give you a blank stare and arrest you.")
                #time.sleep(15)
                print("\n You lose! \n THE END!!!")
                
#CBBB                
            else:
                print("You rush out of the room, but realize you are hungry. You find a vending machine and get… \n A. A healthy all natural bar \n B. A bag of Lays \n C. Cheez Its")
                choice = input("Choose a letter: ")
#CBBBA               
                if choice == 'A':
                    print("You get your bar, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("\n You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A. Stay and fight \n B. Run away")
                    choice = input("Choose a letter: ")
#AABAA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABAAA                    
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABAAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABAAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABAB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABABA                    
                        if choice == 'A':
                            print(" You have hardly any energy left, but you kick him, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bar, and you unwrap it. You eat it as fast as you can. It fuels you up. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#AABABAA
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
                        
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
                        
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABABB                            
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABABC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
        

#AABB                         
                elif choice == 'B':
                    print("You get your bag, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABBA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABBAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABBAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABBB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABBBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A.  Kick \n B.  Go sicko mode \n C.  Use special sloth power move")
                            choice = input("Choose a letter: ")
#AABBBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABBBAB                         
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover you give him an uppercut. He falls backwards. He is knocked unconscious. You drag his limpless body to the police station. You give the police the recording that Bjorn took. The police then arrest Dr. Knut. \n YOU WIN!!! \n THE END!!!")
#AABBBAC                         
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
##AABBBB                             
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
##AABBBC                         
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")


                    
#AABC                    
                else:
                    print("You get your Cheez Its, but before you can eat it, Bjorn swipes it. You are furious and are about to yell, but all of a sudden, you hear two officers talking. You run out of the Old Navy, and towards Dr. Knut.")
                    print("You are outside of Dr. Knut’s house. You are hesitant to knock on the door. You decide to kick the door down and yell ‘Dr. Knut come face me like a man.’ A chair twirls and sitting it is nonother that Dr. Knut. ‘What are you talking about?’ He questions you. You reply ‘I hate people who steal socks, they are the scum of the earth.’ He answers ‘When I was a child, I was mistreated by my parents. They never got me fabric softener, so my socks were stiff and rigid. In school, I was made fun of for them. Now no one shall ever wear socks, so I can make fun of everyone since I will be the only one with socks.’ You reply ‘Well you see there is one problem.’ ‘What problem?’ Dr. Knut asks. ‘Well you see, while you were confessing, Bjorn recorded it.’ Dr. Knut runs at you and viciously punches you across the face. \n A.  Stay and fight \n B.  Run away")
                    choice = input("Choose a letter: ")
#AABCA                
                    if choice == 'A':
                        print("You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and rips out some of his hair. Dr. Knut retaliates by punching you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCAA                   
                        if choice == 'A':
                            print("You kick him where it hurts, and he falls to the ground. You then drag him to the police station. You show the police the recording that Bjorn took of Dr. Knut confessing. \n YOU WIN!!! \n THE END")
#AABCAB                        
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")
#AABCAC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")
#AABCB                        
                    else:
                        print("You run towards the doors, but they slam on you. Now the only way out is to fight. You throw a punch at him, and it lands squarely on his cheek. While you punch him, Bjorn jumps from your shoulder to his, and tugs on his ears. Dr. Knut rips Bjorn off, and chucks him back at you. Bjorn lands on your face, covering your eyes. While you are blinded, Dr. Knut punches you. \n A. Kick him \n B. Punch \n C. Curl into a ball")
                        choice = input("Choose a letter: ")
#AABCBA                    
                        if choice == 'A':
                            print("You have hardly any energy left, but you kick him where it hurts, and it has no effect. Dr. Knut then slowly walks towards you. Punching you until you fall to the ground. Bjorn then throws you your bag of chips, and you open it. You eat it as fast as you can. You get back up from the ground and you… \n A. Kick him \n B. Go sicko mode \n C. Use special sloth power move ")
                            choice = input("Choose a letter: ")
#AABCBAA                        
                            if choice == 'A':
                                print("You kick, but Dr. Knut catches your foot, and Judo flips you. You land on your head. \n YOU LOSE!!! \n THE END!!!")
#AABCBAB                            
                            elif choice == 'B':
                                print("Bjorn takes your phone and plays Sicko Mode by Travis Scott. You then jump up and punch Dr. Knut from above. Dr. Knut staggers, but without letting him recover move in closer. You are just about to hit him again. All of a sudden, you do not feel too good. The bag of Cheez Its betrayed you. It made you sick. You slowly walk to Dr, Knut clutching your stomach.  Dr. Knut moves in and before he can do anything, you puke. The puke gets all over Dr. Knut’s shoes, and he slips. He falls flat on his face. You stand there wheezing. You could not have taken it anymore, but Dr. Knut is unconscious. You take him to the police station, and show the officers the evidence. They throw Dr. Knut into jail, and they let you go. \n YOU WIN!!! \n THE END")
#AABCBAC                            
                            else:
                                print("You throw your sloth at Dr. Knutt. Bjorn does a 360 midair and lands on Dr. Knut. He continues to circle Dr. Knut and trips him. Dr. Knut gets back up and throws Bjorn. While Dr. Knut throws Bjorn, you rush at him and punch him in the gut. He then passes out. You run to Bjorn. Bjorn is badly injured. You take Dr. Knut to the police station and hand him over to the police with the recording. You then take Bjorn to the vet. The vet says Bjorn will make it, but has been paralyzed. You take Bjorn and decide to end your detective career. \n YOU WIN!!! \n THE END!!!")
#AABCBB
                        elif choice == 'B':
                            print("You punch him, but it has no effect. He then picks you up and chucks you across the room. You pass out. \n YOU LOSE!!! \n THE END")

#AABCBC                        
                        else:
                            print("You curl into a ball, and Dr. Knut repeatedly punches you. You get knocked out. \n YOU LOSE. \n THE END")

        
#Aligator kills
#CBC                
        else:
            print("\n You launch Bjorn, and the gator opens its jaws and bites Bjorn. Bjorn whimpers in agony and falls into the stream. You stand there petrified. You don’t move even when the gator charges at you.")
            print("\n You Lose! \n THE END!!!")
    
