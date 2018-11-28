#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

const string IMPOSSIBLE = "IMPOSSIBLE";

const int N = 101;

int d[N][N];

double d2[N][N];

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        int n, q;
        scanf("%d%d", &n, &q);
        printf("Case #%d: ", CT);
        
        vector<int> s(n);
        vector<int> e(n);
        
        for (int i = 0; i < n; i ++)
            scanf("%d%d", &e[i], &s[i]);
        
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < n; j ++)
                scanf("%d", &d[i][j]);
        
        
        for (int i = 0; i < n; i ++) {
//            cout << "From " << i << endl;
            vector<bool> fl(n, false);
            for (int j = 0; j < n; j ++)
                d2[i][j] = 1e25;
            
            d2[i][i] = 0;
            
            
            for (int k = 0; k < n; k ++) {
                int mini = -1;
                double minv = 1e20;
                for (int j = 0; j < n; j ++) {
                    if (!fl[j] && (minv > d2[i][j])) {
                        mini = j;
                        minv = d2[i][j];
                    }
                }
                
//                cout << "min: " << minv << " at " << mini << endl;
                
                if (mini == -1)
                    break;
                
                fl[mini] = true;
                for (int j = 0; j < n; j ++)
                    if (!fl[j] && d[mini][j] != -1) {
                        if (d2[i][mini] + d[mini][j] <= e[i] + 0.5) {
                            d2[i][j] = min(d2[i][j], d2[i][mini] + d[mini][j]);
                        }
                    }
            }
            
            for (int j = 0; j < n; j ++) {
                if (fl[j])
                    d2[i][j] = d2[i][j] / s[i];
                else
                    d2[i][j] = -1;
            }
        }
        
//        cout << d2[1][0] << endl;
        
        for (int k = 0; k < n; k ++)
            for (int i = 0; i < n; i ++)
                for (int j = 0; j < n; j ++) {
                    if (d2[i][k] > -0.1 && d2[k][j] > -0.1) {
//                        if (i == 2 && j == 0)
//                            cout << k << endl;
                        if (d2[i][j] < -0.1)
                            d2[i][j] = d2[i][k] + d2[k][j];
                        else
                            d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);
                    }
                }
        
        for (int i = 0; i < q; i ++) {
            int u, v;
            scanf("%d%d", &u, &v);
            printf("%lf%s", d2[u - 1][v - 1], (i == q - 1) ? "\n" : " ");
        }
    }
    
    
    return 0;
}
