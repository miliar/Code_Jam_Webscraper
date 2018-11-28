#include <bits/stdc++.h>

using namespace std;

bool isAscending(const string& s) {
    char cur = 0;
    for (int i = 0; i < s.size(); i++) {
        if (cur > s[i]) return false;
        cur = s[i];
    }
    return true;
}

int t;
string n;
int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n;
        cout << "Case #" << test << ": ";
        if (isAscending(n)) {
            cout << n << endl;
            continue;
        }
        for (int i = n.size() - 1; i >= 0; i--) {
            string tmp = n;
            if (n[i] == '0') continue;
            tmp[i] = tmp[i] - 1;
            for (int j = i + 1; j < tmp.size(); j++) {
                tmp[j] = '9';
            }
            // cout << tmp << endl;
            if (isAscending(tmp)) {
                if (tmp[0] == '0') tmp = tmp.substr(1);
                cout << tmp << endl;
                break;
            }
        }
    }
}