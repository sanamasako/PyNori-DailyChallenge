# PyNori Daily Challenge Generator
As the repository name implies, this exists solely to automatically generate **JSON files** (found in "challenges/") to be used in [PyNori](https://shirley-xml.itch.io/pynori) version 2.0.0 or newer for the "Daily Challenge" feature.

**11/10/2025: THE "LAIR" DAILY CHALLENGE TYPE IS CURRENTLY IN DEVELOPMENT. UNTIL THE RELEASE OF v2.3.0, PLEASE DISREGARD ANY MESSAGES TELLING YOU TO UPDATE THE GAME TO PLAY A CHALLENGE. THE UPDATE IS NOT READY YET.**

### What exactly is going on here?
Every day at midnight UTC (or at least, approximately), a workflow will automatically execute which generates a new challenge JSON in the format of "daily-MM-DD-YYYY.json", where MM is the current month, DD is the current day, and YYYY is the current year.
**Yes, I use Month/Day/Year format. If you don't, get used to it. I hate all the other formats.**

In-game, selecting option 7[^1] on the Title Screen will attempt to load today's JSON if it exists (if it doesn't, the game will inform the player that the Daily Challenge hasn't been generated yet and boot them back to the title screen).
If loading the JSON was a success, the game will create a little synopsis of the current challenge and give you the option of playing either the current Daily Challenge or a past one (and of course, returning to the title screen if desired).

### October 2025 Update
Starting in v2.2.0, there will now be a "news feed" for Daily Challenge related updates. Generations, verifications, and difficulty markings will be reported at the top of the Daily Challenge menu, and there will be an option allowing you to view past reports. This additional functionality should not affect versions 2.0.0 to 2.1.2 in any way.

The news feed will be handled by a workflow separate from the one that generates the Daily Challenges. To prevent conflict with the text file that keeps track of recent changes (conveniently named recent_changes.txt), the news feed workflow runs 1 minute after the Daily Challenge one. Luckily, I'm pretty sure you can go far longer than 1 minute without reading today's Daily Challenge news.

### Do I get rewarded for beating the Daily Challenge?
No. The only reward you get from beating Daily Challenges is a sense of accomplishment, if any. If you want actual rewards, play the minigames (not from the Title Screen).

### Types of Challenges
**Overworld**
: The game will create a fake area (fake as in disconnected from the normal areas in the game, similarly to the April Fool's Event) for you to step through. The step requirement, population, and enemy pool will be random. Additionally, there will be randomised weather[^2] to endure while making steps and battling enemies. The challenge is completed when the player reaches the end of the area.

**Battle**
: The game will start a battle with a non-existent enemy with randomised stats (HP, ATK, DEF, Level). Additionally, there will be randomised weather for the player to endure while attacking the enemy. The challenge is completed when the enemy dies.

**Lair (IN DEVELOPMENT)**
: The game will create a fake version of Shadorako's Lair[^3] with up to 10 floors. Each floor can have from 2 to 5 rooms, and each room (with the exception of the last one, which is always the "stairs" type) is random. The challenge is completed when the final floor is cleared. Compatible with PyNori v2.3.0 or newer.

**In all types of challenges, the player's starting stats are randomised as well. Also, items are not included.**

### Important Note
Since these challenges are generated with RNG, **expect repetitive/similar and potentially impossible challenges from time to time**. Rather than seeing the impossible challenges as a negative, see it as a competition to see who can get the farthest. Who knows, maybe if you get lucky enough, the impossible challenge won't be so impossible. Think of it like a race to verify a Geometry Dash extreme demon.

### Have fun, and make sure to follow [Shirley-XML on itch](https://shirley-xml.itch.io/)!
(and file bug reports if you come across a crash.)

[^1]: From PyNori v1.5.0 to v1.9.1, option 7 was assigned to "Exit Game" (prior to v1.5.0, "Exit Game" was option 6); from v2.0.0 onward, option 7 will be "Daily Challenge" instead, and the number 0 will be used for "Exit Game".
[^2]: PyNori v2.0.0 introduced a weather system for extra immersion. In the main game, the weather is dependent on the player's actual weather in real life.
[^3]: A sub-area of Archlekia that was added in v1.9.0.
