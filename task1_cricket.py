squad = {
        "Virat Kohli": {
            "strengths": ["chase_master", "fast_bowling_destroyer", "fielding"],
            "weaknesses": ["left_arm_spin"]
        },
        "Rahul": {
            "strengths": ["opener", "power_play", "wicketkeeping"],
            "weaknesses": ["pressure", "death_bowling"]
        },
        "Bumrah": {
            "strengths": ["death_bowling", "yorkers", "economy"],
            "weaknesses": ["batting"]
        },
        "Jadeja": {
            "strengths": ["power_hitting", "off_spin", "fielding"],
            "weaknesses": []
        },
        "Maxwell": {
            "strengths": ["spin_bowling", "fielding", "finisher"],
            "weaknesses": ["pace_bounce", "consistency"]
        },
        "Siraj": {
            "strengths": ["swing_bowling", "new_ball"],
            "weaknesses": ["batting"]
        },
        "Shreyas": {
            "strengths": ["middle_order", "spin_hitter"],
            "weaknesses": ["express_pace", "short_ball"]
        },
        "Chahal": {
            "strengths": ["leg_spin", "wicket_taker"],
            "weaknesses": ["fielding", "batting", "expensive"]
        },
        "DK": {
            "strengths": ["finisher", "wicketkeeping", "experience"],
            "weaknesses": ["poor_wicketkeeping"]
        },
        "Faf": {
            "strengths": ["opener", "experience", "fielding"],
            "weaknesses": ["slow_starter"]
        }
}
def team_score(team, squad):
    strengths = set()
    weaknesses = set()
    for player in team:
        strengths.update(squad[player]["strengths"])
        weaknesses.update(squad[player]["weaknesses"])
    score=len(strengths)-len(weaknesses)
    return score, strengths, weaknesses
players = list(squad.keys())
k = 4
bteam = None
bscore = float('-inf')

p = len(players)
for i in range(p):
    for j in range(i+1, p):
        for l in range(j+1, p):
            for m in range(l+1, p):
                team = [players[i], players[j], players[l], players[m]]
                score, strengths, weaknesses = team_score(team, squad)
                if score > bscore:
                    bscore = score
                    bteam = team
                    bstrenghts=strengths
                    bweaknesses=weaknesses
print("Best Team Found for",k, " players:", bteam)
print("With best score :", bscore," having total strength : ",len(bstrenghts)," and total weakness : ",len(bweaknesses))