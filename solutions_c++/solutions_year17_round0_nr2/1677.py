#include <bits/stdc++.h>
using namespace std;

#define sz(x) (int(x.size()))

string S;

bool is_tidy(const string& s) {
    for (int i = 1; i < sz(s); i++) {
        if (s[i] < s[i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int TC;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        cin >> S;
        cout << "Case #" << tc << ": ";

        if (is_tidy(S)) {
            cout << S << endl;
            continue;
        }

        int t = 1;
        while (t < sz(S) && S[t] >= S[t - 1]) {
            t++;
        }
        while (t >= 2 && S[t - 2] == S[t - 1]) {
            t--;
        }

        string pref = S.substr(0, t);
        string suff = string(sz(S) - sz(pref), '9');

        pref.back()--;
        if (pref == "0") {
            pref = "";
        }

        cout << pref << suff << endl;
    }

    return 0;
}
