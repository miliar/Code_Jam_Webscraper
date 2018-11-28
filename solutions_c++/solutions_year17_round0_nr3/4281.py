#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
priority_queue <int> pq;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cas, C = 1;
    scanf("%d", &cas);
    while(cas--)
    {
        while(!pq.empty())
            pq.pop();
        int n, k, mx, mn;
        scanf("%d %d", &n, &k);
        printf("Case #%d: ", C++);
        pq.push(n);
        for(int i = 0; i < k; i++)
        {
            int tmp = pq.top();
            pq.pop();
            tmp--;
            mn = tmp / 2;
            mx = tmp - mn;
            if(mn != 0)
                pq.push(mn);
            if(mx != 0)
                pq.push(mx);
        }
        printf("%d %d\n", mx, mn);
    }
    return 0;
}
