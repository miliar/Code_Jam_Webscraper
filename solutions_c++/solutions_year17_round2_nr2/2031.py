#include <cstdio>
#include <string>
#include <unordered_map>
using namespace std;
int tests, N, R, O, Y, G, B, V;

unordered_map<long long, bool> possible;

inline long long encode(int R, int Y, int B, int startCol, int lastCol) {
    long long result = startCol;
    result = (result << 10) + R;
    result = (result << 10) + Y;
    result = (result << 10) + B;
    result = (result << 2) + lastCol;

    return result;
}

struct col {
    int no;
    char repr;
};
col A[4];

bool isTerminal(int R, int Y, int B) {
    return R + Y + B == 0;
}

bool get(int R, int Y, int B, int startCol, int lastCol) {
    //printf("STATE: R: %d, Y: %d, B: %d, startCol: %d, lastCol: %d\n", R, Y, B, startCol, lastCol);
    long long currState = encode(R, Y, B, startCol, lastCol);
    auto it = possible.find(currState);
    if (it != possible.end()) {
        return it -> second;
    }

    if (isTerminal(R, Y, B)) {
        possible[currState] = (startCol != lastCol);
        return startCol != lastCol;
    }

    // try with nextCol = red
    if (R > 0 && startCol != 0 && get(R - 1, Y, B, 0, lastCol)) {
        possible[currState] = true;
        return true;
    }
    // try with nextCol = yellow
    if (Y > 0 && startCol != 1 && get(R, Y - 1, B, 1, lastCol)) {
        possible[currState] = true;
        return true;
    }
    // try with nextCol = blue
    if (B > 0 && startCol != 2 && get(R, Y, B - 1, 2, lastCol)) {
        possible[currState] = true;
        return true;
    }
    
    possible[currState] = false;
    return false;
}

void recons(int R, int Y, int B, int startCol, int lastCol, string& result) {
    long long currState = encode(R, Y, B, startCol, lastCol);

    if (isTerminal(R, Y, B)) {
        result += A[lastCol].repr;
        return ;
    }

    if (R > 0 && startCol != 0 && get(R - 1, Y, B, 0, lastCol)) {
        result += 'R';
        recons(R - 1, Y, B, 0, lastCol, result);
        return ;
    }

    if (Y > 0 && startCol != 1 && get(R, Y - 1, B, 1, lastCol)) {
        result += 'Y';
        recons(R, Y - 1, B, 1, lastCol, result);
        return ;
    }

    result += 'B';
    recons(R, Y, B - 1, 2, lastCol, result);
}

int main() {
    freopen("neighbors.in", "r", stdin);
    freopen("neighbors.out", "w", stdout);

    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);

        A[0] = {R, 'R'};
        A[1] = {Y, 'Y'};
        A[2] = {B, 'B'};

        bool possible = false;
        string result;
        for (int startCol = 0; startCol < 3 && !possible; startCol++) {
            if (A[startCol].no > 0) {
                for (int endCol = 0; endCol < 3 && !possible; endCol++) {
                    if (A[endCol].no > 0 && startCol != endCol) {
                        int chosenRed = startCol == 0 || endCol == 0;
                        int chosenYellow = startCol == 1 || endCol == 1;
                        int chosenBlue = startCol == 2 || endCol == 2;

                        if (get(R - chosenRed, Y - chosenYellow, B - chosenBlue, startCol, endCol)) {
                            possible = true;
                            result += A[startCol].repr;
                            recons(R - chosenRed, Y - chosenYellow, B - chosenBlue, startCol, endCol, result);
                        }
                    }
                }
            }
        }

        printf("Case #%d: ", test);
        if (!possible) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%s\n", result.c_str());
        }
    }

    return 0;
}