#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; i++)
#define frab(i, a, b) for (int i = a; i < b; i++)

using namespace std;

typedef long long ll;

bool ok(string s) {
    fr(i, (int)s.size() - 1)
        if (s[i] > s[i + 1])
            return false;
    return true;
}

string solveOK(string s) {
    if (ok(s)) return s;
    fr(i, (int)s.size() - 1)
        if (s[i] > s[i + 1]) {
            s[i]--;
            frab(j, i + 1, (int)s.size())
                s[j] = '9';
            if (i == 0 && s[0] == '0')
                s = s.substr(1, (int)s.size() - 1);
            return solveOK(s);
        }

}

int main() {
    //srand(time(NULL));
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    int tests;
    cin >> tests;
    fr(i, tests) {
        string s;
        cin >> s;
        string ans = solveOK(s);
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
