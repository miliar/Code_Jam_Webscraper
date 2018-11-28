#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
LL lo[105],ro[105],p[105],lj[105],rj[105],sum[105];
int n,k;

struct node
{
    int l,r,id;
    bool operator < (const node &a) const
    {
        int p1 = min(l,r);
        int p2 = min(a.l,a.r);
        if(p1 != p2) return p1 < p2;
        p1 = max(l,r);
        p2 = max(a.l,a.r);
        if(p1 != p2) return p1 < p2;
    }
};

int main()
{
    int T;
    freopen("C-small-2-attempt1.txt","r",stdin);
    freopen("C2059.txt","w",stdout);
    scanf("%d",&T);
    for(int kase = 1;kase <= T;kase++)
    {
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",kase);
        if(n == k) {puts("0 0");continue;}
        priority_queue<node> q;
        node u;
        if(n%2) u.l = n/2,u.r = n / 2;
        else u.l = n/2 - 1,u.r = n/2;
        q.push(u);
        for(int i = 1;i <= k;i++)
        {
            node v = q.top();q.pop();
            if(i == k)
            {
                int y = max(v.l,v.r);
                int z = min(v.l,v.r);
                printf("%d %d\n",y,z);
            }
            else
            {
                int x = max(v.l,v.r);
                int xx = min(v.l,v.r);
                if(x%2) u.l = x/2,u.r = x / 2;
                else u.l = max(x/2 - 1,0),u.r = x/2;
                q.push(u);

                //printf("i = %d u.l = %d u.r = %d\n",i,u.l,u.r);

                if(xx%2) u.l = xx/2,u.r = xx / 2;
                else u.l = max(xx/2 - 1,0),u.r = xx/2;
                q.push(u);

               // printf("i = %d u.l = %d u.r = %d\n",i,u.l,u.r);

            }
        }

    }
    return 0;
}

