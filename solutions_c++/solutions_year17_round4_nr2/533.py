#include <iostream>
#include <fstream>

using namespace std;

int n, c, m;
int place[2000], owner[2000];
int ticks[2000];
int places[2000];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n >> c >> m;
        int l = 0, r = 2000;
        for (int i = 0; i < c; ++i)
            ticks[i] = 0;
        for (int i = 0; i < m; ++i) {
            cin >> place[i] >> owner[i];
            --place[i];
            --owner[i];
            ++ticks[owner[i]];
            l = max(l, ticks[owner[i]]);
        }
        while (l < r) {
            int cen = (l + r) / 2;
            for (int i = 0; i < n; ++i)
                places[i] = 0;
            for (int i = 0; i < m; ++i)
                places[place[i]]++;
            for (int i = n - 1; i > 0; --i) {
                places[i - 1] += max(0, places[i] - cen);
            }
            if (places[0] > cen) l = cen + 1;
            else r = cen;
        }
        for (int i = 0; i < n; ++i)
            places[i] = 0;
        for (int i = 0; i < m; ++i)
            places[place[i]]++;
        int ans = 0;
        for (int i = n - 1; i > 0; --i) {
            ans += max(0, places[i] - l);
        }
        cout << "Case #" << t << ": " << l << ' ' << ans << "\n";
    }

    return 0;
}