#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int main() {
    int T;
    cin >> T;
    forn(t, T) {
        string s;
        int k;
        cin >> s >> k;
        int res = 0;
        forn(i, s.size()) if(s[i] == '-' and i + k <= s.size()) {
            forn(j, k) s[i + j] = (s[i + j] == '-')? '+': '-';
            res ++;
        }
        forn(i, s.size()) if(s[i] == '-') res = -1;
        if(res < 0) {
            cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << t + 1 << ": " << res << endl;
        }
    }
}
