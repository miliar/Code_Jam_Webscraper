#include <iostream>
#include <vector>
#include <string>

using namespace std;

void fillCakeCol(int colCnt, string& row, vector<string>& cake) {
    char prevNotQuest = 0;
    int questStartIdx = -1;
    for (int c = 0; c < colCnt; ++c) {
        if (row[c] == '?') {
            if (questStartIdx == -1) {
                questStartIdx = c;
            }

            if (c == colCnt -1 && prevNotQuest != 0) {
                for (int q = questStartIdx; q < colCnt; ++q) {
                    row[q] = prevNotQuest;
                }
            }

        } else {
            if (questStartIdx != -1) {
                for(int q = questStartIdx; q < c; ++q) {
                    if (prevNotQuest == 0) {
                        row[q] = row[c];
                    } else {
                        row[q] = prevNotQuest;
                    }
                }
            }
            questStartIdx = -1;
            prevNotQuest = row[c];
        }
    }
    cake.push_back(row);
}

void fillRowQuest(int rowCnt, vector<string>& cake) {
    int questStartIdx = -1;
    int lastNotQuestIdx = -1;
    for (int r = 0; r < rowCnt; ++r) {
        if (cake[r][0] == '?') {
            if (questStartIdx == -1) {
                questStartIdx = r;
            }

            if (r == rowCnt - 1) {
                for (int q = questStartIdx; q < rowCnt; ++q) {
                    cake[q] = cake[lastNotQuestIdx];
                }
            }
        } else {
            if (questStartIdx != -1) {
                for (int q = questStartIdx; q < r; ++q) {
                    cake[q] = cake[r];
                }
            }
            lastNotQuestIdx = r;
            questStartIdx = -1;
        }
    }
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int R, C;
        cin >> R >> C;

        vector<string> cake;
        for (int j = 0; j < R; ++j) {
            string row;
            cin >> row;
            fillCakeCol(C, row, cake);
        }
        fillRowQuest(R, cake);

        cout << "Case #" << i + 1 << ":" << endl;
        for (int j = 0; j < R; ++j) {
            cout << cake[j] << endl;
        }
    }

    return 0;
}
