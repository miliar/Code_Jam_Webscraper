#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    long long n,k,l,r;
    scanf("%d",&t);
    int t1=0;
    while(t--)
    {
        scanf("%lld%lld",&n,&k);
        priority_queue<long long> pq;
        pq.push(n);
        t1++;
        while(k--)
        {
            n=pq.top();
            if(n==1)
            {
                l=0;
                r=0;
                break;
            }
            pq.pop();
            if(n%2==0)
            {
                l=n/2;
                r=n/2-1;
                if(l)
                    pq.push(l);
                if(r)
                    pq.push(r);
            }
            else
            {
                l=n/2;
                r=n/2;
                if(l)
                    pq.push(l);
                if(r)
                    pq.push(r);
            }
        }
        printf("Case #%d: %lld %lld\n",t1,l,r);
    }
    return 0;
}

