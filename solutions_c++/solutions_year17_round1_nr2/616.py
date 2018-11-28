#include<bits/stdc++.h>
using namespace std;
#define eps (double)1e-5
int n,m;
double rat[55];
priority_queue<double> p[55];
int check(int x)
{
    int i;
    double val;
    for(i=0;i<n;i++)
    {
        val = rat[i]*x;
        while(!p[i].empty())
        {
            if(-p[i].top()*10<val*9)
            {
//                printf("pop %lf\n",-p[i].top());
                p[i].pop();
            }
            else break;
        }
        if(p[i].empty()) return 0;
        else if(-p[i].top()*10>val*11) return 0;
    }
    for(i=0;i<n;i++)
    {
//        printf("pop %lf\n",-p[i].top());
        p[i].pop();
    }
    return 1;
}
main()
{
    int T,cnum=1;
    int i,j,t,ans;
    double x;
    freopen("B-large.in","r",stdin);
    freopen("B_out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        cerr << cnum << endl;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++) scanf("%lf",&rat[i]);
        for(i=0;i<n;i++) while(!p[i].empty()) p[i].pop();
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%lf",&x);
                p[i].push(-x);
            }
        }
        ans = 0;
        for(i=1;i<=1000000;i++)
        {
            while(1)
            {
                t = check(i);
                ans += t;
                if(!t) break;
            }
        }
        printf("Case #%d: %d\n",cnum++,ans);
    }
}
