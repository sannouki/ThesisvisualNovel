# scene1Funeral.rpy

# Define Fonts (Ensure these are declared before character definitions)
define talkFont = 24

# Define Characters
define silas = Character("Silas", color="#ff5252", what_size=talkFont)

label scene_1:
    scene bg forest
    "The wind cuts through the trees, and for a moment, a cold emptiness follows."
    "The earth turns white as shadows shade it in. I see a tall figure in the distance."
    "I narrow my sight towards him."
    show sadPlayerImage
    player "Silas?"
    
    "Silas looks at me with apologetic eyes. I turn away, distracting myself with the bed of roses on the ground."
    show SilasImage
    silas "Are you ok?"
    
    "He hesitates, seemingly regretting his question. He knows the pain I've been through, how many tears the death of my sister has brought me."
    
    silas "I know it's not fair of me to ask that. I'm sorry."
    show sadPlayerImage2
    menu:
        "No, it's fine. I'm...doing better.": 
            player "No, it's fine. I'm...doing better."
        "No, being sorry won’t solve anything.": 
            player "No, being sorry won’t solve anything."
    
    player "I promise I'll figure out who did it and get revenge."
    show SilasImage
    silas "I still think about her a lot. Your sister was so kind... she didn't deserve this."
    
    player "Yeah..."
    "Two weeks... and still no trace of the killer."
    "Silas stares at the ground, he's never been the best at comforting, but neither am I, I suppose."
    "No corpse was found. Not anything except a pool of scattered blood and her ring."
    show sadPlayerImage3
    player "I just can't believe she's gone. I feel so useless."
    
    "Silas places a hand onto my shoulder, examining my dejected disposition."
    show sadPlayerImage2
    silas "We should head inside. The service is about to start."
    
    "It tears me apart knowing that we haven't even done the bare minimum and brought her killer to justice, and now I have to say my last goodbyes to her."
    "I look at the rose bed one last time."
    
    player "They were her favorite."
    
    "I glance at the large decrepit church, taking a breath."
    show SilasImageSerious
    silas "Are you ready?"

    #this boolean will help skip a section of the story.
    default Transitions = False

    menu:
        "Yes.": 
            silas "Ok, let's go. Let me know if it gets to be too much for you."
            $ Transitions = True
        "No.": 
            player "I don't think I can do this, I'm not ready to face all those people..."

    if Transitions == True:
        jump scene_3

    silas "Silas has been my best friend since before I can remember. He's usually much less serious, always teasing and joking with me. It's jarring to see him like this."
    "We walk inside to attend the funeral."
    
    player "I don't think I can do this, I'm not ready to face all those people."
    
    silas "It's ok, you don't have to do anything you don't want to."
    
    player "I don't think I can do this, at least not until I can bring her justice."
    
    return
