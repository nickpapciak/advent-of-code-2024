import marimo

__generated_with = "0.9.26"
app = marimo.App(width="medium")


@app.cell
def __():
    import re
    import string

    data = """........0.......................c.................
    ........a.........................................
    .......0........................................r.
    .....W............................................
    ..............Z..F.......................c........
    ..F....a.....................c.......Lr....5......
    ............................v.......L5............
    ..................0.....v............r...E........
    ...a..........................p..E..5...7L.m...Z..
    ......j..0............z.....p.........E...........
    ...j...S...W.7................J........4..........
    ......W........X...............................4..
    W..........................p................M.....
    i........Z....................L.............U.....
    .....z....j..X..............................b....M
    ........................Z......m..................
    ....f.........X........J................4......H..
    y..................p............X.JvmR.U..........
    ..................................................
    ................................4.................
    .........N........................U...............
    ........u...q.......5....J..7.................M...
    .y..i.F...z..........................9x.....A.....
    ...i.....2...zw....Y.........................M....
    ............Bu.................I...........U......
    ..f.....2.......k...........b.........I.......x...
    .f............................................G...
    .O...o.......f...............7.t..Q.G.............
    a.....N....i2.........g..o...RI........G..........
    ......oy...q..........N..H........sQ..............
    ....y..2............K........b........9...m.......
    .......w...............b....Y........G.......A....
    ......uO.w............q.k..Y.....v.............A..
    ...u...K....O..............I......................
    o.O.........w.......Y.........R.Q..............T..
    ......................t...3........k...x...C9.....
    .............q........3..6......t............Q.x..
    V......................N..............S...........
    ..............6....K...............1...n..P.......
    ......8..........................T....H.........1.
    ..................s....t.....3....H.......n.......
    ......K.g6...B...........h..T..l.....P.....9......
    ..................l....k..T....h............1....e
    ............6.........l.......h.....Pe..C.........
    ...........s.V....................e..........C....
    .....8...V.......s.g...........n......e...........
    ..V......B.g...........l.8........................
    ......B.................R..3...............1.....S
    ........................h...................S...CP
    .................................................."""

    data = data.splitlines()

    def is_in_bounds(i, j): 
        return i >= 0 and j >= 0 and i < len(data) and j < len(data[0])
        
    frequencies = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    locations = dict.fromkeys(frequencies, [])

    for _freq in frequencies: 
        for i, row in enumerate(data): 
            # wow you can't use += here because it calls
            # __iadd__ what a sneaky sneaky bug that is
            locations[_freq] = locations[_freq] + [(
                i, j.start()) for j in re.finditer(_freq, row)
            ]
    return data, frequencies, i, is_in_bounds, locations, re, row, string


@app.cell
def __(is_in_bounds, locations):
    def all_pairs(seq): 
        res = []
        for i in range(len(seq)): 
            for j in range(i): 
                res.append((seq[i], seq[j]))
        return res

    def vec2_sum(v1, v2): 
        return v1[0] + v2[0], v1[1] + v2[1]

    def neg_vec(v): 
        return -v[0], -v[1]


    def count_antinodes_simple():
        antinodes = set()
        for freq, locs in locations.items(): 
            pairs = all_pairs(locs)
            for x, y in pairs: 
                diff = vec2_sum(x, neg_vec(y))
                a1 = vec2_sum(x, diff)
                a2 = vec2_sum(y, neg_vec(diff))
                if is_in_bounds(*a1): 
                    antinodes.add(a1)
                if is_in_bounds(*a2): 
                    antinodes.add(a2)
        return antinodes

    # 409
    print(len(count_antinodes_simple()))
    return all_pairs, count_antinodes_simple, neg_vec, vec2_sum


@app.cell
def __(all_pairs, is_in_bounds, locations, neg_vec, vec2_sum):
    def count_antinodes():
        antinodes = set()
        for freq, locs in locations.items(): 
            pairs = all_pairs(locs)
            for x, y in pairs: 
                diff = vec2_sum(x, neg_vec(y))

                while is_in_bounds(*x): 
                    antinodes.add(x)
                    x = vec2_sum(x, diff)

                while is_in_bounds(*y): 
                    antinodes.add(y)
                    y = vec2_sum(y, neg_vec(diff))
                
        return antinodes

    # 1308
    print(len(count_antinodes()))
    return (count_antinodes,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
