#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 1e3 + 10;

int N, C, M;
int cnt[maxn];
int sum[maxn];

bool check(int num)
{
    int rem = 0;
    for (int i = 1; i <= N; ++i)
    {
        rem += num;
        rem -= sum[i];
        if (rem < 0)
            return false;
    }
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d %d %d", &N, &C, &M);
        for (int i = 1; i <= C; ++i)
            cnt[i] = 0;
        for (int i = 1; i <= N; ++i)
            sum[i] = 0;
        for (int i = 0; i < M; ++i)
        {
            int P, B;
            scanf("%d %d", &P, &B);
            ++cnt[B];
            ++sum[P];
        }
        int L = 0, R = M;
        for (int i = 1; i <= C; ++i)
            L = max(L, cnt[i]);
        while (L < R)
        {
            int M = (L + R) >> 1;
            if (check(M))
                R = M;
            else
                L = M + 1;
        }
        int ans = 0;
        for (int i = N; i >= 1; --i)
            if (sum[i] > L)
                ans += sum[i] - L;
        static int kase = 1;
        printf("Case #%d: %d %d\n", kase++, L, ans);
    }
    return 0;
}