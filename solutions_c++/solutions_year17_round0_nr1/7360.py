#include <vector>
#include <iostream>
#include <string>
#include <cassert>
using namespace std;

string s;
int n;

void flip(int l) {
    for (int i = l; i < l + n; ++i) {
        if (s[i] == '-') {
            s[i] = '+';
        } else {
            s[i] = '-';
        }
    }
}

int main() {
    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cin >> s >> n;
        assert(n <= s.size());
        
        int ans = 0;
        for (int i = 0; i <= s.size() - n; ++i) {
            if (s[i] == '-') {
                flip(i);
                ++ans;
            }
        }

        cout << "Case #" << T + 1 << ": ";
        bool ok = true;
        for (int i = 0; i < s.size(); ++i) {
            ok = ok && (s[i] == '+');
        }
        if (ok) {
            cout << ans;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << "\n";
    }
}
