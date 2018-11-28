#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("B.inp", "r", stdin);
    freopen("B.out", "w", stdout);
    const string Color = "ROYGBV";
    typedef pair<int, char> IC;

    int TC; cin >> TC;
    for (int testID = 1; testID <= TC; ++testID) {
        printf("Case #%d: ", testID);
        int n; IC a[6]; cin >> n;
        for (int i = 0; i < 6; ++i) cin >> a[i].first, a[i].second = Color[i];
        sort(a, a + 6, greater<IC>());
        if (a[0].first > a[1].first + a[2].first) {
            puts("IMPOSSIBLE");
            continue;
        }

        string S[2000];
        for (int i = 0; i < a[1].first; ++i) S[i] += a[1].second;
        for (int i = 0; i < a[2].first; ++i) S[(i + a[1].first) % a[0].first] += a[2].second;

        for (int i = 0; i < a[0].first; ++i) cout << a[0].second << S[i];
        cout << endl;
    }
    return 0;
}
