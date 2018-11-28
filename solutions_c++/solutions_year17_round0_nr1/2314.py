#include <bits/stdc++.h>
using namespace std;
#define forsn(i, s, n) for (uint i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define dforsn(i, s, n) for (uint i = n - 1; i >= s; i--)
#define dforn(i, n) dforsn(i, 0, n)
#define pb push_back
#define fst first
#define snd second
#define tint long long
#define uint unsigned tint
#define debug(v) cerr << #v << " = " << v << '\n';

int main() {
    uint t;

    cin >> t;

    forn(tt,t) {
        cout << "Case #" << tt+1 << ": ";

        string s;
        uint k;

        cin >> s >> k;

        bool error = false;
        tint res = 0;

        /*
        int flipped = 0;
        queue<uint> flip;

        forn(i, s.length()) {
            if(flip.size() and flip.front() == i) {
                flip.pop();
                flipped ^= 1;
            }

            int v = s[i] == '+' ? 1 : 0;
            v += flipped;
            v %= 2;

            if(v == 0) {
                if(i <= s.length()-k) {
                    res++;
                    flipped ^= 1;
                    flip.push(i+k);
                } else {
                    error = true;
                    break;
                }
            }
        }*/

        forn(i, s.length()) {
            if(s[i] == '-') {
                if(i > s.length()-k) {
                    error = true;
                    break;
                }

                forn(j,k) {
                    s[i+j] = s[i+j] == '+' ? '-' : '+';
                }

                res++;
            }
        }

        if(error)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << res << endl;
    }

    return 0;
}
