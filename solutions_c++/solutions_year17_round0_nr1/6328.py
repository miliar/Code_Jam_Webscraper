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
    int t, K;
    string S;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    int unhappy_p, happy_p, tmp, flipps;
    vector<int> pancakes;
    bool solution;
    for (int i = 1; i <= t; ++i) {
        pancakes.clear();
        cin >> S >> K;
        unhappy_p = 0;
        happy_p = 0;
        flipps = 0;
        for (int c = 0; c < S.length(); ++c) {
            if (S[c] == '-') {
                pancakes.push_back(0);
            } else {
                pancakes.push_back(1);
            }
        }
        for (int j = 0; j < pancakes.size() - K + 1; ++j) {
            if (pancakes[j]==0) {
                for (int s = 0; s < K; ++s)
                    pancakes[j + s] = 1 - pancakes[j + s];
                ++flipps;
            }
        }
        solution = true;
        for (int s = 0; s < K; ++s) {
            if (pancakes[pancakes.size() - s -1] == 0) {
                solution = false;
                break;
            }
        }
        if (solution) {
            cout << "Case #" << i << ": " <<flipps << endl;
        } else {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        }

    }
}