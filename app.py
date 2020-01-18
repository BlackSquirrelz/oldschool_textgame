import random


class Enemy:
    def __init__(self, distance):
        self.distance = distance


def gun_range(deg):
    range = 40000 * round(deg) + 20000
    return range

def fire_canon(gun_range, target):
    print("Gun Range {}".format(gun_range))
    print("Distance to target {}".format(target.distance))
    print("Fire in the whole")
    proximity = target.distance - gun_range
    print(proximity)
    if(abs(proximity) > 100):
        print('Missed \n Try again')
        set_angle()

    elif(abs(proximity) < 100 ):
        print('Target Destroyed, moving on.')
        result = False
        return result
    else:
        print('What the fuck...')
        result = False
        return result

    hit =  0
    return hit

def set_angle():
   angle = int(input("Enter a desired angle, (MIN 1, MAX 89: "))
   print("Your calculated range is {} meters. \n Type fire to shoot the canon, or adjust to adjust the angle of the canon.".format(gun_range(angle)))
   return gun_range(angle)

def main():
    print("Gunner \n - Inspired by Creative Computings Book: 'Basic Computer Games' "
          "\nYou are the officer in charge, giving orders to a gun crew "
          "\n telling them the degrees of elevation you estimate "
          "\n will place a projectile on target. A hit within 100m of the target will destroy it.")



    game_status = True
    while(game_status):
        # positioning the enemy
        min_gunRange = gun_range(1)
        max_gunRange = gun_range(89)
        target = Enemy(random.randint(min_gunRange, max_gunRange))
        print("The target is {} meters away.".format(target.distance))

        angle = set_angle()
        action = input()
        if (action == 'fire'):
            game_status = fire_canon(angle, target)
        else:
            print('Adjusting the angle')
            set_angle()


    print("End of game so far....")
    if(input('Would you like to play another round?')) == 'yes':
        game_status = True
    else:
        print('OK, Goodbye')

if __name__ == '__main__':
    main()
