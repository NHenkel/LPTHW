def start():
  print "Wanna go on an adventure?"

  choice = raw_input("> ")
  if "yes" in choice or "Yes" in choice:
    adventure_time()
  else:
    dead ("You're a goddamn couch potatoe. ")

def adventure_time():
    print "Would you rather go on a survival trip or travel in time?"

    choice = raw_input("> ")
    if "survival trip" in choice or "Survival trip" in choice:
        print "Wow, so you're one of those so called #naturelovers."
        print "Great! Let's do some real survival stuff."
        print "First of all you need any kind of shelter, where you can sleep."
        shelter()
    elif "travel in time" in choice or "Travel in time" in choice:
        print "Well, you seem to be very interested in history."
        time_travel()

def shelter():
    print "You can choose between the following:"
    print "A cold cave "
    print "Or a selfmade wooden tent with a comfy moss bed "

    choice = raw_input("> ")
    if "A cold cave" in choice or "cold cave" in choice:
        print "Great! You can collect some moss to create a comfy and sheltered bed for the night."
        print "The next step will be picking some stuff you can have for dinner."
        food()
    elif "A selfmade wooden tent with a comfy moss bed" in choice or "wooden tent" in choice:
        print "Better think twice... If it starts raining in the night you'll catch a cold and your shelter will be flooded."
        shelter()

def food():
    print "You're walking around the woods and suddenly there's a bunch of mushrooms."
    print "There are incredibly yellow ones and red ones with green dots on it."
    print "Which one do you choose? "
    choice = raw_input("> ")
    if "yellow ones" in choice or "yellow" in choice or "red ones" in choice or "red" in choice:
        dead("Really? Thats something you learn in primary school, not to eat stuff you've never seen before. You'll die through poisoning yourself.")
    elif "none" in choice:
        print "You're a smart little thing."
        print "Rather search for something you already ate. Just to make sure you won't be poisoning yourself."
        campfire()


def campfire():
    print "After a while you found some veggies you could roast/grill."
    print "Therefore you'll need a campfire."
    print "You'll get one tool to make that fire burn."
    print "Which one would you choose?"
    print "A lighter. Half filled with gasoline"
    print "A matchbox with 5 matches."

    choice = raw_input("> ")
    if "A lighter" in choice or "lighter" in choice:
        print "Nice. You'll inflame a huge campfire in front of you cave."
        print "Now you can roast your veggies, warm yourself and keep dangerous animals away overnight while you're sleeping."
        exit (0)
    elif "A matchbox" in choice or "matchbox" in choice:
            dead ("They won't be enough to inflame a whole campfire, as the wind will blow out the first before you can light the another one.")

def time_travel():
    print "Which year would you like to travel to?"
    choice = raw_input("> ")
    year = int(choice)
    if year < 1850:
        print "You don't have that much engery in your time travel machine to travel that far."
        print "Enter the secret code to get on this badass long journey."
        choice = raw_input("> ")
        if "Alan Turing" in choice or "alan turing" in choice:
            yay()
        else:
            print "Choose another year to collect the missing code to give your machine the extra boost."
            print "Hint: search for a name."
            time_travel()
    elif year > 1850 and year <= 1932:
        print "Wow that was an interesing time back then."
        print "I hope you'll have a lot of fun but please don't forget that you'll have to come back to 2017 after a few hours."
        exit(0)
    elif year >= 1933 and year < 1946:
        print "Nobody wants to die in war and nobody wants to experience WWII if he/she/it dont' has to! What the hell is wrong with you?"
        print "BTW Turing was a pretty important guy these days. I'm sure you've already heard of him before."
        print "You should also travel to the time before 1850. There are a lot more things to discover."
        time_travel()
    elif year >= 1946 and year < 1980:
        print "Well, I hope you'll have fun meeting your teenaged parents. Make sure not to get too drunk with them that you can't find you way back home to 2017."
        exit(0)
    elif year >= 1980 and year < 2010:
        print "80's, 90's, 00's. Make sure to join a party and enjoy the legendary taste of music people had back then."
        print "But don't forget to come back some day."
        exit(0)
    elif year >= 2010 and year <= 2017:
        dead("Are you serious? That was ... like ... yesterday!")
    else:
        dead("Nobody wants to know what happend back then. Don't pretend to be one of those history fanatic peeps.")

def yay():
    print "You made it. Smart ass. Wish you a looooot of fun."
    exit(0)

def dead(why):
    print why, "Seriously? You should just go home an continue watching Netflix."

start()
