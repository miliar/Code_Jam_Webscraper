#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

int N, K;
char state[1005];
int v[1005];

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d\n", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        scanf("%s %d\n", state, &K);
        N = strlen(state);
        for(int i = 0; i < N; i++)
        {
            if(state[i] == '-') v[i] = 0;
            else    v[i] = 1;
        }

        int ans = 0;
        for(int i = 0; i < N - K + 1; i++)
            if(!v[i])
            {
                ans++;
                for(int j = 0; j < K; j++)
                    v[i + j] ^= 1;
            }

        int ok = 1;
        for(int i = 0; i < N; i++)
            if(!v[i])
                ok = 0;

        if(!ok)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }

    return 0;
}
