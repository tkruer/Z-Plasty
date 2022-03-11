import math
from colorama import Fore
from data.utils import read_file, log_message

#compare theorietical vs actual increase
#make triangle change in way that makes it realizstic, with np or pd

class Zplasty:

    def start(self):
        more = True
        while more:
            try:
                print(Fore.GREEN + "What would you like to Calculate?")
                print(Fore.BLUE + "Enter [1] for ZPlasty Arms")
                print(Fore.BLUE + "Enter [2] for Zplasty Angles")
                print(Fore.BLUE + "Enter [3] for Zplasty Single VS Series")
                print(Fore.BLUE + "Enter [4] for To Quit")
                choice = input(Fore.BLUE + "Choice: ")
                if choice.lower().startswith('1'):
                    Zplasty.zplastyArms()
                if choice.lower().startswith('2'):
                    Zplasty.zplastyAngles()
                if choice.lower().startswith('3'):
                    Zplasty.zplastySingleVsSeries()
                if choice.lower().startswith('4'):
                    more = False
            except ValueError:
                print(Fore.RED + "Please Select An Option.")
                continue

    def __init__(self) -> None:
        self.start()

    def _load_config(self):
        try:
            try:
                self.user_data = read_file("./data/config.json")
            except FileNotFoundError:
                self.user_data = read_file("../data/config.json")
        except FileNotFoundError:
            log_message("Error", "File config.json not found.")
            exit()
        self.FilePath: str = self.user_data["FilePath"]
        self.Arms: str or int = self.user_data["Arms"]


    def zplastyArms():
        #sides and angles
        side_a = float(input('Enter Side A Length: '))
        side_b = float(input('Enter Side B Length: '))
        side_x = float(input('Enter Side X Length: '))
        side_y = float(input('Enter Side Y Length: '))
        side_c = ((side_a*side_a) - (side_b * side_b))
        side_z = ((side_x*side_x) - (side_y * side_y))
        angle_A = math.degrees(math.pi/2)
        angle_X = math.degrees(math.pi/2)
        calc_c = float(math.acos(side_b/side_a))
        calc_y = math.acos(side_y/side_x)
        angle_C = math.degrees(calc_c)
        angle_Z = math.degrees(calc_y)
        angle_B = (180 - ((angle_A)+(angle_C)))
        angle_Y = (180 - ((angle_X)+(angle_Z)))
        #central calculations
        flapOne_a2_plus_b2 = ((side_a)*(side_a) + (side_b)*(side_b))
        flapOne_two_a_b = (2 * (side_a) * (side_b))
        rads_c = math.radians(angle_C)
        flapOne_cos_c = math.cos(rads_c)
        flapOne_c_sqrd = (flapOne_a2_plus_b2 - ((flapOne_two_a_b) * (flapOne_cos_c)))
        flapOne_half = math.sqrt(flapOne_c_sqrd)
        flapTwo_a2_plus_b2 = ((side_x)*(side_x) + (side_y)*(side_y))
        flapTwo_two_a_b = (2 * (side_x) * (side_y))
        flapTwo_rads_c = math.radians(angle_Z)
        flapTwo_cos_c = math.cos(flapTwo_rads_c)
        flapTwo_c_sqrd = (flapTwo_a2_plus_b2 - ((flapTwo_two_a_b) * (flapTwo_cos_c)))
        flapTwo_half = math.sqrt(flapTwo_c_sqrd)
        central = (flapTwo_half + flapOne_half)
        percentIncrease = ((((central) / (side_a)) * 100) - 100)

        print(Fore.YELLOW + f'''
        Side A, B, C {side_a, side_b, side_c} 
        Side X, Y, Z {side_x, side_y, side_z} 
        Angle A, B, C {angle_A, angle_B, angle_C} 
        Angle X, Y, Z {angle_X, angle_Y, angle_Z}
        Flap One Supporting Math {flapOne_a2_plus_b2, flapOne_two_a_b, flapOne_cos_c, flapOne_c_sqrd, flapOne_half}
        Flap Two Supporting Math {flapTwo_a2_plus_b2, flapTwo_two_a_b, flapTwo_cos_c, flapTwo_c_sqrd, flapTwo_half}
        Central {central}
        Percent Increase {percentIncrease} %
        ''')




    def zplastyAngles():
        #sides and angles
        side_a = 2.5
        side_b = 1.25
        side_x = 2.5
        side_y = 1.25
        side_c = ((side_a*side_a) - (side_b * side_b))
        side_z = ((side_x*side_x) - (side_y * side_y))
        angle_A = math.degrees(math.pi/2)
        angle_X = math.degrees(math.pi/2)
        input_c = float(input(f'Please Enter an Angle C In Radians: '))
        input_z = float(input(f'Please Enter an Angle C In Radians: '))
        angle_C = math.degrees(input_c)
        angle_Z = math.degrees(input_z)
        angle_B = (180 - ((angle_A)+(angle_C)))
        angle_Y = (180 - ((angle_X)+(angle_Z)))
        #central calculations
        flapOne_a2_plus_b2 = ((side_a)*(side_a) + (side_b)*(side_b))
        flapOne_two_a_b = (2 * (side_a) * (side_b))
        rads_c = math.radians(angle_C)
        flapOne_cos_c = math.cos(rads_c)
        flapOne_c_sqrd = (flapOne_a2_plus_b2 - ((flapOne_two_a_b) * (flapOne_cos_c)))
        flapOne_half = math.sqrt(flapOne_c_sqrd)
        flapTwo_a2_plus_b2 = ((side_x)*(side_x) + (side_y)*(side_y))
        flapTwo_two_a_b = (2 * (side_x) * (side_y))
        flapTwo_rads_c = math.radians(angle_Z)
        flapTwo_cos_c = math.cos(flapTwo_rads_c)
        flapTwo_c_sqrd = (flapTwo_a2_plus_b2 - ((flapTwo_two_a_b) * (flapTwo_cos_c)))
        flapTwo_half = math.sqrt(flapTwo_c_sqrd)
        central = (flapTwo_half + flapOne_half)
        percentIncrease = ((((central) / (side_a)) * 100) - 100)

        print(Fore.YELLOW + f'''
        Side A, B, C {side_a, side_b, side_c} 
        Side X, Y, Z {side_x, side_y, side_z} 
        Angle A, B, C {angle_A, angle_B, angle_C} 
        Angle X, Y, Z {angle_X, angle_Y, angle_Z}
        Flap One Supporting Math {flapOne_a2_plus_b2, flapOne_two_a_b, flapOne_cos_c, flapOne_c_sqrd, flapOne_half}
        Flap Two Supporting Math {flapTwo_a2_plus_b2, flapTwo_two_a_b, flapTwo_cos_c, flapTwo_c_sqrd, flapTwo_half}
        Central {central}
        Percent Increase {percentIncrease} %
        ''')

    def zplastySingleVsSeries():
        #single ZPlasty calculation
        #Series Zplasty calculation
        #Export valuse for csv
        print(Fore.YELLOW + f'Still Working On it haha')