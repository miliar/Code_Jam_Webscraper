#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

const int maxn = 101;
const long long INF = 1E18;

int solve() {
    int n, q;
    cin >> n >> q;

    int speed[maxn], maxD[maxn];
    for (int i = 0; i < n; i++)
        cin >> maxD[i] >> speed[i];

    long long a[maxn][maxn];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
            if (a[i][j] == -1)
                a[i][j] = INF;
            if (i == j)
                a[i][j] = 0;
        }

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = min(a[i][j], a[i][k] + a[k][j]);

    while(q--) {
        double dist[maxn];
        bool used[maxn];
        for (int i = 0; i < n; i++)
            dist[i] = INF, used[i] = false;

        int start, finish;
        cin >> start >> finish;
        start--, finish--;
        dist[start] = 0;

        while(true) {
            int mn;
            double minD = INF + 1;
            for (int i = 0; i < n; i++)
                if (!used[i] && dist[i] < minD) {
                    minD = dist[i];
                    mn = i;
                }
            used[mn] = true;

            if (mn == finish)
                break;

            for (int i = 0; i < n; i++)
                if (a[mn][i] <= maxD[mn])
                    dist[i] = min(dist[i], dist[mn] + 1.0 * a[mn][i] / speed[mn]);
        }

        cout << fixed << setprecision(10);
        cout << dist[finish] << ' ';
    }
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
