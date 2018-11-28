#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool allHappy(vector<bool> pancakes) {
    for (int i = 0; i < pancakes.size(); i++) {
        if (!pancakes[i])
            return false;
    }
    return true;
}

int flipper(vector<bool> pancakes, int K, int start) {
    if (allHappy(pancakes))
        return 0;

    int best = -1;

    for (int i = start; i <= pancakes.size() - K; i++) {
        // Flip
        for (int j = 0; j < K; j++) {
            pancakes[i + j] = !pancakes[i + j];
        }
        int res = flipper(pancakes, K, i + 1);
        if (res > -1 && (best == -1 || res + 1 < best))
            best = res + 1;
        // Unflip for next.
        for (int j = 0; j < K; j++) {
            pancakes[i + j] = !pancakes[i + j];
        }
    }

    return best;
}

int flipFast(vector<bool> pancakes, int K) {
    int flips = 0;
    for (int i = 0; i <= pancakes.size() - K; i ++) {
        if (!pancakes[i]) {
            flips++;
            for (int j = 0; j < K; j++) {
                pancakes[i + j] = !pancakes[i + j];
            }
        }
    }
    for (int i = pancakes.size() - K + 1; i < pancakes.size(); i++) {
        if (!pancakes[i])
            return -1;
    }
    return flips;
}

vector<bool> parseS(string S) {
    vector<bool> r;
    for (char c : S) {
        if (c == '+') {
            r.push_back(true);
        } else {
            r.push_back(false);
        }
    }
    return r;
}

int main() {
    /*
    vector<bool> t;
    for (int i = 0; i < 50; i++) {
        t.push_back(true);
        t.push_back(false);
    }
    cout << flipFast(t, 30) << endl;
    
    exit(0);
    */

    int tests, K;
    string S;
    cin >> tests;
    for (int i = 0 ; i < tests; i++) {
        cin >> S >> K;
        int res = flipFast(parseS(S), K);
        if (res == -1) {
            cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << (i + 1) << ": " <<  res << endl;
        }
    }
}