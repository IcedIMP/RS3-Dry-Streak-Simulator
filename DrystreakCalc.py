
import random
import math

# Script to simulate repeated content and the likelihood/size of drystreaks
def drystreak(chances,droprate,runs):
    drops = [2]*chances
    count = 0; dry = 0; drymax = 0; dryav = 0; dryruns = 0

    for i in range(runs):
        for j in range(chances):
            drops[j] = random.randint(1,droprate)

        # 1 is drop anything else is miss
        if(min(drops) == 1):
            count += drops.count(1)
            drymax = max(drymax,dry)
            if(dry > droprate/chances):
                dryav += dry
                dryruns += 1
            dry = 0
        else:
            dry += 1
    
    print("obtained " + str(count) + " drops")
    print("this is equiv to " + str(count/runs*droprate/chances) + " times droprate") 
    print("the longest dry streak was " + str(drymax))
    print("the average dry streak was " + str(dryav/dryruns) + " runs long")

# set the parameters for the simulation
def main():

    # runs: the number of completions to simulate
    #
    # chances:  is the number of chances you have 
    #           to recieve a drop when you defeat 
    #           the boss
    # droprate: is the INTEGER chance (one in droprate 
    #           (1/droprate)) of the drop. must be the
    #            same rate for each of 'chances' 
    #           
    # ie -  at ed2 you have 3 chances at a 1 in 100 
    #       droprate item so chances = 3 droprate = 100
    # 
    # ed2 -- ed3 solo comment out respectively can add for any other boss
    #

    runs = 1500000

    chances = 3; droprate = 100 #ed2
    #chances = 1; droprate = 55 #ed3
    #chances = 1; droprate = 284 #Nex AoD for INDIVIDUAL person to get wand or orb in group of 7 OR LESS
    #chances = 2; droprate = 400 #Solak crossbows
    #chances = 1; droprate = 200 #Solak grimoire
    #chances = 1; droprate = math.ceil(1000/23) #Raksha for any boots/unique minus pet (less accurate, faster runtime)
    #chances = 23; droprate = 1000 #Raksha for any of boots or unique minus pet (more accurate, much slower (lower 'runs'))

    drystreak(chances,droprate,runs)

   

if __name__ == "__main__":
    main()



