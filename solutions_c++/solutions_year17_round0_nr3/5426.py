#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<queue>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
typedef long long LL;
using namespace std;

void divide(LL n, LL &a, LL &b)
{
    a = n / 2;
    if (a == 0)
        b = 0;
    else
        b = (n & 1) ? a : a - 1;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("data.txt", "r", stdin);
    freopen("out.txt","w",stdout);
#endif

    int cases, num;
    LL n, k, m, a, b, ta, tb;
    char path[20];
    scanf("%d\n", &cases);
    for (int c = 1; c <= cases; c++)
    {
        printf("Case #%d: ", c);
        scanf("%lld %lld", &n, &k);
        
        priority_queue<LL> pq;
        pq.push(n);
        while (k-- > 0)
        {
            n = pq.top();
            pq.pop();
            divide(n, a, b);
            pq.push(a);
            pq.push(b);
        }

        printf("%lld %lld\n", a, b);
    }
    return 0;

}
