#include <bits/stdc++.h>

using namespace std;

int main () {
    int testCases, R, C;
    char temp;
    vector<int> redo;
    vector<vector<char>> cake;

    cin >> testCases;
    for (int curCase = 1; curCase <= testCases; curCase++) {
        cin >> R >> C;

        cake = vector<vector<char>>(R);
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cin >> temp;
                cake[i].push_back(temp);
            }
        }

        bool any = false;
        for (int i = 0; i < R; i++) {
            int begin = 0;
            bool foundFirst = false;
            for (int j = 0; j < C; j++) {
                if (!foundFirst) {
                    if (cake[i][j] != '?') {
                        for (int k = begin; k <= j; k++) {
                            cake[i][k] = cake[i][j];
                            begin = j;
                            foundFirst = true;
                            any = true;
                        }
                    }
                }
                else {
                    if (cake[i][j] == '?') {
                        cake[i][j] = cake[i][begin];
                    }
                    else {
                        begin = j;
                    }
                }
            }
            if (foundFirst == false && any == false) {
                redo.push_back(i);
            }
            else if (foundFirst == false && any == true) {
                cake[i] = cake[i-1];
            }
            else if (foundFirst == true && redo.size() != 0) {
                for (int j = 0; j < static_cast<int>(redo.size()); j++) {
                    cake[redo[j]] = cake[i];
                }
                redo.clear();
            }
            foundFirst = false;
        }

        cout << "Case #" << curCase << ": " << endl;
        for (auto slice : cake) {
            for (auto piece : slice) {
                cout << piece;
            }
            cout << endl;
        }
    }

    return 0;
}