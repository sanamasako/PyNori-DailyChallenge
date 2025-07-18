import json, random, datetime, os

def TempFetchFahrenheit(F):
	if F < -20: return "deadly cold"
	elif -19 <= F <= -1: return "extreme cold"
	elif 0 <= F <= 31: return "moderate cold"
	elif 32 <= F <= 49: return "mild cold"
	elif 50 <= F <= 59: return "neutral"
	elif 60 <= F <= 69: return "mild heat"
	elif 70 <= F <= 95: return "moderate heat"
	elif 96 <= F <= 120: return "extreme heat"
	else: return "deadly heat"

def TempFetchCelsius(C):
	if C < -29: return "deadly cold"
	elif -28 <= C <= -17: return "extreme cold"
	elif -18 <= C <= -1: return "moderate cold"
	elif 0 <= C <= 9: return "mild cold"
	elif 10 <= C <= 15: return "neutral"
	elif 16 <= C <= 21: return "mild heat"
	elif 22 <= C <= 32: return "moderate heat"
	elif 33 <= C <= 49: return "extreme heat"
	else: return "deadly heat"

def GenerateChallenge():
	TempF = random.randint(-40,120); TempC = (TempF-32)*(5/9); RandPlayerDEF = random.randint(2,20); RandEnemDEF = random.randint(4,30); StepsNeeded = random.randint(2,20)*5
	EnemyList = ["Bayet", "Siwi", "Oh Deer", "Deer God", "Pessimistick", "Optimistick", "Drizzly Bear", "Simi", "Clef", "Ore Gano"]
	Challenge = {
        "difficult": "false",
	"verified": "false",
	"verifier": "None",
	"type": random.choice(["overworld", "battle"]), # the game will handle the difference between these two locally
        "steps": StepsNeeded,
        "population": min(random.randint(5,50),round(StepsNeeded/2)),
        "enemypool": random.sample(EnemyList, k=random.randint(4,len(EnemyList))),
        "PlayerStats": {
		"HP": random.randint(10,300),
		"ATK": random.randint(2,20),
		"DEF": RandPlayerDEF,
		"Lvl": (RandPlayerDEF//8)+1,
		"VP": random.randint(1,20)*10
        },
        "Weather": {
		"TempF": TempF, "TempC": TempC, "TempStateF": TempFetchFahrenheit(TempF), "TempStateC": TempFetchCelsius(TempC),
			"Humidity": random.choice(["very dry", "mildly dry", "neutral", "mildly humid", "very humid"]),
			"Wind": random.choice(["calm", "breezy", "windy", "strong wind", "powerful wind", "deadly wind"]),
			"Season": random.choice(["Spring", "Summer", "Autumn", "Winter"]),
			"Rain": random.choice(["none", "light", "moderate", "heavy", "torrential"]),
			"Conditions": []
        },
		"CustomEnemy": {
			"HP": random.randint(10,800),
			"ATK": random.randint(2,30),
			"DEF": RandEnemDEF,
			"Lvl": (RandEnemDEF//8)+1
        }
    }
	if Challenge["Weather"]["Rain"] != "none" and TempF > 32: Challenge["Weather"]["Conditions"].append("rain")
	if Challenge["Weather"]["Rain"] != "none" and TempF <= 32: Challenge["Weather"]["Conditions"].append("snow")
	if random.randint(1,10) == 6: Challenge["Weather"]["Conditions"].append("thunder")
	if Challenge["Weather"]["Wind"] != "calm": Challenge["Weather"]["Conditions"].append("wind")
	return Challenge

ChallengeData = GenerateChallenge(); Date = datetime.datetime.now(); Month = Date.month; Day = Date.day; Year = Date.year
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "challenges", f"daily-{Month}-{Day}-{Year}.json"), "w") as f: json.dump(ChallengeData, f, indent=2)
