#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void solve() {
    string s;
    cin >> s;
    int k;
    cin >> k;
    int ans = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        if (i + k - 1 >= (int)s.size()) {
            break;
        }
        if (s[i] == '-') {
            ++ans;
            for (int j = i; j < i + k; j++) {
                if (s[j] == '-') s[j] = '+'; else s[j] = '-';
            }
        }
    }
    bool fail = false;
    for (int i = 0; i < (int)s.size(); i++) {
        if (s[i] == '-') {
            fail = true;
        }
    }
    if (fail) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans << endl;
    }
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}