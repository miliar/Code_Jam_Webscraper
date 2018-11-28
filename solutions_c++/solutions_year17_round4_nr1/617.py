#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

int N, P;
int f[10], ff[10];

int tps[6][3] =
{
    4, 0, 0,
    2, 1, 0,
    1, 0, 1,
    0, 2, 0,
    0, 1, 2,
    0, 0, 4
};

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

        scanf("%d%d", &N, &P);
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= N; i++)
        {
            int x;
            scanf("%d", &x);
            f[x % P]++;
        }

        if(P == 2)
        {
            int ans = f[0] + f[1] / 2;
            if(f[1] & 1)    ans++;
            printf("%d\n", ans);
        }
        else if(P == 3)
        {
            int ans = f[0];
            int mn = min(f[1], f[2]);
            ans += mn;
            ans += (f[1] - mn) / 3 + (f[2] - mn) / 3;
            if( (f[1] - mn) % 3 != 0 || (f[2] - mn) % 3 != 0 )  ans++;
            printf("%d\n", ans);
        }
        else if(P == 4)
        {
            vector <int> prm;
            for(int i = 0; i < 6; i++)  prm.push_back(i);
            for(int i = 0; i < 4; i++)  ff[i] = f[i];
            int ans = 0;
            do
            {
                for(int i = 0; i < 4; i++)  f[i] = ff[i];

                int cnt = 0;
                for(int i = 0; i < 6; i++)
                {
                    int id = prm[i];
                    while(f[1] >= tps[id][0] && f[2] >= tps[id][1] && f[3] >= tps[id][2])
                    {
                        cnt++;
                        f[1] -= tps[id][0];
                        f[2] -= tps[id][1];
                        f[3] -= tps[id][2];
                    }
                }
                int ok = 0;
                for(int i = 1; i <= 3; i++)
                    if(f[i])
                        ok = 1;
                cnt += ok;
                ans = max(ans, cnt);

            }while(next_permutation(prm.begin(), prm.end()));
            ans += ff[0];
            printf("%d\n", ans);
        }
    }

    return 0;
}
