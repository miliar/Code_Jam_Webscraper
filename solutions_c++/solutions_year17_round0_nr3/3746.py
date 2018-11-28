#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdio>
#include <queue>
using namespace std;
#define maxn 1005
char s[maxn];

priority_queue<int>q;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        while(!q.empty()) q.pop();
        int n,k;
        scanf("%d%d",&n,&k);
        q.push(n);
        for(int i=0;i<k;i++)
        {
            int now=q.top();
            q.pop();
            int x=now/2;
            q.push(x);
            if(now%2) q.push(x);
            else q.push(x-1);

            if(i==k-1)
            {
                now--;
                int L=now/2;
                int R=now-now/2;
                printf("Case #%d: %d %d\n",cas,max(L,R),min(L,R));
            }
        }
    }
}
