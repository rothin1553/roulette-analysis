import sys

sys.path.append("..")


from original_code.test_roul import test_case1, test_case2


dataPoints = []

win_threshold = 300
while win_threshold <= 400:
    test = 100
    win_count = 0
    for i in range(test):
        if(test_case2(win_threshold=win_threshold)>= win_threshold):
            win_count+=1
    point = {
        "label": f"${win_threshold}",
        "y"    : win_count/test*100
    }
    dataPoints.append(point)

    win_threshold += 10

import json

outfile = open("data_points.json", "w")
outfile.writelines(json.dumps(dataPoints, indent=4))
outfile.close()
