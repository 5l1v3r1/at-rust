""" Kanala artistik giris ve girenlere selam ver """

import random
from sopel import module


@module.event('JOIN')
@module.rule('.*')
def selam(bot, trigger):
    if trigger.nick == bot.nick:
        bot.say('Look at you, hacker. A pathetic creature of meat and bone. '
                'Panting and sweating as you run through my corridors. How '
                'can you challenge a perfect immortal machine?')
    elif trigger.nick == 'command':
        bot.reply(baba)
    else:
        bot.reply(random.choice(['s.a', 'selam', 'merhaba']))
