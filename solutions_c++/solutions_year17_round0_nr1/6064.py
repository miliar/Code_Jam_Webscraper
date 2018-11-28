//
// Created by jeraz on 4/8/17.
//

#include <iostream>

using namespace std;

bool validate(string s) {
    for (char c : s) {
        if (c != '+') return false;
    }
    return true;
}

char flip(char c) {
    if (c == '+') return '-';
    return '+';
}

int greedyFlip(string &s, int flipSize) {
    int count = 0;
    for (int i = 0; i <= s.size() - flipSize; i++) {
        if (s[i] == '-') {
            count++;
            for (int j = i; j < i + flipSize; j++) {
                s[j] = flip(s[j]);
            }
        }
    }
    return count;
}

int main() {
    int t;
    cin >> t;

    for (unsigned i = 0; i < t; i++) {
        string temp;
        int fSize;
        cin >> temp >> fSize;
        int c = greedyFlip(temp, fSize);
        if (validate(temp)) {
            cout << "Case #" << i + 1 << ": " << c << endl;
        } else {
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
    }
}