#include <bits/stdc++.h>
#define SMAX 1010

using namespace std;

int lg, k;
char s[SMAX];

void solve() {

    int steps, i, j;
    bool Minus;

    for (steps = 0; steps <= k * lg; steps++) {
        Minus = false;
        for (i = 0; i <= lg - k; i++)
            if (s[i] == '-') {
                Minus = true;
                for (j = i; j <= i + k - 1; j++)
                    if (s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                break;
            }
        for (i = 0; i < lg; i++)
            if (s[i] == '-')
                Minus = true;
        if (!Minus) {
            cout << steps << '\n';
            return;
        }
    }

    cout << "IMPOSSIBLE\n";

}

int main() {

    int t, i;

    cin >> t;
    for (i = 1; i <= t; i++) {
        cin >> s >> k;
        lg = strlen(s);
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
