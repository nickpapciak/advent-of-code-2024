import marimo

__generated_with = "0.9.26"
app = marimo.App(width="medium")


@app.cell
def __():
    from dataclasses import dataclass
    from time import sleep
    import marimo

    data = """p=49,14 v=-82,-41
    p=27,80 v=67,31
    p=76,93 v=-15,-66
    p=90,62 v=-84,86
    p=62,86 v=46,20
    p=7,72 v=25,26
    p=30,32 v=-92,60
    p=91,40 v=6,1
    p=50,58 v=57,-21
    p=71,79 v=-3,58
    p=84,44 v=36,-59
    p=87,12 v=-62,-95
    p=69,46 v=76,39
    p=50,51 v=-26,-64
    p=41,58 v=30,5
    p=80,97 v=-13,9
    p=52,84 v=98,-50
    p=52,32 v=64,39
    p=52,91 v=61,20
    p=31,22 v=49,45
    p=85,73 v=-43,32
    p=77,15 v=20,-52
    p=17,10 v=74,-3
    p=88,92 v=-54,26
    p=20,46 v=31,-63
    p=42,49 v=-26,44
    p=3,101 v=40,-95
    p=78,77 v=-17,48
    p=10,88 v=-88,55
    p=100,68 v=74,76
    p=42,11 v=-97,-25
    p=88,57 v=-37,93
    p=11,36 v=-33,54
    p=88,61 v=-58,43
    p=66,47 v=-55,82
    p=11,52 v=52,-60
    p=9,48 v=41,-64
    p=70,57 v=61,27
    p=22,80 v=11,11
    p=73,11 v=65,56
    p=79,84 v=-28,41
    p=50,79 v=-93,-12
    p=55,35 v=23,-64
    p=48,26 v=45,29
    p=38,23 v=-86,-54
    p=71,48 v=-21,6
    p=60,98 v=28,-54
    p=75,70 v=59,7
    p=24,71 v=-20,-46
    p=55,88 v=79,-23
    p=13,48 v=44,49
    p=37,73 v=-86,-99
    p=82,12 v=-26,80
    p=13,16 v=-8,30
    p=86,34 v=84,99
    p=45,90 v=-31,68
    p=23,93 v=44,8
    p=3,52 v=-65,-54
    p=64,7 v=16,-30
    p=97,88 v=-67,-39
    p=58,87 v=72,42
    p=8,70 v=-27,5
    p=25,67 v=99,22
    p=48,92 v=19,31
    p=23,46 v=-16,-76
    p=13,101 v=70,13
    p=55,4 v=-25,-39
    p=44,10 v=10,-59
    p=56,2 v=83,67
    p=90,83 v=28,42
    p=28,84 v=7,-12
    p=49,87 v=-7,-50
    p=11,56 v=-76,87
    p=27,72 v=46,-28
    p=76,43 v=-59,32
    p=19,50 v=80,62
    p=12,1 v=44,-84
    p=53,29 v=83,61
    p=57,12 v=-63,-90
    p=67,39 v=38,71
    p=38,78 v=86,26
    p=14,19 v=-72,-85
    p=75,9 v=42,-43
    p=89,33 v=65,-43
    p=77,21 v=-64,54
    p=32,72 v=-45,-71
    p=9,21 v=55,-4
    p=22,49 v=70,-71
    p=86,73 v=-35,-7
    p=32,5 v=-41,-62
    p=14,51 v=89,-92
    p=71,34 v=24,-69
    p=87,18 v=69,-10
    p=58,67 v=4,-28
    p=22,75 v=15,26
    p=73,14 v=-77,24
    p=2,26 v=-12,91
    p=53,3 v=38,-57
    p=49,35 v=-37,-59
    p=25,87 v=52,-83
    p=47,74 v=46,-22
    p=70,22 v=-81,24
    p=46,57 v=23,-76
    p=59,96 v=27,-40
    p=72,77 v=99,28
    p=66,89 v=61,-67
    p=46,43 v=70,-23
    p=30,55 v=-67,48
    p=8,75 v=89,-17
    p=15,29 v=-86,-3
    p=53,2 v=38,-56
    p=6,90 v=55,-83
    p=44,83 v=8,-50
    p=2,56 v=-54,-43
    p=30,13 v=19,-62
    p=21,97 v=-78,-46
    p=13,53 v=70,22
    p=2,5 v=59,56
    p=2,48 v=18,50
    p=81,94 v=92,57
    p=1,1 v=6,-59
    p=99,61 v=-65,-76
    p=99,95 v=-24,35
    p=17,53 v=-84,19
    p=33,77 v=-4,53
    p=100,32 v=-3,-43
    p=60,74 v=-10,97
    p=23,54 v=-57,-75
    p=56,69 v=27,21
    p=58,100 v=-51,44
    p=43,77 v=-41,-93
    p=75,3 v=80,13
    p=66,32 v=72,34
    p=67,67 v=-32,69
    p=80,80 v=-23,-3
    p=62,23 v=-4,48
    p=77,0 v=87,30
    p=2,96 v=-35,-73
    p=15,4 v=4,-38
    p=92,56 v=-54,-16
    p=90,46 v=26,-16
    p=75,2 v=1,67
    p=59,71 v=-59,-33
    p=79,21 v=-62,24
    p=34,99 v=45,14
    p=49,18 v=-37,-76
    p=63,26 v=79,-41
    p=97,54 v=-80,71
    p=66,18 v=69,-30
    p=14,25 v=74,-90
    p=9,95 v=-87,96
    p=24,39 v=-8,83
    p=32,98 v=-75,79
    p=36,50 v=-23,-92
    p=97,36 v=-73,86
    p=66,36 v=23,-53
    p=84,3 v=2,95
    p=89,73 v=48,26
    p=3,94 v=-46,68
    p=61,75 v=-52,-98
    p=51,36 v=8,50
    p=70,48 v=80,-2
    p=32,39 v=-54,4
    p=73,85 v=-92,-72
    p=22,70 v=-12,38
    p=92,48 v=-92,93
    p=100,79 v=-76,-12
    p=1,52 v=-43,65
    p=22,98 v=78,52
    p=35,76 v=-97,48
    p=52,14 v=-48,-74
    p=7,55 v=29,98
    p=79,40 v=-2,-38
    p=90,91 v=57,-72
    p=60,3 v=-14,-94
    p=34,69 v=-56,32
    p=63,19 v=-44,24
    p=48,71 v=-18,-98
    p=90,42 v=-87,9
    p=73,59 v=27,-28
    p=30,66 v=18,-48
    p=9,54 v=-79,-43
    p=57,73 v=-73,-34
    p=75,93 v=-39,60
    p=31,75 v=-98,86
    p=93,86 v=-95,-45
    p=64,33 v=33,4
    p=62,27 v=12,46
    p=76,93 v=91,58
    p=92,23 v=-13,29
    p=54,93 v=69,51
    p=19,53 v=59,-16
    p=78,90 v=84,-7
    p=17,93 v=33,25
    p=100,73 v=5,59
    p=74,39 v=80,28
    p=88,4 v=84,19
    p=63,98 v=-65,-2
    p=81,98 v=32,4
    p=64,89 v=-7,9
    p=88,3 v=-35,9
    p=77,14 v=-62,-79
    p=15,15 v=18,-41
    p=40,4 v=41,-24
    p=14,68 v=89,-98
    p=77,71 v=-14,97
    p=69,28 v=1,-9
    p=16,102 v=-87,52
    p=26,20 v=-62,15
    p=100,25 v=28,-37
    p=22,63 v=93,-5
    p=9,47 v=77,-47
    p=78,36 v=76,-95
    p=41,84 v=52,63
    p=14,6 v=30,-88
    p=99,72 v=59,42
    p=72,45 v=7,-21
    p=99,71 v=-20,-98
    p=30,40 v=-6,82
    p=75,50 v=-99,97
    p=91,80 v=8,44
    p=7,44 v=52,-91
    p=96,12 v=-50,-74
    p=72,48 v=-88,-33
    p=21,7 v=-29,-3
    p=96,38 v=2,-48
    p=33,22 v=86,-36
    p=79,84 v=-36,-77
    p=87,65 v=2,48
    p=46,42 v=98,-11
    p=60,79 v=80,-27
    p=95,3 v=-2,-94
    p=94,75 v=88,-29
    p=16,66 v=-24,48
    p=83,51 v=-24,-64
    p=54,94 v=-10,-7
    p=0,96 v=-8,-96
    p=4,50 v=-31,71
    p=21,98 v=-66,-4
    p=50,85 v=-48,69
    p=71,14 v=5,67
    p=19,56 v=71,6
    p=18,43 v=-16,-49
    p=11,25 v=18,45
    p=38,90 v=-52,-34
    p=50,9 v=-89,73
    p=15,23 v=-20,-65
    p=32,35 v=82,-91
    p=7,52 v=29,38
    p=43,53 v=-11,-97
    p=32,62 v=15,40
    p=20,4 v=40,73
    p=15,95 v=93,-67
    p=13,2 v=52,-36
    p=0,85 v=60,-61
    p=71,21 v=43,-36
    p=61,49 v=16,-70
    p=14,8 v=-53,57
    p=25,97 v=-64,30
    p=42,13 v=-40,2
    p=90,75 v=17,-49
    p=76,50 v=-10,60
    p=98,36 v=-50,17
    p=11,7 v=29,13
    p=55,11 v=12,67
    p=54,73 v=23,-82
    p=67,60 v=-49,27
    p=57,72 v=90,10
    p=9,19 v=-31,29
    p=84,2 v=34,49
    p=56,23 v=-83,-73
    p=19,8 v=15,-74
    p=89,73 v=74,-95
    p=53,29 v=-50,27
    p=94,13 v=57,-32
    p=41,30 v=52,2
    p=58,44 v=-65,-37
    p=22,63 v=15,-85
    p=22,48 v=64,-66
    p=28,41 v=52,-5
    p=67,98 v=-54,75
    p=77,15 v=87,45
    p=33,21 v=-60,34
    p=72,15 v=-21,2
    p=19,93 v=97,-7
    p=58,17 v=-75,-70
    p=61,71 v=66,-82
    p=67,93 v=80,-12
    p=99,44 v=3,-40
    p=13,13 v=-49,32
    p=60,14 v=62,-8
    p=88,30 v=87,85
    p=6,27 v=32,-96
    p=70,76 v=83,-60
    p=37,95 v=67,-26
    p=54,10 v=-10,-84
    p=54,100 v=-44,63
    p=5,95 v=17,-67
    p=3,5 v=85,53
    p=51,73 v=19,-55
    p=30,69 v=-19,97
    p=78,57 v=-35,-10
    p=67,55 v=-17,-21
    p=7,14 v=-8,18
    p=69,11 v=-88,7
    p=30,45 v=-58,-70
    p=28,35 v=-75,77
    p=42,21 v=-82,-74
    p=1,8 v=81,24
    p=3,22 v=51,-95
    p=67,89 v=46,15
    p=32,74 v=-60,-88
    p=64,29 v=-29,88
    p=80,13 v=65,-62
    p=99,56 v=-80,5
    p=55,11 v=-74,-89
    p=71,45 v=20,-22
    p=29,83 v=-53,-44
    p=53,26 v=68,26
    p=95,37 v=-24,61
    p=77,23 v=-52,-90
    p=80,88 v=6,-45
    p=0,7 v=74,39
    p=59,24 v=72,2
    p=93,38 v=56,67
    p=21,9 v=87,-85
    p=56,73 v=51,94
    p=0,47 v=-91,-16
    p=39,16 v=30,-40
    p=18,85 v=18,96
    p=99,49 v=98,1
    p=52,70 v=61,-66
    p=61,86 v=-68,48
    p=29,91 v=74,69
    p=51,62 v=-3,-65
    p=56,91 v=-14,69
    p=13,9 v=-98,46
    p=15,47 v=72,32
    p=19,63 v=-34,16
    p=32,92 v=-56,-77
    p=13,80 v=-1,-77
    p=57,68 v=-89,-17
    p=40,54 v=83,33
    p=44,12 v=90,46
    p=1,37 v=22,-76
    p=61,72 v=58,-43
    p=95,52 v=63,-76
    p=87,77 v=-54,15
    p=28,59 v=-38,-92
    p=29,60 v=-14,18
    p=92,10 v=32,-3
    p=70,82 v=61,15
    p=64,5 v=25,-15
    p=21,70 v=50,9
    p=42,75 v=94,14
    p=15,20 v=-53,67
    p=47,0 v=-97,-19
    p=26,96 v=88,55
    p=53,51 v=-7,-97
    p=26,28 v=-79,23
    p=84,3 v=-73,-74
    p=71,63 v=-40,-11
    p=6,65 v=-16,-44
    p=92,74 v=67,15
    p=31,83 v=-4,-99
    p=88,61 v=88,-27
    p=25,80 v=22,-18
    p=45,62 v=-22,97
    p=42,70 v=-74,73
    p=91,95 v=-13,-83
    p=15,12 v=18,-95
    p=53,57 v=-3,87
    p=32,2 v=-64,41
    p=59,8 v=83,-25
    p=45,56 v=60,87
    p=58,91 v=98,-19
    p=96,76 v=57,-14
    p=50,83 v=-74,79
    p=37,31 v=-11,-58
    p=4,39 v=2,50
    p=14,35 v=94,-30
    p=23,28 v=30,-31
    p=90,78 v=-77,23
    p=36,90 v=81,45
    p=23,51 v=-16,-49
    p=33,80 v=44,-91
    p=95,43 v=92,93
    p=54,102 v=83,79
    p=73,88 v=35,14
    p=98,86 v=-9,9
    p=73,22 v=-96,8
    p=61,99 v=46,-40
    p=86,2 v=84,68
    p=66,35 v=72,-64
    p=28,66 v=56,-99
    p=19,83 v=-83,91
    p=26,59 v=99,10
    p=22,29 v=-83,72
    p=14,41 v=-70,13
    p=47,54 v=-78,28
    p=55,25 v=12,17
    p=42,14 v=-45,23
    p=93,71 v=43,20
    p=62,88 v=-25,-28
    p=85,56 v=-50,-70
    p=97,35 v=29,-80
    p=61,49 v=-6,76
    p=25,0 v=-49,-3
    p=23,45 v=63,81
    p=84,45 v=-81,-22
    p=59,23 v=42,-91
    p=17,99 v=78,-35
    p=30,27 v=-67,-52
    p=68,24 v=-81,45
    p=36,99 v=71,68
    p=55,2 v=37,-56
    p=5,9 v=71,-91
    p=1,62 v=-91,-98
    p=23,91 v=67,85
    p=61,101 v=-29,25
    p=9,8 v=3,19
    p=24,32 v=97,-26
    p=56,100 v=75,-79
    p=87,95 v=-77,20
    p=29,79 v=-64,-50
    p=47,29 v=-63,-53
    p=5,40 v=85,-86
    p=58,14 v=-44,94
    p=29,41 v=-19,12
    p=52,5 v=-92,71
    p=94,57 v=47,38
    p=90,50 v=-47,23
    p=28,48 v=-79,49
    p=61,22 v=53,8
    p=95,69 v=-65,-66
    p=78,54 v=-22,19
    p=59,53 v=-14,-17
    p=2,17 v=51,1
    p=41,87 v=10,70
    p=17,15 v=3,-68
    p=46,60 v=4,81
    p=28,83 v=52,15
    p=93,7 v=70,-90
    p=3,86 v=-48,75
    p=20,20 v=93,83
    p=75,36 v=-14,-9
    p=78,23 v=95,67
    p=94,4 v=72,-85
    p=2,6 v=65,-56
    p=13,33 v=17,27
    p=28,57 v=26,-33
    p=79,36 v=69,-32
    p=40,72 v=95,-80
    p=92,91 v=-92,-23
    p=90,37 v=-95,76
    p=19,75 v=8,76
    p=100,38 v=-69,-65
    p=83,57 v=39,-49
    p=78,42 v=1,-53
    p=37,50 v=86,54
    p=78,72 v=5,-17
    p=6,96 v=44,-2
    p=23,11 v=20,-24
    p=26,3 v=82,-30
    p=39,40 v=71,-58
    p=58,28 v=12,-37
    p=97,38 v=-11,-74
    p=82,10 v=67,64
    p=93,63 v=-31,86
    p=52,70 v=35,-18
    p=76,82 v=84,-89
    p=10,63 v=70,10
    p=87,44 v=66,-82
    p=33,59 v=71,-71
    p=92,34 v=-46,93
    p=85,60 v=-5,51
    p=92,45 v=15,-24
    p=4,3 v=36,41
    p=25,20 v=-16,23
    p=74,78 v=13,29
    p=41,75 v=-3,-39
    p=42,4 v=37,15
    p=66,36 v=-44,-42
    p=18,79 v=-66,-42
    p=94,15 v=-84,-68
    p=5,61 v=-46,-49
    p=72,80 v=27,50
    p=50,78 v=-82,-46
    p=66,13 v=16,67
    p=67,10 v=-25,-36
    p=13,2 v=82,-25
    p=79,63 v=-77,92
    p=58,24 v=-20,16
    p=91,22 v=2,-69
    p=4,29 v=-76,-37
    p=26,32 v=-57,-63
    p=70,28 v=-25,-31
    p=44,55 v=-90,-93
    p=82,54 v=61,93
    p=53,77 v=77,39"""


    WIDTH = 101
    HEIGHT = 103

    @dataclass
    class Robot:
        px : int
        py : int
        vx : int
        vy : int

        def update(self): 
            self.px += self.vx
            self.px %= WIDTH
            self.py += self.vy
            self.py %= HEIGHT

    def parse_data(old_data): 
        data = []
        for robot in old_data.splitlines():
            p, v = robot.split(' ')
            (px, py), (vx, vy) = p[2:].split(','), v[2:].split(',')
            data.append(Robot(int(px), int(py), int(vx), int(vy)))
        return data

    data = parse_data(data)

    def visual_robots(data): 
        locs = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

        for robot in data: 
            locs[robot.py][robot.px] += 1


        res = ""
        for row in locs:
            for item in row: 
                res += str(item) if item else '.'
            res += '\n'
        return res[:-1]


    for _ in range(100):
        for robot in data:
            robot.update()


    def safety_score(data):
        quadrants = [0, 0, 0, 0]
        for robot in data:
            div_horizontal = HEIGHT // 2
            div_vertical = WIDTH // 2
            if robot.px < div_vertical and robot.py < div_horizontal:
                quadrants[0] += 1
            elif robot.px > div_vertical and robot.py < div_horizontal:
                quadrants[1] += 1
            elif robot.px < div_vertical and robot.py > div_horizontal:
                quadrants[2] += 1
            elif robot.px > div_vertical and robot.py > div_horizontal:
                quadrants[3] += 1
        return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]

    # 219150360
    print(safety_score(data))
    return (
        HEIGHT,
        Robot,
        WIDTH,
        data,
        dataclass,
        marimo,
        parse_data,
        robot,
        safety_score,
        sleep,
        visual_robots,
    )


