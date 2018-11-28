#include <bits/stdc++.h>
#define int long long

using namespace std;

int const N = 105;
int const MAX = 1e13+1;

int DP[N][N],n, q, E[N], V[N];
double T[N][N];

 main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int Test, x, y;
    cin >> Test;
    for(int _=1; _<=Test; _++){
        cout << "Case #" << _ << ": ";
        cin >> n >> q;

        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++)
                DP[i][j] = T[i][j] = MAX;
            T[i][i] = 0;
        }

        for(int i=1; i<=n; i++){
            cin >> E[i] >> V[i];
        }
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                cin >> DP[i][j];
                if(DP[i][j] == -1)  DP[i][j] = MAX;
            }
        }

        for(int i=1; i<=n; i++)
            for(int u=1; u<=n; u++)
                for(int v=1; v<=n; v++)
                    DP[u][v] = min(DP[u][v], DP[u][i] + DP[i][v]);
        for(int step=1; step<=100; step++)
        for(int i=1; i<=n; i++)
            for(int u=1; u<=n; u++)
                for(int v=1; v<=n; v++)
                    if(E[i] >= DP[i][v])
                        T[u][v] = min(T[u][v], T[u][i] + 1.0 * DP[i][v] / V[i]);

        for(int i=1; i<=q; i++){
            cin >> x >> y;
            printf("%0.9f ", T[x][y]);
        }
        cout << endl;
    }
}
