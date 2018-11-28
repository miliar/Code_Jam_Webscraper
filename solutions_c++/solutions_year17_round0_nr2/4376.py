#include <bits/stdc++.h>

using namespace std;

#define gcj cout << "Case #" << Test << ": "

pair<string, int> solve(string s) {
        if (s.length() == 1) {
            return {s, 0};
        } else {
            int ind = 0;
            bool bad = true;
            for (int i = 1; i < s.length(); ++i) {
                if (s[i - 1] > s[i]) {
                    ind = i - 1;
                    bad = false;
                    break;
                }
            }
            if (bad) {
                return {s, 0};
            }
            for (int i = ind + 1; i < s.length(); ++i) {
                s[i] = '9';
            }
            int jj = ind;
            while (jj > -1) {
                --s[jj];
                if (jj == 0) {
                    break;
                } else {
                    if (s[jj] >= s[jj - 1]) {
                        break;
                    }
                }
                --jj;
            }
            while (jj + 1 <= ind) {
                s[jj + 1] = '9';
                ++jj;
            }
            if (s[0] == '0') {
                int sz = s.length() - 1;
                s = "";
                for (int i = 0; i < sz; ++i) {
                    s += '9';
                }
            }
            return {s, ind};    
        }
    }

bool sorted(string s) {
    for (int i = 1; i < s.length(); ++i) {
        if (s[i] < s[i - 1]) {
            return false;
        }
    }
    return true;
}

int to_int(string s) {
    int r = 0;
    for (int i = 0; i < s.length(); ++i) {
        r *= 10;
        r += s[i] - '0';
    }
    return r;
}

string stupid(string s) {
    int k = to_int(s);
    string z = s;
    while (!sorted(z)) {
        --k;
        z = to_string(k);
    }
    return z;
}

int main() {
    
    int tests;
    cin >> tests;
    for (int Test = 1; Test <= tests; ++Test) {
        string s;
        cin >> s;
        gcj;
        cout << solve(s).first << '\n';
    }
}