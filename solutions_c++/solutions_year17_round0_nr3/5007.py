#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int i,l,r,x,n,k,a,b;
    int t,z;
    priority_queue<long long int> q;
    scanf("%d",&t);
    for(z=1;z<=t;z++)
    {
        scanf("%lld%lld",&n,&k);
        x=n;
        for(i=0;i<k;i++)
        {
           x--;
           l=x/2;
           r=x-l;
           q.push(r);
           q.push(l);
           a=max(l,r);
           b=min(l,r);
           x=q.top();
           q.pop();
        }
        while(!q.empty())
            q.pop();

        printf("Case #%d: %lld %lld\n",z,a,b);
    }
    return 0;
    }
