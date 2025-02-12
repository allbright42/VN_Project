# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Julie")
define d = Character("Dad")
define jd = Character("Jude")
image first_letter_1 = "first letter"

# The game starts here.

label splashscreen:
    scene black 
    with Pause(2)

    show text "JSM Productions presents" with dissolve
    play sound "intro.mp3" volume 0.2  
    with Pause(2)
    hide text with dissolve 
    with Pause(2)
    
    return




label start:

    scene first_letter_1
    play sound "letter_noise.mp3" volume 0.5
    with fade
    with Pause(45)
    
    scene black bg 
    with fade
    play sound "ringtone.mp3" volume 0.2
    "Ring Ring...Ring Ring..."
    play sound "pickup.mp3" volume 0.2
    pause(1)

    scene black bg
    "Ring Ring...Ring Ring..."
    mc "Hey dad, just wanted to call and let you know I just landed."
    d "Hey Kiddo! That's great to hear. Don't forget to call you're Mom and let her know too."
    mc "Yeah I will, don't worry."
    d "Oh and remember no loud mu-"
    mc "No loud music on my headphones while in public, always pay attention to my surroundings, dont trust anyone, I know dad."
    mc "I'm 21 dad please stop treating me like im still a kid."
    d "I'm sorry kiddo, it's just y'know how dangerous the city ca-"
    mc "Oh, sorry dad, getting off the plane right now. Call you back soon."
    d "Oh okay, bye honey."
    play sound "call_end.mp3" 
    pause(2)


    label airport:

    scene  airport_bg
    with fade
    play music "airport_talking.mp3" volume 0.1
    "Immigration Officer" "Excuse me, your passport please?"
    "You hand the officer your passport."
    "Immigration Officer" "Thank you very much. Hmmm Utah?"
    "Immigration Officer" "What brings you to the big apple?"
    mc "Well I got accepted into a writing program and I always wanted to visit New York so I couldn't say no to that offer."
    "Immigration Officer" " Ahh got it. Well everything seems good. Here's your passport and welcome to The Big Apple Ma'am."
    "He hands you back your passport"
    mc "Thank you sir."
    "You head towards the entrance but the Officer yell's something as you start walking."
    "Immigration Officer" "Oh by the way! There's this really good Italian spot that me and my wife go to every Sunday. You should check it out, it's called La Nona"
    mc "Oh thanks! I'll check it out."
    "Immigartion Officer" "Thanks kid! You too!"
    stop music fadeout(1.0)
    jump train


    label train:
        scene outside_airport_bg
        with fade
        mc "Finally, some fresh air after 13 hours in the sky. I'm starving..."
       
        menu:
                mc "Should I listen to that guys recommendation?"

                "Italian Restraunt":
                    mc "Yeah sure why not. Always wanted to try authentic italian food."
                    play sound "ringtone.mp3" volume 0.2
                    "Ring...Ring...Ring"
                    mc "What the..."
                    "Your phone starts to ring."
                    "..."
                    play sound "pickup.mp3" volume 0.2
                    pause(1)
                    d "Sweetie, did you make it out alright?"
                    mc "Yes Dad, I'm okay."
                    d "Thank goodness, alright remember go straight to your apartment alright?"
                    mc "..."
                    mc "Alright Dad I will."
                    d "Alright honey, get there safe. Bye Bye."
                    mc "Bye Dad."
                    play sound "call_end.mp3" 
                    "You hang up the phone."
                    mc "Ugh..."
                    mc "Anyways...let's see how I can get there."
                    jump italy

                "Japanese Restraunt":
                    
                    mc "Nahh, I don't wanna eat something I might not like."
                    mc " There should be a Ramen place near where I'm staying so I should start going."
                    "Ring...Ring...Ring"
                    mc "What the..."
                    "Your phone starts to ring."
                    "..."
                    d "Sweetie, did you make it out alright?"
                    mc "Yes Dad, I'm okay."
                    d "Thank goodness, alright remember go straight to your apartment alright?"
                    mc "..."
                    mc "Alright Dad I will."
                    d "Alright honey, get there safe. Bye Bye."
                    mc "Bye Dad."
                    "You hang up the phone."
                    mc "Ugh..."
                    mc "Anyways... let's see how I can get there."
                    jump japan  
    
    

    label italy:
        scene italy_rest_bg
        with fade
        mc "This should be the place."
        "As you approach the entrance you notice how packed the restaurant is."
        mc "WOAH. WHY IS THIS PLACE FLOODED WITH PEOPLE. IT CANT BE THIS GOOD."
        "Crowd " "IT'S COMING HOME! IT'S COMING HOME! IT'S COMING HOME!"
        mc "What the hell is going on..."
        "You try to walk deeper into the crowded restraunt but you suddenly bump into a wall."
        "Wait it's not a wall... IT'S A GUY?!?"
        show jude_talking at center with moveinright
        with hpunch
        jd "Woah there! Are you alright?"
        "You notice a red stain on your shirt."
        mc "HEY! Watch where you're going man. Just got this shirt..."
        show jude_concerned
        jd "Oh, I'm terribly sorry. Here take this."
        "He hands you a $100 dollar bill"
        show jude_happy
        jd "This should be enough to take care of that."
        mc "Uhh, thanks."
        "You take the $100 bill hesitantly."
        show jude_confused
        jd "Sorry, is it not enough? Here."
        show jude_happy
        "He hands you 200 more dolllars."

        menu: 
            "Accept the $200?"

            "Decline":
                mc "Hey man it was just a spill, you don't have to hand me all of this."
                show jude_talking
                jd "No, No. I insist. I'll be winning it back soon anyway when England score!"
                mc "Huh?"
            
            "Take Money":
                mc "Uhhh, this is a lot but thanks I guess?"
                show jude_neutral
                jd " It's no problem! I'm sure that shirt cost a tooth and leg hehe."

        mc "(This guy's accent...definitely not from here.)"
        "You notice the multiple television screens surrounding the restaurant."
        "Looks like England and Italy are playing against each other, no wonder it's crazy in here"
        show jude_neutral
        jd "Not a fan of football I assume? It's the quarter final of the World Cup! England is bringing it home!"

        menu:
            "What should I say?"

            "Yeah I actually am!":
                mc "Yeah I am actually. I just have been so busy today I didn't have time to watch the game today."
                show jude_happy
                jd "Thats great! Well if you want you can join me and the lads! Drinks on me!"
                
            "No, not really.":
                mc " Yeah, not really a fan of \"Soccer\". All I see are guys throwing themselves on the floor and acting."
                show jude_concerned
                jd "HEY! It’s actually Football. You play with your feet cmon. And for the record it's much more than just \ “guys throwing themselves\ ”, it's a piece of art that is exemplified throughout the entire world."
                mc "(I didn't ask to hear all of that...)"
                jd "Listen, why don't you stay and watch the game with me and the lads for a bit? I can teach you a thing or two about \"SOCCER \" and drinks are on me of course."
                
        menu:
            "What should I do?"

            "Stay":
                mc "You know what? Sure I’ll stay."
                show jude_happy
                jd "Wait really?!? Great! Here follow me."
                jump jude_friends

            "Leave":
                mc "Actually, I should go now because I just land-
                jump jude_friends"




