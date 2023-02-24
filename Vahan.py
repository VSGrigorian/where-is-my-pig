print('''
---------

Hello.

---------''')
my_name = input("what's your name?")
main_choice = int(input('''Choose the topic. Press 1 for the Silly Hospital Story, Press 2 for the Abnormal Weekend Story. Press 3 for the Strange Letter'''))
print (f'''
---------
Cool, {my_name} jan. I will ask you some random questions. Be patient and fill everything in. You will be amazed in the end (just kidding haha).
---------
OK.Let's start.
---------''')
final = f'''--------
    OK, {my_name} jan! here's your reward.'''
if main_choice == 1:
    num1_1 = input("write some random number") #the number after the underscore (_) symbol indicates that the variable belongs to the choice 1, choice 2 or choice 3
    time_1 = input ("fill in the gap. My ultimate measure of t+ime is ... ?")
    transport_1 = input ("what is your favourite transport?")
    adj1_1 = input ("your favourite adjective?")
    adj2_1= input ("your second favourite adjective?")
    noun1_1= input ("now write a noun maybe?")
    colour1_1 = input ("name some random colour. be creative.")
    body1_1 = input ("we're getting more intimate. your favourite body part?")
    verb1_1 = input ('''name one random verb. but don't write "to" in the beginning''')
    number2_1 = input ("guess a number")
    noun2_1 = input ("write another random noun you like")
    noun3_1 = input ("I know, I know. Be patient. Now write another noun!")
    body2_1 = input ("your least favourite body part")
    noun4_1 = input ("guess what? I want you to name another noun now. Do it for me")
    adj3_1 = input ("wow you're smashing it like a real linguist. write an adjective")
    silly_1 = input ("what's the silliest word that you have heard")
    story_1 = f'''
    ---------
    It was about {num1_1} {time_1}s ago when I arrived at the hospital
    by {transport_1}. The hospital is a rather {adj1_1} place, there are a lot
    of {adj2_1} {noun1_1}s here. There are nurses here who have {colour1_1} {body1_1}s.
    If someone wants to come into my room I told them that they have to {verb1_1} first. I’ve
    decorated my room with {number2_1} {noun2_1}s. Today I talked to a doctor and they were wearing
    a {noun3_1} on their {body2_1}s. I heard that all doctors like to {verb1_1} some {noun4_1} every
    day for breakfast.
    The most {adj3_1} thing about being in the hospital is the {silly_1} {noun1_1} !'''
    print(final)
    print(story_1)
elif main_choice == 2:
    name1_2 = input ("Please write a name and a surname")
    noun1_2 = input ("Please mention one noun")
    adj1_2 = input ("Please insert one adjective, which indicates a feeling")
    adj2_2 = input ("write another feeling - adjective, just like you just did!")
    verb1_2 = input ('''write some verb. but please without "to" in the beginning''')
    animal_2 = input ("Think of one animal. Mention it!")
    verb2_2 = input ("input another verb")
    colour1_2 = input ("think of a colour. name it!")
    verbing1_2 = input ("now I want you to write a verb which is in Present Continuous tense, i.e. ends with -ing")
    adverb1_2 = input ("cool, you know the tenses like a native speaker. Now. Do you remember what's an adverb?? something that answers the question 'How?' and typicalLY ends with -ly. OK? Write one adverb then.")
    number1_2 = input ("write some random number")
    time1_2 = input ("fill in the gap. My ultimate measure of time is ... ?")
    silly1_2 = input ("write me some silly word")
    noun2_2 = input ("Almost done. Write some noun.")
    story_2 = f'''
    ---------
    This weekend I am going camping with {name1_2}. I packed my lantern, sleeping bag,
    and {noun1_2}. I am so {adj1_2} to {verb1_2} in a tent. I am very {adj2_2} we might see one
    {animal_2}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2_2}.
    I have heard that the {colour1_2} lake is great for {verbing1_2}. Then we will {adverb1_2}
    hike through the forest for {number1_2} {time1_2}. If I see a {colour1_2} {animal_2} while hiking,
    I am going to bring it home as a pet! At night we will tell {number1_2} {silly1_2} stories and roast {noun2_2}
    around the campfire!!'''
    print(final)
    print(story_2)
elif main_choice == 3:
    name1_3= input("Please write a name and a surname")
    adj1_3 = input("Please insert one adjective, which indicates a feeling")
    colour1_3 = input("think of a colour. name it!")
    animal1_3 = input ("name some random animal now.")
    place1_3 = input ("input a name of some random place")
    adj2_3 = input ("another adjective please")
    magical1_3 = input ("imagine one magical creature. mention it.")
    magical2_3 = input ("wrong choice. haha. mention another magical creature!")
    adj3_3 = input ("now write an adjective")
    room1_3 = input ("what's your favourite room?")
    noun1_3 = input ("now insert some noun")
    noun2_3 = input ("you're on a roll! another noun, please")
    noun3_3 = input ("I know, I know. Be patient. write another noun but in plural form")
    noun4_4 = input ("not quite there. another plural noun, please")
    adj4_3 = input ("write an adjective for me")
    num1_3 = input ("write one random number")
    time1_3 = input ("fill in the gap. My ultimate measure of time is ... ?")
    verbing1_3 = input("now I want you to write a verb which is in Present Continuous tense, i.e. ends with -ing")
    adj5_3 = input ("reaching the end. write an adjective")
    noun5_5 = input ("almost. and write another noun")
    story_3 = f'''
    ---------
    Dear {name1_3}, I am writing to you from one {adj1_3} castle in an enchanted forest.
    I found myself here one day after going for a ride on a {colour1_3} {animal1_3} in {place1_3}. There are {adj2_3}
    {magical1_3}s and {adj3_3} {magical2_3}s here! In the {room1_3} there is a pool full of {noun1_3}s.
    I fall asleep each night on a {noun2_3} of {noun3_3} and dream of {adj4_3} {noun4_4}.
    It feels as though I have lived here for {num1_3} {time1_3}. I hope one day you can
    visit, although the only way to get here now is {verbing1_3} on a {adj5_3} {noun5_5}!!'''
    print(final)
    print(story_3)
okay= input("OK?")
print ("BYE!")
