#include <cstdio>
#include <cstring>

#define MAXLEN 1000

void solve()
{
    char S[MAXLEN];
    unsigned int K;
    scanf("%s%d", S, &K);

    auto const l = strlen(S);
    bool f[l - K] = {};
    int flips = 0, old = 0;

    for(size_t i = 0; i < l; i++)
    {
        if(i >= K) old ^= f[i - K];
        if((flips & 1) ^ old ^ (S[i] == '-'))
        {
            if(i > l - K)
            {
                printf("IMPOSSIBLE");
                return;
            }
            else
            {
                f[i] = 1;
                flips++;
            }
        }
    }

    printf("%d", flips);
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}
