#include <stdio.h>
#include <map>
std::map<long long, long long> M;
std::map<long long, long long>::iterator it;
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, t;
    long long N, K;
    long long l, f;
    scanf("%d", &T);
    for (t = 1; t <= T; t++)
    {
        M.clear();
        scanf("%I64d %I64d", &N, &K);
        M.insert(std::make_pair(N, 1LL));
        while (1)
        {
            it = M.end();
            it--;
            l = it->first;
            f = it->second;
            if (K - f <= 0)
            {
                printf("Case #%d: %I64d %I64d\n", t, (l - 1) - (l - 1)/2, (l - 1)/2);
                break;
            }
            M.erase(it);
            M[(l - 1)/2] += f;
            M[(l - 1) - (l - 1)/2] += f;
            K -= f;
        }
    }
}
