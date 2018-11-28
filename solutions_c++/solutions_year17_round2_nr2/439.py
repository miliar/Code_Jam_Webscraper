#include <bits/stdc++.h>
#define foru(i, a, b) for (int i = a; i <= b; i++)
using namespace std;
int n, r, o, y, g, b, v;
pair<int, char> a[3];
char s[1005];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TC;
    scanf("%d", &TC);

    foru(TT, 1, TC) {
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        a[0] = make_pair(r, 'R');
        a[1] = make_pair(y, 'Y');
        a[2] = make_pair(b, 'B');
        sort(a, a + 3, greater<pair<int, char> >());

        if (a[0].first > n / 2) {
            cout << "Case #" << TT << ": " << "IMPOSSIBLE" << endl;
            continue;
        }

        foru(i, 0, a[0].first - 1) s[2 * i] = a[0].second;
        int x = 1; bool stop = false;
        foru(i, 2 * a[0].first - 1, n - 1) {
            s[i] = a[x].second; --a[x].first;
            if (a[x].first < 0) {
                stop = true;
                cout << "Case #" << TT << ": " << "IMPOSSIBLE" << endl;
                break;
            }
            x ^= 3;
        }
        if (stop) continue;
        foru(i, 0, a[1].first - 1) s[2 * i + 1] = a[1].second;
        foru(i, 0, a[2].first - 1) s[2 * (i + a[1].first) + 1] = a[2].second;
        s[n] = '\0';
        cout << "Case #" << TT << ": " << s << endl;
    }

}
