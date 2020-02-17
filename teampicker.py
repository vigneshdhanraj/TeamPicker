import sys
import json
import random


class Getteam:
    def __init__(self, team="format.json"):
        self.team = team

    def getteamlist(self):
        with open(self.team, "r") as f:
            res = json.load(f)
            return res.get("Team")

    def combineteams(self):
        combineteam = []
        Teamlist = self.getteamlist()
        for team in Teamlist:
            if team.get("Team1"):
                for t in team['Team1']:
                    t['Teamname'] = "Team1"
                    combineteam.append(t)
            elif team.get("Team2"):
                for t in team['Team2']:
                    t['Teamname'] = "Team2"
                    combineteam.append(t)
        return combineteam

    def pickrandom(self):
        allrounder = 0
        bat = 0
        bowl = 0
        wk = 0
        team1 = 0
        team2 = 0
        teamlist = self.combineteams()
        sample = random.sample(teamlist, 11)
        for s in sample:
            if s['Teamname'] == "Team1":
                team1 = team1 + 1
            else:
                team2 = team2 + 1
            if s['Role'] == "ALL":
                allrounder = allrounder + 1
            elif s['Role'] == "BAT":
                bat = bat + 1
            elif s['Role'] == "BOWL":
                bowl = bowl + 1
            elif s['Role'] == "WK":
                wk = wk + 1
        total_credit = sum([s['Credit'] for s in sample])
        if (
            (
                (allrounder >= 1) and (
                    allrounder <= 4)) and (
                (bat >= 3) and (
                    bat <= 6)) and (
                        (bowl >= 3) and (
                            bowl <= 6)) and (
                                (wk >= 1) and (
                                    wk <= 3))) and (
                                        (team1 >= 4) and (
                                            team1 <= 7)) and (
                                                total_credit <= 100.0):
            print("================================================================")
            print ("\nTotal Credit Used: " + str(total_credit) + "\n")
            print (
                "Bat: " +
                str(bat) +
                " Bowl: " +
                str(bowl) +
                " ALL: " +
                str(allrounder) +
                " WK: " +
                str(wk) +
                " Team1: " +
                str(team1) +
                " Team2: " +
                str(team2))

        else:
            sample = self.pickrandom()
        return sample

    def output_printer(self, wk, bat, bowl, allround):
        print("\n<<<<<<<<<Wicket Keepers<<<<<<<<<<")
        for s in wk:
            print(s['Name'])
        print("\n<<<<<<<<<<<<Batsmen<<<<<<<<<<<<<<")
        for s in bat:
            print(s['Name'])
        print("\n<<<<<<<<<<<AllRounders<<<<<<<<<<<")
        for s in allround:
            print(s['Name'])
        print("\n<<<<<<<<<<<<Bowlers<<<<<<<<<<<<<<")
        for s in bowl:
            print(s['Name'])
        return 0

    def selecting_cap(self, team):
        cap = random.sample(team, 2)
        print (
            "\nCAPTAIN: " +
            cap[0]['Name'] +
            "\tVICE-CAPTAIN: " +
            cap[1]['Name'] +
            "\n")
        return 0

    @staticmethod
    def worker(name="format.json"):
        obj = Getteam(name)
        team = obj.pickrandom()
        sorted_team = sorted(team, key=lambda i: i['Role'])
        wk = [s for s in sorted_team if s['Role'] == "WK"]
        bat = [s for s in sorted_team if s['Role'] == "BAT"]
        bowl = [s for s in sorted_team if s['Role'] == "BOWL"]
        allround = [s for s in sorted_team if s['Role'] == "ALL"]
        obj.output_printer(wk, bat, bowl, allround)
        obj.selecting_cap(sorted_team)
        return sorted_team


def pickteams(name="format.json"):
    i = 1
    while i <= 11:
        ret = Getteam.worker(name)
        i = i + 1
    return 0


def work(name="format.json"):
    if len(sys.argv) == 2:
        ret = Getteam.worker(sys.argv[1])
    else:
        ret = Getteam.worker()
    while True:
        print("================================================================")
        opt = raw_input(
            "Are you Statisfied with the Selection (Y/N): ").lower()
        if opt == "yes" or opt == "y":
            while True:
                con = raw_input("Do you want one more team? (Y/N): ").lower()
                if con == "yes" or con == "y":
                    ret = Getteam.worker(sys.argv[1])
                    while True:
                        print(
                            "================================================================")
                        opt = raw_input(
                            "Are you Statisfied with the Selection (Y/N): ").lower()
                        if opt == "no" or opt == "n":
                            cap = random.sample(ret, 2)
                            print (
                                "\nCAPTAIN: " +
                                cap[0]['Name'] +
                                "\tVICE-CAPTAIN: " +
                                cap[1]['Name'] +
                                "\n")
                        else:
                            break
                elif con == "no" or con == "n":
                    break
                else:
                    print("Sorry, I didn't Understand that.Please Say Yes or NO (Y/N)")
                    continue
            print("\n")
            return 0
        elif opt == "no" or opt == "n":
            cap = random.sample(ret, 2)
            print (
                "\nCAPTAIN: " +
                cap[0]['Name'] +
                "\tVICE-CAPTAIN: " +
                cap[1]['Name'] +
                "\n")
        else:
            print("Sorry, I didn't Understand that.Please Say Yes or NO (Y/N)")
            continue
    return 0


if __name__ == "__main__":
    opt = raw_input(
        "Select any one option: 1) ONE BY ONE  Mode 2) AUTO Mode: ")
    if len(sys.argv) == 2:
        if opt == "2":
            ret = pickteams(sys.argv[1])
        else:
            ret = work(sys.argv[1])
    else:
        if opt == "2":
            ret = pickteams()
        else:
            ret = work()
