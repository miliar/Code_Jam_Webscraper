#include <bits/stdc++.h>

using namespace std;

int const Max = 1e9+1;

int const N = 1440 * 2 + 5;
int DP[N][N][3];
int a[N], ans;


int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, p, q, u, v;
    cin >> T;
    for(int _=1; _<=T; _++){
        cout << "Case #" << _ << ": ";
        memset(a, 0, sizeof(a));
        ans = Max;
        int n = 1440;
        cin >> p >> q;
        for(int i=1; i<=p; i++){
            cin >> u >> v;
            v--;
            for(int j=u; j<=v; j++)
                a[j] = 1;
            u += n;  v += n;
            for(int j=u; j<=v; j++)
                a[j] = 1;
        }
        for(int i=1; i<=q; i++){
            cin >> u >> v;
            v--;
            for(int j=u; j<=v; j++)
                a[j] = 2;
            u += n;  v += n;
            for(int j=u; j<=v; j++)
                a[j] = 2;
        }

        for(int i=0; i<=2*n; i++){
            for(int j=0; j<=720; j++)
                DP[i][j][1] = DP[i][j][2] = Max;
        }

        DP[0][0][1] = 0;
        for(int i=1; i<=n; i++)
            for(int j=0; j<=720; j++){
                if(a[i] == 1 || a[i] == 0){
                    if(j)   DP[i][j][1] = min(DP[i-1][j-1][1], DP[i-1][j-1][2] + 1);
                    else
                        DP[i][j][1] = DP[i-1][j][2] + 1;
                }
                if(a[i] == 2 || a[i] == 0){
                    DP[i][j][2] = min(DP[i-1][j][2], DP[i-1][j][1] + 1);
                }

            }
        ans = min(ans, DP[n][720][1]);


        for(int i=0; i<=2*n; i++){
            for(int j=0; j<=720; j++)
                DP[i][j][1] = DP[i][j][2] = Max;
        }

        DP[0][0][2] = 0;
        for(int i=1; i<=n; i++)
            for(int j=0; j<=720; j++){
                if(a[i] == 1 || a[i] == 0){
                    if(j)   DP[i][j][1] = min(DP[i-1][j-1][1], DP[i-1][j-1][2] + 1);
                    else
                        DP[i][j][1] = DP[i-1][j][2] + 1;
                }
                if(a[i] == 2 || a[i] == 0){
                    DP[i][j][2] = min(DP[i-1][j][2], DP[i-1][j][1] + 1);
                }
            }

        ans = min(ans, DP[n][720][2]);
        cout << ans << endl;
    }
}
