#include <bits/stdc++.h>

using namespace std;

bool used[301];
long long sp[301];
long long e[301];
long long a[301][301];
double d[301][301];
const double eps = 1e-7;

int main(){
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    for (int cur = 0; cur < t; cur++){
        cout << "Case #" << cur + 1 << ": ";
        int n, q;
        cin >> n >> q;
        for (int i = 0; i < n; i++){
            cin >> e[i] >> sp[i];
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cin >> a[i][j];
            }
        }
        for (int k = 0; k < n; k++){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if (a[i][k] != -1 && a[k][j] != -1 && (a[i][j] == -1 || a[i][j] > a[i][k] + a[k][j]))
                        a[i][j] = a[i][k] + a[k][j];
                }
            }
        }
        for (int s = 0; s < n; s++){
            for (int i = 0; i < n; i++){
                d[s][i] = -1;
                used[i] = 0;
            }
            d[s][s] = 0;
            for (int i = 0; i < n; i++){
                int j1 = -1;
                for (int j = 0; j < n; j++){
                    if (!used[j] && d[s][j] > -eps && (j1 == -1 || d[s][j] < d[s][j1] - eps))
                        j1 = j;
                }
                if (j1 == -1) break;
                used[j1] = true;
                for (int j = 0; j < n; j++){
                    if (a[j1][j] != -1 && a[j1][j] <= e[j1] && (d[s][j] < -eps || d[s][j] > d[s][j1] + (a[j1][j] / (double) sp[j1]))){
                        double ad = (a[j1][j] / (double) sp[j1]);
                        d[s][j] = d[s][j1] + ad;
                    }
                }
            }
        }
        cout << fixed << setprecision(20);
        for (int i = 0; i < q; i++){
            int s, t;
            cin >> s >> t;
            s--, t--;
            cout << d[s][t] << " ";
        }
        cout << "\n";
    }
    return 0;
}
