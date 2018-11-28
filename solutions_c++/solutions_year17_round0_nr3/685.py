#include <cstdio>

using namespace std;

const int MAGIC = 1e6;

long long L[MAGIC];
long long cnt[MAGIC];

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        long long N, K;
        scanf("%lld %lld", &N, &K);
        printf("Case #%d: ", kase);
        L[0] = N;
        cnt[0] = 1;
        int head = 0, tail = 1;
        long long ans = -1;
        while (head < tail)
        {
            long long sum = 0;
            int pos = head;
            while (pos < tail && L[pos] == L[head])
                sum += cnt[pos++];
            K -= sum;
            if (K <= 0)
            {
                ans = L[head];
                break;
            }
            L[tail] = L[head] / 2;
            cnt[tail] = sum;
            ++tail;
            L[tail] = (L[head] - 1) / 2;
            cnt[tail] = sum;
            ++tail;
            head = pos;
        }
        printf("%lld %lld\n", ans / 2, (ans - 1) / 2);
    }
    return 0;
}