#include<bits/stdc++.h>
using namespace std;

int main()
{
   freopen("toiletout.out","w",stdout);
   //freopen("toiletin.in","r",stdin);
    long long n,a,b,i,j,k,l,tc,t,p,h;
    cin>>tc;
    t=0;
    while(tc--)
    {
        t++;
        cin>>n>>k;
        priority_queue<long long>pq;
        a=n/2;
        b=n-a;
        if(b>a)
            b--;
        else a--;
        k--;
        pq.push(a);
        pq.push(b);
        while(k--)
        {
            l=pq.top();
            pq.pop();
            if(l==0)
            {
                a=0;
                b=0;
                break;
            }
            a=l/2;
            b=l-a-1;
            pq.push(a);
        pq.push(b);

        }
        p=max(a,b);
        h=min(a,b);
       printf("Case #%lld: %lld %lld\n",t,p,h);
    }
    return 0;
}
