import marimo

__generated_with = "0.9.26"
app = marimo.App(width="medium")


@app.cell
def __():
    from copy import deepcopy
    from collections import Counter

    data = "92 0 286041 8034 34394 795 8 2051489"

    data = data.split()

    def blink(stones): 
        new_stones = Counter()

        for stone in list(stones.keys()): 
            if stone == 0:
                new_stones[1] += stones[0] 
            elif len(stone_str := str(stone)) % 2 == 0:
                split = len(stone_str) // 2
                stone1, stone2 = int(stone_str[:split]), int(stone_str[split:])
                new_stones[stone1] += stones[stone]
                new_stones[stone2] += stones[stone]
            else: 
                new_stones[stone*2024] += stones[stone]
        return +new_stones

    output = Counter(map(int, data))
    for _ in range(25): 
        output = blink(output)
    print(sum(output.values())) # 239714

    output = Counter(map(int, data))
    for _ in range(75): 
        output = blink(output)
    print(sum(output.values())) # 284973560658514
    return Counter, blink, data, deepcopy, output


@app.cell
def __():
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
