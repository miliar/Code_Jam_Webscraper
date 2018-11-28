#include <bits/stdc++.h>

using namespace std;

int main () {
    int tt; 
    cin >> tt;
    for (int cases = 1; cases <= tt; ++cases) {
        cout << "Case #" << cases << ": ";
        int n, q; 
        cin >> n >> q;
        double hd[n], hv[n];
        for (int i = 0; i < n; ++i)
            cin >> hd[i] >> hv[i];
        double d [n][n];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                cin >> d[i][j];
                if (d[i][j] < 0)
                    d[i][j] = 0x707070707070L;
            }

        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    if (d[i][j] > d[i][k] + d[k][j])
                        d[i][j] = d[i][k] + d[k][j];

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (d[i][j] > 0 && d[i][j] <= hd[i] + 0.0000000001)
                    d[i][j] /= hv[i];
                else
                    d[i][j] = 0x707070707070L;
        
        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    if (d[i][j] > d[i][k] + d[k][j])
                        d[i][j] = d[i][k] + d[k][j];
        
        for (int trips = 0; trips < q; ++trips) {
            if (trips)
                cout << " ";
            int s, f;
            cin >> s >> f;
            cout << fixed << setprecision(9) << d[s-1][f-1];
        }
        cout << "\n";
    }
}
