"""
I took a short break from SoloLearn / 100 days of code to
branch out on my own and explore new concepts and libraries
in Python. Here is a fun, quick little project I did today!
"""

import asyncio
from random import randint


async def rolldice():
    dice1 = randint(1, 100)
    print(dice1)
    dice2 = randint(1, 100)
    await asyncio.sleep(2)
    print(dice2)
    dice3 = randint(1, 100)
    await asyncio.sleep(2)
    print(dice3)


asyncio.run(rolldice())
