#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("c-small.in","r",stdin);
    freopen("c-small.out","w",stdout);

    int t;
    cin >> t;
    for (int c = 0; c < t; c++) {
        int n, q;
        cin >> n >> q;
        vector<vector<int> > horse(n,vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> horse[i][0] >> horse[i][1];
        }
        vector<int> dist(n);
        dist[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int d;
                cin >> d;
                if (d != -1) {
                    dist[i+1] = dist[i] + d;
                }
            }
        }
        int u, v;
        cin >> u >> v;
        vector<double> time(n,-1);
        time[n-1] = 0;
        for (int i = n-2; i >= 0; i--) {
            int d = horse[i][0];
            int s = horse[i][1];
            for (int j = i+1; j < n; j++) {
                int dij = dist[j] - dist[i];
                if (dij > d)
                    break;
                if (time[j] == -1)
                    continue;
                double t1 = (double) dij / s + time[j];
                if (time[i] == -1 || t1 < time[i])
                    time[i] = t1;
            }
        }

        cout << "Case #" << c+1 << ": " << fixed << setprecision(6) << time[0] << "\n";
    }
}
