#include <bits/stdc++.h>

using namespace std;
using ll = long long;
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define REP(i, n)    FOR(i, 0, n - 1)

int T;
string s;

string trim(string s) {
    string r = "";
    int n = s.length();
    int pos = -1;

    REP(i, n) {
        if (s[i] != '0') {
            pos = i;
            break;
        }
    }

    FOR(i, pos, n - 1) {
        r += s[i];
    }
    return r;
}


string comp(string s) {
    s = "0" + s;

    int n = s.length();
    int pos = -1;

    REP(i, n - 1) {
        if (s[i] > s[i + 1]) {
            pos = i;
            break;
        }
    }
    if (pos < 0) {
        return trim(s);
    }

    while (pos > 0) {
        if (s[pos] - 1 >= s[pos - 1]) {
            s[pos]--;
            FOR(i, pos + 1, n - 1) {
                s[i] = '9';
            }
            break;
        } else {
            pos--;
        }
    }
    return trim(s);
}


int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> T;
    REP(t, T) {
        cout << "Case #" << t + 1 << ": ";
        cin >> s;

        cout << comp(s) << "\n";
    }

    fclose(stdout);
}
// 99 999 999 999 999 999
// 99 999 999 999 999 999
//111 111 111 111 111 110