#include <bits/stdc++.h>
using namespace std;

void flip(string &s, int i, int j) {
    for (int k = i; k <= j; k++) {
        if (s[k]=='+') s[k] = '-';
        else s[k] = '+';
    }
}
int main() {
    int t, k;
    string s;
    cin >> t;
    int tc = 1;
    while (t--) {
        cin >> s >> k;
        int patties = 0;
        int flips = 0;
        int first = -1;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '+' && patties == 0) {
                continue;
            } else {
                if (s.size() - k <= i && patties == 0) break;
                if (first == -1 && s[i] == '+') {
                    first = i;
                }
                patties += 1;
                if (patties == k) {
                    flip(s, i-k+1, i);
                    patties = 0;
                    flips++;
                    if (first != -1) {
                        i = first-1;
                        first = -1;
                    }
                }
            }
        }
        bool possible = true;
        int prev = s[s.size() - k];
        for (int i = s.size() - k + 1; i < s.size(); i++) {
            if (prev != s[i]) {
                possible = false;
                break;
            }
        }
        if (prev == '-') flips++;
        if (possible) {
            cout << "Case #" << tc << ": " << flips << endl;
        } else {
            cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
        }
        tc++;
    }
}