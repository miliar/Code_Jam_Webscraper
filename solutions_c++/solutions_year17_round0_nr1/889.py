#include <cstdio>
#include <cstring>
using namespace std;

char s[1002];
int N;
int K;
int T;
int ans;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z)
    {
        scanf("%s%d", s, &K);
        N = strlen(s);
        ans = 0;
        for (int i = 0; i <= N - K; ++i)
        {
            if (s[i] == '+')
                continue;
            for (int j = 0; j < K; ++j)
                s[i + j] ^= 6;
            ans += 1;
        }
        for (int i = N - K + 1; i < N; ++i)
        {
            if (s[i] == '-')
            {
                ans = -1;
                break;
            }
        }
        printf("Case #%d: ", z);
        if (ans >= 0)
            printf("%d\n", ans);
        else
            printf("IMPOSSIBLE\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
