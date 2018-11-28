//
// Created by Andrei Zakharevich on 07.04.17.
//

#include <iostream>
#include <map>
#include <set>

using namespace std;

map<string, int> m;
set<string> in_progress;


string flip(string s, int start, int k) {
    string res = s;
    for (int i = start; i < start + k; i++)
        if (res[i] == '+')
            res[i] = '-';
        else
            res[i] = '+';
    return res;
}


int calc(string s, int k) {
    if (m.find(s) != m.end())
        return m[s];
    bool ok = true;
    for (int i = 0; i < s.length(); i++)
        if (s[i] == '-') {
            ok = false;
            break;
        }
    if (ok) {
        return 0;
    }
    int res = 999999999;
    for (int i = 0; i < s.length() - k + 1; i++) {
        string key = flip(s, i, k);
        if (in_progress.find(key) == in_progress.end()) {
            in_progress.insert(key);
            int value = calc(key, k);
            in_progress.erase(key);
            res = min(res, value + 1);
        }
    }
    m[s] = res;
    return res;
}


int main() {
    int T;
    cin >> T;
    for (int j = 1; j <= T; j++) {
        m.clear();

        string s;
        int k;
        cin >> s >> k;
        int res = calc(s, k);
        if (res == 999999999)
            cout << "Case #" << j << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << j << ": " << res << endl;
    }
    return 0;
}