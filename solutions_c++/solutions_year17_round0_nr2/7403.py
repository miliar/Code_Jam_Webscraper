#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(string &s) {
    for (int i = 0; i < s.size() - 1; ++i) {
        if (s[i] > s[i + 1]) {
            return 0;
        }
    }

    return 1;
}

void doTidy(string &s) {
    for (int i = 0; i < s.size() - 1; ++i) {
        if (s[i] > s[i + 1]) {
            s[i]--;

            for (int j = i + 1; j < s.size(); ++j) {
                s[j] = '9';
            }

            break;
        }
    }

    while (s[0] == '0') {
        s = s.substr(1, s.size() - 1);
    }
}

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    int t;
    cin >> t;

    string s;
    for (int k = 1; k <= t; ++k) {
        cin >> s;

        while (!check(s)) {
            doTidy(s);
        }

        cout << "Case #" << k << ": " << s << endl;
    }

    return 0;
}
