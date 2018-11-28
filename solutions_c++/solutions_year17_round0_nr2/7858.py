#include <bits/stdc++.h>

using namespace std;

bool good(int start, int digit, string &s) {
    for (int i = start; i < s.size(); i++) {
        if (digit > s[i] - '0') {
            return false;
        }
        if (digit < s[i] - '0') {
            return true;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        string line;
        cout << "Case #" << test << ": ";
        cin >> line;
        if (!good(0, 1, line)) {
            for (int i = 0; i < line.size() - 1; i++) {
                cout << "9";
            }
            cout << endl;
        } else {
            for (int i = 0; i < line.size(); i++) {
                if (good(i, line[i] - '0', line)) {
                    cout << line[i];
                    continue;
                } else {
                    cout << line[i] - '1';
                    for (int j = i + 1; j < line.size(); j++) {
                        cout << 9;
                    }
                    break;
                }
            }
            cout << endl;
        }
    }
    
    return 0;
}