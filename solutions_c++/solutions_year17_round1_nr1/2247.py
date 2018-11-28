#include <iostream>

using namespace std;

void printResult(int nr, int result) {
    cout << "Case #" << nr << ": " << result << "\n";
}

void printResult(int nr, string result) {
    cout << "Case #" << nr << ": " << result << "\n";
}

void printResult(long long nr, pair<long long, long long> result) {
    cout << "Case #" << nr << ": " << result.first << " " << result.second << "\n";
}

void printResult(int nr, char tab[][26], int r, int c) {
    cout << "Case #" << nr << ":\n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << tab[i][j];
        }
        cout << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    int r, c;
    char cake[26][26];

    for (int h = 1; h <= t; h++) {
        cin >> r >> c;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> cake[i][j];
            }
        }

      //  printResult(h, cake, r, c);

        char initial = '?';
        int lastIndex = 0;

        for (int i = 0; i < r; i++) {
            initial = '?';
            lastIndex = 0;
            for (int j = 0; j < c; j++) {
                if (cake[i][j] != '?') {
                    initial = cake[i][j];
                    for (int k = 0; k < j; k++) {
                        cake[i][k] = initial;
                    }
                    lastIndex = j + 1;
                    break;
                }
            }
            for (int j = lastIndex; j < c; j++) {
                if (cake[i][j] == '?') {
                    cake[i][j] = initial;
                }
                else {
                    initial = cake[i][j];
                }
            }
        }

      //  printResult(h, cake, r, c);

        for (int i = 0; i < c; i++) {
            initial = '?';
            lastIndex = 0;
            for (int j = 0; j < r; j++) {
                if (cake[j][i] != '?') {
                    initial = cake[j][i];
                    for (int k = 0; k < j; k++) {
                        cake[k][i] = initial;
                    }
                    lastIndex = j + 1;
                    break;
                }
            }
            for (int j = lastIndex; j < r; j++) {
                if (cake[j][i] == '?') {
                    cake[j][i] = initial;
                }
                else {
                    initial = cake[j][i];
                }
            }
        }

        printResult(h, cake, r, c);
    }

    return 0;
}