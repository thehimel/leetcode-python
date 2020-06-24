"""
Question: https://leetcode.com/problems/edit-distance/
Solution: https://www.youtube.com/watch?v=OCsF6u-bLBc
Solution: http://thecodingworld.com/2020/05/31/edit-distance/

The edit distance between two strings is the minimum number of operations
(insertions, deletions, and substitutions of symbols) to transform one string
into another.

Source: short
Target: ports
Output: 3

Source: editing
Target: distance
Output: 5

Source: ab
Target: ab
Output: 0
"""


def edit_distance(source, target):
    table = [
        [0 for i in range(len(target) + 1)]
        for j in range(len(source) + 1)]

    for i in range(len(source) + 1):
        for j in range(len(target) + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i

            elif source[i-1] == target[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(
                    table[i-1][j-1], table[i][j-1], table[i-1][j])

    return table[-1][-1]


def test(source, target, output):
    print("Pass" if output == edit_distance(source, target) else "Fail")


if __name__ == "__main__":
    test("short", "ports", 3)
    test("ab", "ab", 0)
    test("editing", "distance", 5)
