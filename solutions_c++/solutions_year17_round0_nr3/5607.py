#include <bits/stdc++.h>
#define VMAX 1000010

using namespace std;

bool v[VMAX];
int n, k;

int right(int k) {
    int nr, i;
    for (i = k + 1, nr = 0; ; i++, nr++)
        if (v[i])
            return nr;
}

int left(int k) {
    int nr, i;
    for (i = k - 1, nr = 0; ; i--, nr++)
        if (v[i])
            return nr;
}

void solve() {

    int Left, Right, i, j, jMin, Min, Max;

    memset(v, false, sizeof(v));
    v[0] = v[n + 1] = true;

    for (i = 1; i <= k; i++) {
        Min = Max = -618618618;
        for (j = 1; j <= n; j++)
            if (!v[j]) {
                Left = left(j);
                Right = right(j);
                if (min(Left, Right) > Min) {
                    Min = min(Left, Right);
                    Max = max(Left, Right);
                    jMin = j;
                }
                else
                    if (min(Left, Right) == Min && max(Left, Right) > Max) {
                        Max = max(Left, Right);
                        jMin = j;
                    }
                    else
                        if (min(Left, Right) == Min && max(Left, Right) == Max)
                            jMin = j;
            }
        v[jMin] = true;
    }

    cout << Max << ' ' << Min << '\n';

}

int main() {

    int t, i;

    cin >> t;
    for (i = 1; i <= t; i++) {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;

}
