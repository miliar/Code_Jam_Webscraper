#include <cstdio>
#include <cstring>

const int maxn = 1111;

char S[maxn];

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        printf("Case #%d: ", kase);
        int K;
        scanf("%s %d", S, &K);
        int N = strlen(S);
        int ans = 0;
        for (int i = 0; i <= N - K; ++i)
            if (S[i] == '-')
            {
                ++ans;
                for (int j = 0; j < K; ++j)
                    S[i + j] = '+' + '-' - S[i + j];
            }
        for (int i = 0; i < N; ++i)
            if (S[i] == '-')
                ans = -1;
        if (ans == -1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
    return 0;
}