@app.cell
def __(HEIGHT, WIDTH, data, visual_robots):
    def search_base_tree(data): 
        # returns largest string of consecutive 1's for the base of a tree
        locs = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for robot in data: 
            locs[robot.py][robot.px] = True

        longest = 0
        curr = 0
        for row in locs:
            for item in row:
                if item: 
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 0
            curr = 0

        return longest

    longest = 0
    for i in range(10000):
        temp = search_base_tree(data)  
        if temp > longest:
            # Since we did 100 iterations earlier we add 100
            print(i + 100, temp)
            print(visual_robots(data))
            longest = temp
        for r in data:
            r.update()
    return i, longest, r, search_base_tree, temp


@app.cell
def __():
    # winner ends up as 8053
    """.....................1111111111111111111111111111111............................1.........1..........
    .....................1.............................1.................................................
    .....................1.............................1.................................................
    .....................1.............................1............................................1....
    .....................1.............................1......................1.....1....................
    ..................1..1..............1..............1.................................................
    ........1............1.............111.............1.1...............................................
    .....................1............11111............1.................................................
    ......1..............1...........1111111...........1.................................................
    .....................1..........111111111..........1.................................................
    .....................1............11111............1.................................................
    1.........1..........1...........1111111...........1.................................................
    ...........1.........1..........111111111..........1......1....................................1.....
    .....1...............1.........11111111111.........1.................................................
    .....................1........1111111111111........1.......................................1.....1...
    .....................1..........111111111..........1.............................1...................
    .....................1.........11111111111.........1..............................................1..
    .....................1........1111111111111........1.................................................
    ...................1.1.......111111111111111.......1.................................................
    .....................1......11111111111111111......1.........................1.......1...........1...
    .....................1........1111111111111........1.............................................1...
    1....................1.......111111111111111.......1.................................................
    .....................1......11111111111111111......1..............1..................................
    .....................1.....1111111111111111111.....1..............1.............................1....
    .....................1....111111111111111111111....1.................................................
    .....................1.............111.............1...............1.................................
    .....................1.............111.............1.................................................
    .................1...1.............111.............1.................................................
    .....................1.............................1.................................................
    ..1..........1...1...1.............................1...........................1........1............
    .....................1.............................1...................................1.............
    .....................1.............................1.....................................1...........
    .....................1111111111111111111111111111111..............1............1....................."""
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
