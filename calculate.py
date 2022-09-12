import matplotlib.pyplot as plt

class calculate():
    #Initialize variables
    def __init__(self, teamA, teamB):
        self.teamA = teamA              #Team A's shot data
        self.teamB = teamB              #Team B's shot data

        self.twomA = 0                  #Team A two pointers made
        self.totaltwoA = 0              #Team A two pointer attempts
        self.nc3mA = 0                  #Team A non corner threes made
        self.totalnc3A = 0              #Team A non corner three attempts
        self.c3mA = 0                   #Team A corner threes made
        self.totalc3A = 0               #Team A corner three attempts

        self.twomB = 0                  #Team B two pointers made
        self.totaltwoB = 0              #Team B two pointer attempts
        self.nc3mB = 0                  #Team B non corner threes made
        self.totalnc3B = 0              #Team B non corner three attempts
        self.c3mB = 0                   #Team B corner threes made
        self.totalc3B = 0               #Team B corner three attempts

    #Calculates total shots taken by each team
    def allShots(self):
        self.teamAtotalShots = len(self.teamA)
        self.teamBtotalShots = len(self.teamB)

    #Going through each team's shots and checking if shot location is in 2PT zone, and if FG made or not
    def twoShotCalculation(self):
        for i in self.teamA:
            if (float(i[1]) >= -22 and float(i[1]) <= 22 and float(i[1])**2 + float(i[2])**2 <= 564.025):
                self.totaltwoA += 1
                if float(i[3]) == 1:
                    self.twomA += 1

        for i in self.teamB:
            if (float(i[1]) >= -22 and float(i[1]) <= 22 and float(i[1])**2 + float(i[2])**2 <= 564.025):
                self.totaltwoB += 1
                if float(i[3]) == 1:
                    self.twomB += 1

    #Going through each team's shots and checking if shot location is in NC3 zone, and if FG made or not
    def ncThreeShotCalculation(self):
        for i in self.teamA:
            if (float(i[2]) > 7.8 and float(i[1])**2 + float(i[2])**2 > 564.025):
                self.totalnc3A += 1
                if float(i[3]) == 1:
                    self.nc3mA += 1

        for i in self.teamB:
            if (float(i[2]) > 7.8 and float(i[1])**2 + float(i[2])**2 > 564.025):
                self.totalnc3B += 1
                if float(i[3]) == 1:
                    self.nc3mB += 1

    #Going through each team's shots and checking if shot location is in C3 zone, and if FG made or not
    def cThreeShotCalculation(self):
        for i in self.teamA:
            if (float(i[1]) < -22 and float(i[2]) <= 7.8) or (float(i[1]) > 22 and float(i[2]) <= 7.8):
                self.totalc3A += 1
                if float(i[3]) == 1:
                    self.c3mA += 1

        for i in self.teamB:
            if (float(i[1]) < -22 and float(i[2]) <= 7.8) or (float(i[1]) > 22 and float(i[2]) <= 7.8):
                self.totalc3B += 1
                if float(i[3]) == 1:
                    self.c3mB += 1

    #Calculating shot percentages, eFG%, and presenting data through print statements and bar charts
    def printData(self):
        print("Team A shot data")

        #Team A shot percentage calculation
        twoshotPercentageA = self.totaltwoA / self.teamAtotalShots
        print("   2PT shot percentage was " + str(twoshotPercentageA))

        nc3shotPercentageA = self.totalnc3A / self.teamAtotalShots
        print("   NC3 shot percentage was " + str(nc3shotPercentageA))

        c3shotPercentageA = self.totalc3A / self.teamAtotalShots
        print("   C3 shot percentage was " + str(c3shotPercentageA))

        #Team A eFG% calculation
        twoeFGA = (self.twomA + 0.5 * 0) / self.totaltwoA
        print("   2PT eFG was " + str(twoeFGA))

        nc3eFGA = (self.nc3mA + 0.5 * self.nc3mA) / self.totalnc3A
        print("   NC3 eFG was " + str(nc3eFGA))

        c3eFGA = (self.c3mA + 0.5 * self.c3mA) / self.totalc3A
        print("   C3 eFG was " + str(c3eFGA))

        eFGA = ((self.twomA + self.nc3mA + self.c3mA) + (0.5 * (self.nc3mA + self.c3mA))) / self.teamAtotalShots
        print("   Team A's overall eFG% was " + str(eFGA))

        ###########################################################

        print("Team B shot data")

        #Team B shot percentage calculation
        twoshotPercentageB = self.totaltwoB / self.teamBtotalShots
        print("   2PT shot percentage was " + str(twoshotPercentageB))

        nc3shotPercentageB = self.totalnc3B / self.teamBtotalShots
        print("   NC3 shot percentage was " + str(nc3shotPercentageB))

        c3shotPercentageB = self.totalc3B / self.teamBtotalShots
        print("   C3 shot percentage was " + str(c3shotPercentageB))

        #Team B eFG$ calculation
        twoeFGB = (self.twomB + 0.5 * 0)/ self.totaltwoB
        print("   2PT eFG was " + str(twoeFGB))

        nc3eFGB = (self.nc3mB + 0.5 * self.nc3mB) / self.totalnc3B
        print("   NC3 eFG was " + str(nc3eFGB))

        c3eFGB = (self.c3mB + 0.5 * self.c3mB) / self.totalc3B
        print("   C3 eFG was " + str(c3eFGB))

        eFGB = ((self.twomB + self.nc3mB + self.c3mB) + (0.5 * (self.nc3mB + self.c3mB)))/self.teamBtotalShots
        print("   Team B's overall eFG% was " + str(eFGB))

        ###########################################################

        #Bar chart representing Team A and B 2pt shot % compared to 2021-22 NBA average
        teams = ['Team A', 'Team B', 'NBA average']
        twoShotBar = [twoshotPercentageA, twoshotPercentageB, .6004540295]
        plt.bar(teams, twoShotBar)
        plt.title('2pt shot % (OKC vs NBA average)')
        plt.xlabel('Teams')
        plt.ylabel('2pt shot %')
        plt.show()

        #Bar chart representing Team A and B 3pt shot % compared to 2021-22 NBA average
        overallThreeA = (self.totalnc3A + self.totalc3A)/self.teamAtotalShots
        overallThreeB = (self.totalnc3B + self.totalc3B)/self.teamBtotalShots

        teams = ['Team A', 'Team B', 'NBA average']
        threeShotBar = [overallThreeA, overallThreeB, .3995459705]
        plt.bar(teams, threeShotBar)
        plt.title('3pt shot % (OKC vs NBA average)')
        plt.xlabel('Teams')
        plt.ylabel('3pt shot %')
        plt.show()

        #Bar chart representing Team A and B eFG% compared to 2021-22 NBA average
        teams = ['Team A', 'Team B', 'NBA average']
        eFGShotBar = [eFGA, eFGB, .532]
        plt.bar(teams, eFGShotBar)
        plt.title('eFG% (OKC vs NBA average)')
        plt.xlabel('Teams')
        plt.ylabel('eFG%')
        plt.show()

