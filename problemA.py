import sys
import time
import operator


def main():
    n = input("please input your cases:\n")
    for i in range(1, n + 1):
        detect_case(i)


def detect_case(case):
    array = []
    for i in range(4):
        array.append(sys.stdin.readline()[0:4])
    sys.stdin.readline()
    result = detect_winner(array)
    sys.stdout.write("Case #{}: {}\n".format(case, result))


def detect_winner(array):
    if win(array, 'X'):
        return "X won"
    elif win(array, 'O'):
        return "O won"
    elif not_complete(array):
        return "Game has not completed"
    else:
        return "Draw"


def win(array, player):
    for i in range(4):
        if reduce(operator.and_, [(ele == 'T') or (ele == player) for
                  ele in [array[i][j] for j in range(4)]], 1):
            return True
        if reduce(operator.and_, [(ele == 'T') or (ele == player) for
                  ele in [array[j][i] for j in range(4)]], 1):
            return True

    if reduce(operator.and_, [(ele == 'T') or (ele == player) for
              ele in [array[i][i] for i in range(4)]], 1):
        return True

    if reduce(operator.and_, [(ele == 'T') or (ele == player) for
              ele in [array[i][3 - i] for i in range(4)]], 1):
        return True

    return False


def not_complete(array):
    for i in range(4):
        if reduce(operator.and_, [('.' == m) for 
                  m in [array[i][j] for j in range(4)]], 1):
            return True
    return False


if __name__ == "__main__":
    start_time = time.clock()
    main()
    #sys.stderr.write("Used {}(s) to run finish detecting.\n".format(time.clock() - start_time))
