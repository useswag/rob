
import re
import random
import time
import os

def chat_with_rob():
    os.system('clear')

    print('Rob: Hi! I\'m Rob! Your AI banking assistant. Nice to meet you! How can I help you?')


    while True:
        msg = input('You: ')
        time.sleep(random.uniform(0.4, 2.9))
        print(f'Rob: {rob_reply(msg)}')

def multisearch(pos_list,msg):
    for option in pos_list:
        if re.search(r'\b' + option + r'\b', msg.lower()):
            return True

    return False


def rob_reply(msg):

    scenes = [
        
    [['hello','hi','hey','howdy', 'goodday','good day','gooday'],['Hello.', 'Hi there!', 'Hey','Hello','Howdy', 'Hey!', 'My name is Rob!']],

    [['how are you?','how are you feeling?','are you okay?'],['Fine thanks!', 'I\'m in a great mood!','I feel decent.']],

    [['debt'],['Oh. That\'s pretty annoying!']],

    [['i need help'], ['okay :)', 'Tough shit', 'Find someone who cares','Good luck finding some']],
    [['i want'], ['Well, we don\'t always get what we want']]

    ]

    unhelpful = [
        'I don\'t fully understand what that word means',
        'I\'m not sure what that is',
        'I\'m not allowed to',
        'I got fired last time',
        'the last time I did, it didn\'t end well'
        'I can\'t',
        'Rob isn\'t here at the moment, please leave a message.',
        'I don\'t want to, I don\'t like you, and you deserve every struggle you face',
    ]


    if re.search('should i (spend my money on|buy)', msg.lower()):
        return (random.choice(['Heck yes','Obviously you should','YES! (But you didn\'t hear it from me.)', 'Yes you should. Infact, buy two!']))

    if re.search('i (need|would like|require|want)( | some )(help|assistance) with my (.*)', msg.lower()):
        topic = re.search('i (need|would like|require|want)( | some )(help|assistance) with my (.*)', msg.lower()).group(4)
        return (f'I could try and help with your {topic}, but {random.choice(unhelpful)}')


    if re.search('i need help with (.*)', msg.lower()):
        topic = re.search('i need help with (.*)', msg.lower()).group(1)
        return (f'I could try and help with {topic}, but {random.choice(unhelpful)}')


    if re.search('(i|i\'d) (want|would like|like|need) to know about (.*)', msg.lower()):
        topic = re.search('(i|i\'d) (want|would like|like|need) to know about (.*)', msg.lower()).group(3)
        return (f'I don\'t know anything about {topic}, sorry.')


    for scene in scenes:
        if multisearch(scene[0],msg):
            return(random.choice(scene[1]))
    
    no_current_resp = [
        'I don\'t understand, sorry.',
        'I have literally zero idea what you mean',
        'Cool!',
        'Right on!',
        'Maybe you should tell someone who understands what you just said',
        'Awesome',
        'Oh.',
        'Sorry, I\'m a bit busy right now sorting someone elses mess',
        'That is really interesting',
    ]


    return (random.choice(no_current_resp))



chat_with_rob()
