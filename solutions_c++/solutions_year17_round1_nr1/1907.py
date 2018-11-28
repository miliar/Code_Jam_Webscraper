#include <iostream>
#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b) {
    int t;
    while (b != 0) {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

inline void imp(int i) { cout << "Case #" << i << ": IMPOSSIBLE" << endl; }

int main() {
    int t, X, Y;
    string S;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    vector<int> pancakes;
    for (int i = 1; i <= t; ++i) {
        cin >> X >> Y;
        vector<vector<char>> solution(X, vector<char>(Y, '?'));
        for (int c = 0; c < X; ++c) {
            cin >> S;
            for (int d = 0; d < Y; ++d) {
                if (S[d] == '?') {
                    if (d > 0) {
                        if (solution[c][d - 1] != '?') {
                            solution[c][d] = solution[c][d - 1];

                        }
                    }
                } else {
                    solution[c][d] = S[d];
                }
            }
            for (int e = Y - 2; e >= 0; --e) {
                if (solution[c][e] == '?')
                    solution[c][e] = solution[c][e + 1];
            }
        }
        for (int c = 1; c < X; ++c) {
            if (solution[c][0] == '?') {
                for (int d = 0; d < Y; ++d) {
                    solution[c][d] = solution[c - 1][d];
                }
            }
        }
        for (int c = X - 1; c >= 0; --c) {
            if (solution[c][0] == '?') {
                for (int d = 0; d < Y; ++d) {
                    solution[c][d] = solution[c + 1][d];
                }
            }
        }

        cout << "Case #" << i << ": " << endl;
        for (int c = 0; c < X; ++c) {
            for (int d = 0; d < Y; ++d) {
                cout << solution[c][d];
            }
            cout << endl;
        }

    }
}