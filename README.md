# PyNori Daily Challenge Generator
As the repository name implies, this exists solely to automatically generate **JSON files** (found in "challenges/") to be used in [PyNori](https://shirley-xml.itch.io/pynori) version 2.0.0 or newer for the "Daily Challenge" feature.

### What exactly is going on here?
Every day at midnight UTC (or at least, approximately), a workflow will automatically execute which generates a new challenge JSON in the format of "daily-MM-DD-YYYY.json", where MM is the current month, DD is the current day, and YYYY is the current year.
**Yes, I use Month/Day/Year format. If you don't, get used to it. I hate all the other formats.**

When the challenge JSON is created, selecting option 7[^1] on the Title Screen will attempt to load today's JSON if it exists (if it doesn't, the game will inform the player that the Daily Challenge hasn't been generated yet and boot them back to the title screen).
If loading the JSON was a success, the game will create a little synopsis of the current challenge and give you the option of playing either the current Daily Challenge or a past one (and of course, returning to the title screen if desired).

### Do I get rewarded for beating the Daily Challenge?
No. The only reward you get from beating Daily Challenges is a sense of accomplishment, if any. If you want actual rewards, play the minigames (not from the Title Screen).

### Types of Challenges
**Overworld**
: The game will create a fake area (fake as in disconnected from the normal areas in the game, similarly to the April Fool's Event) for you to step through. The step requirement, population, and enemy pool will be random. Additionally, there will be randomised weather[^2] to endure while making steps and battling enemies. The challenge is completed when the player reaches the end of the area.

**Battle**
: The game will start a battle with a non-existent enemy with randomised stats (HP, ATK, DEF, Level). Additionally, there will be randomised weather for the player to endure while attacking the enemy. The challenge is completed when the enemy dies.

**In both types of challenges, the player's starting stats are randomised as well. Also, items are not included.**

### Important Note
Since these challenges are generated with RNG, **expect repetitive/similar and potentially impossible challenges from time to time**. Rather than seeing the impossible challenges as a negative, see it as a competition to see who can get the farthest. Who knows, maybe if you get lucky enough, the impossible challenge won't be so impossible. Think of it like a race to verify a Geometry Dash extreme demon.

### Have fun, and make sure to follow [Shirley-XML on itch](https://shirley-xml.itch.io/)!
(and file bug reports if you come across a crash.)

[^1]: From PyNori v1.5.0 to v1.9.1, option 7 was assigned to "Exit Game" (prior to v1.5.0, "Exit Game" was option 6); from v2.0.0 onward, option 7 will be "Daily Challenge" instead, and the number 0 will be used for "Exit Game".
[^2]: PyNori v2.0.0 introduced a weather system for extra immersion. In the main game, the weather is dependent on the player's actual weather in real life.
