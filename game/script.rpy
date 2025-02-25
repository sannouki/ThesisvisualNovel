
label start:

    #setting up the player.
    scene bg setupscreen
    "Welcome to the game! This is a visual novel game where you can make choices that will affect the outcome of the story."
    
    "What is your name?"
    $ name = renpy.input("Enter your name:").strip() or "Player"
    
    "Ah! I remember now, your name is [name]! Anyhow, let's get started!"
    
    define player = Character("[name]", color="#25ffed", what_size=talkFont)
    
    #chapters 

    # Jump to Scene 1 - scene1funeral.rpy
    play music "donkey remix.mp3"
    $ renpy.music.set_volume(0.1, 0.0, channel="music")  # Set volume to 20% immediately
    jump scene_1
    stop music fadeout 2.0
    


    "thanks for playing!!"
    return
