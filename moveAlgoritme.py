import numpy as np
tg = [[2,0,0,0],[2,0,0,2],[2,0,0,2],[2,0,0,2]]






def moveLeft(l):
    if l[0] == 0:
        if l[1] == 0:
            if l[2] == 0:
                # print(1)
                return [l[3],0,0,0]
            else: 
                if l[2] == l[3]:
                    # print(2)
                    return [2*l[2], 0, 0, 0]
                else: 
                    # print(3)
                    return [l[2],l[3],0,0]
        else: 
            if l[2] == 0:
                if l[1]==l[3]:
                    # print(4)
                    return [2*l[3],0,0,0]
                else:
                    # print(5)
                    return [l[1],l[3],0,0]
            else: 
                if l[1] == l[2]:
                    # print(6)
                    return [2*l[1], l[3], 0, 0]
                else: 
                    if l[2] == l[3]:
                        # print(7)
                        return [l[1], 2*l[2], 0, 0]
                    else: 
                        # print(8)
                        return [l[1],l[2],l[3],0]


    else: 
        if l[1] == 0:
            if l[2] == 0:
                # print(9)
                if l[3] == l[0]:
                    return [2*l[0],0,0,0]
                return [l[0],l[3],0,0]
            else: 
                if l[0] == l[2]:
                    # print(10)
                    return [2*l[0], l[3], 0, 0]
                else: 
                    if l[2] == l[3]:
                        # print(11)
                        return [l[0],2*l[2],0,0]
                    else: 
                        # print(12)
                        return [l[0],l[2],l[3],0]
                    
        else: 
            if l[0] == l[1]:
                if l[2] == 0:
                    return [2*l[0],l[3],0,0]
                else: 
                    if l[2]==l[3]:
                        return [2*l[0],2*l[2],0,0]
                    else: 
                        return [2*l[0],l[2],l[3],0]

            else:
                if l[1] == l[2]:
                    # print(13)
                    return [l[0],2*l[1],l[3],0]
                else: 
                    if l[3]==l[2]: 
                        # print(14)
                        return [l[0],l[1],2*l[2],0]
                    else:
                        # print(15)
                        return [l[0],l[1],l[2],l[3]]
    # print(16)
    return l



# print(moveLeft([0,2,2,0]))



