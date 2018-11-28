#include <bits/stdc++.h>

using namespace std;

const int MAX_T = 1440;

pair <int, int> a[10], b[10];

int main() {
    ifstream cin ("B-small-attempt3.in");
    //ifstream cin ("schedule.in");
    ofstream cout ("schedule.out");
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin >> test;
    for (int t = 1; t <= test; t++) {
        cout << "Case #" << t << ": ";

        int m, n;
        cin >> m >> n;
        for (int i = 1; i <= m; i++) cin >> a[i].first >> a[i].second;
        for (int i = 1; i <= n; i++) cin >> b[i].first >> b[i].second;
        if (m > 0) sort(a + 1, a + m + 1);
        if (n > 0) sort(b + 1, b + n + 1);

        if (m + n <= 1) cout << "2\n";
        else {
            if (n == 0) {
                int total = min(a[2].second - a[1].first, MAX_T - a[2].first + a[1].second);
                if (2 * total <= MAX_T) cout << "2\n";
                else cout << "4\n";
            } else if (m == 0) {
                int total = min(b[2].second - b[1].first, MAX_T - b[2].first + b[1].second);
                if (2 * total <= MAX_T) cout << "2\n";
                else cout << "4\n";
            } else {
                cout << "2\n";
            }
        }
    }
}
