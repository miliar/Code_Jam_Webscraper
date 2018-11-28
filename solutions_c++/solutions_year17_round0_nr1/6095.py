#include <bits/stdc++.h>

using namespace std;

const int MAX = 1e3 + 7;
char pancake [MAX];

int main () {
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    int t;
    cin >> t;

    for (int kase = 1; kase <= t; kase++) {
        int k;
        cin >> pancake >> k;
        int len = strlen (pancake);
        int cnt = 0;
        for (int i = 0; i < len && i + k - 1 < len; i++) {
            if (pancake [i] == '-') {
                for (int j = i; j < i + k; j++) {
                    if (pancake [j] == '-') pancake [j] = '+';
                    else pancake [j] = '-';
                }
                cnt++;
            }
        }
        bool possible = true;
        for (int i = 0; i < len; i++) {
            if (pancake [i] == '-') {
                possible = false;
                break;
            }
        }

        if (possible) printf ("Case #%d: %d\n", kase, cnt);
        else printf ("Case #%d: IMPOSSIBLE\n", kase);
    }

    return 0;
}
