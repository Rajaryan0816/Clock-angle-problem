#PYTHON PROJECT#

#FUNCTION TO COMPUTE THE ANGLE BETWEEN THE HOUR AND MINUTE HAND
def findAngle(hh, mm):
    #HANDLE 24-HOUR NOTATION
    hh = hh % 12
    #FIND THE POSITION OF THE HOUR'S HAND
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)
    #FIND THE POSITION OF THE MINUTE'S HAND
    m = (mm * 360) // (60)
    #CALCULATE THE ANGLE DIFFERENCE
    angle = abs(h - m)
    #CONSIDER THE SHORTER ANGLE AND RETURN IT
    if angle > 180:
        angle = 360 - angle
    return angle
#CLOCK ANGLE PROBLEM
if __name__ == '__main__':
    hh = int(input("Enter Hour Hands: "))
    mm = int(input("Enter Minute Hand: "))
    print(findAngle(hh, mm))
