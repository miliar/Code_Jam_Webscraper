#include <cstdio>
#include <cstring>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++)
    {
        char S[1005];
        int K;
        scanf("%s%d", S, &K);
        int ans = 0;
        for (int i = 0; S[i+K-1]; i++)
        {
            if (S[i] == '-')
            {
                ans++;
                for (int j = 0; j < K; j++)
                    S[i+j] ^= '+' ^ '-';
            }
        }
        bool good = true;
        for (int i = 0; S[i]; i++)
            if (S[i] != '+')
                good = false;
        printf("Case #%d: ", tt);
        if (good)
            printf("%d\n", ans);
        else
            puts("IMPOSSIBLE");
    }
}
