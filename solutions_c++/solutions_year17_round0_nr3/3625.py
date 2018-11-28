#include <cstdio>
#include <queue>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
const LL mod = 1e9 + 7;
const int N = 1e6 + 5;
struct P
{
    int L, R, len;
    bool operator <(const P &p)const
    {
        if (len < p.len)
            return true;
        if (len == p.len)
            return p.L < L;
        return false;
    }
};
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, ca = 1, n, k, mid;
    scanf("%d", &T);
    while(T--)
    {
        priority_queue<P> Q;
        scanf("%d%d", &n, &k);
        P p, q, r;
        p.L = 1;
        p.R = n;
        p.len = n;
        Q.push(p);
        int ansL = 0, ansR = 0;
        for(int i = 1; i <= k; i++)
        {
            p = Q.top();
            Q.pop();
            mid = (p.L + p.R) >> 1;
            if (i == k)
            {
                ansL = mid - p.L;
                ansR = p.R - mid;
                break;
            }

            q.L = p.L;
            q.R = mid - 1;
            q.len = q.R - q.L + 1;
            if (q.len > 0)
            {
                Q.push(q);
            }

            r.L = mid + 1;
            r.R = p.R;
            r.len = r.R - r.L + 1;
            if (r.len > 0)
            {
                Q.push(r);
            }
        }
        printf("Case #%d: %d %d\n", ca++, max(ansL, ansR), min(ansL, ansR));
    }
    return 0;
}
