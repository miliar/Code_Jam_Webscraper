#include <bits/stdc++.h>
using namespace std;
#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define dforsn(i, s, n) for (int i = n - 1; i >= s; i--)
#define dforn(i, n) dforsn(i, 0, n)
#define pb push_back
#define fst first
#define snd second
#define tint long long
#define uint unsigned tint
#define debug(v) cerr << #v << " = " << v << '\n';

int main() {
    tint t;

    cin >> t;

    forn(tt,t) {
        cout << "Case #" << tt+1 << ": ";

        string s;

        cin >> s;

        char last = s[0];
        int lastInc = 0;

        if(s.length() == 1) {
            cout << s << endl;
            continue;
        }

        forsn(i, 1, s.length()) {
            if(s[i] > last) {
                last = s[i];
                lastInc = i;
                continue;
            } else if(s[i] < last) {
                if(last == '1') {
                    s = string(s.size()-1, '9');
                    break;
                }

                s[lastInc]--;
                forsn(j,lastInc+1,s.length()) {
                    s[j] = '9';
                }
            }
        }

        cout << s << endl;
    }

    return 0;
}
