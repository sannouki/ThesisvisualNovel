# scene1Funeral.rpy

# Define Fonts (Ensure these are declared before character definitions)
define talkFont = 24
define yellFont = 34
define whisper = 16
# Define Characters
define silas = Character("Silas", color="#ff5252", what_size=talkFont)
define playerYell = Character("Player", color="#25ffed", what_size=yellFont)
define sideChar = Character("sideCharacter", color="#e5ffa7", what_size=yellFont)
define mia = Character("Mia", color="#eeaaff", what_size=talkFont)
label scene_3:
    scene bg inside church or funeral house
    
    player "We walk inside to attend the funeral"
    "We are greeted by a variety of different facial expressions. Some look pitying, some hopeful, some distressed…it’s a lot to take in. I am soon bombarded with people, all offering their condolences."
    "sounds of footsteps and hushed whispers fill the room."

    show sadPlayerImage1
    show sadPlayerImage2
    show sadPlayerImage3
    show sadPlayerImage4

    #override sidecharacter name to woman
    $ sideChar = Character("Woman", color="#e5ffa7")
    sideChar "I’m so sorry for your loss."
    "..."
    pause 3
    $ sideChar = Character("Man", color="#e5ffa7")
    sideChar "I am terribly sorry for your loss. Hannah was one of my best employees."

    player "Thank you."
    show sadPlayersmile
    "I suppose it is nice to see such a turnout." 
    "Despite not having a lot of family, Hannah still managed to make an impact in other's lives."

    show sadPlayerImage
    "Mia, my sister's best friend makes her way over to Silas and I. She looks at me with sorrowful eyes."

    mia "[name] , how have you been holding up?"
    "She puts her hand on my shoulder, there is a pleasant delicateness to her gesture that slightly eases my nerves."



    menu:
        "I’ve been..as good as I can be":
            mia "Yeah, I know it’s hard to be especially, just remember you have people you can talk to about it, I’m one of them."

            player "Thanks for that. I appreciate it."

            "mia hold and comforts [name]"
            mia "No worries. anytime."
        "It’s been a challenge":
            mia "Yeah, I can relate. I keep thinking that I’m dreaming, and that I’ll wake up and she’ll be right there. It’s still hard to believe she is really gone."

            player "That’s exactly how I’ve felt."
            "mia holds [name]"
    
    show sadPlayerImage
    "She gives me a small smile and clasps one of my hands in hers. I’ve never really liked physical affection, but something about the way she does it so gently makes me feel seen."
    
    "The service starts and I take my seat up front with Mia and Silas. One by one, people go up on the stage and share stories about Hannah, and I start to remember that it will be my turn soon. The base of my stomach starts to turn." 

    $ sideChar = Character("Pastor", color="#e5ffa7")
    sideChar "And next on the itinerary is Hannah's sister [name], let’s give her a warm welcome."

    player "My legs start shaking as I stand and make my way towards the stage. I take a scan of the audience once I’m on stage and immediately feel my anxiety worsen."
    
    menu:
        "Look at Mia to calm down":
            "s"
        "Look at Silas to calm down":
            "s"
        "Try to calm down by breathing":
            "s  "
    return
