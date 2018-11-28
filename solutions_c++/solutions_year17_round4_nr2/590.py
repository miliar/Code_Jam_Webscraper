#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

int f[2][1005];
int sz[2];

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);

        int N, C, M;
        scanf("%d%d%d", &N, &C, &M);
        memset(f[0], 0, sizeof(f[0]));
        memset(f[1], 0, sizeof(f[1]));
        sz[0] = sz[1] = 0;
        for(int i = 1; i <= M; i++)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            swap(x, y);
            x--;
            f[x][y]++;
            sz[x]++;
        }

        if(sz[0] < sz[1]) { swap(sz[0], sz[1]); for(int i = 1; i <= N; i++) swap(f[0][i], f[1][i]); }

        int cnt = 0;
        int prm = 0;
        for(int i = 1; i <= N; i++)
            while(f[0][i])
            {
                f[0][i]--;
                cnt++;

                int id = 0;
                for(int j = 1; j <= N; j++)
                    if(j != i && f[1][j] > 0 && (f[0][j] > f[0][id] || (f[0][j] == f[0][id] && f[1][j] > f[1][id])))
                        id = j;
                if(id == 0)
                {
                    if(i == 1)  continue;
                    if(f[1][i])
                    {
                        f[1][i]--;
                        prm++;
                    }
                }
                else if(f[1][id] > 0)
                    f[1][id]--;
            }
        for(int i = 1; i <= N; i++)
            while(f[1][i] > 0)
            {
                f[1][i]--;
                cnt++;
            }

        printf("%d %d\n", cnt, prm);
    }

    return 0;
}
