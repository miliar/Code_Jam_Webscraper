#include<cstdio>
#include<queue>
#include<map>
using namespace std;

long long mx(long long a,long long b)
{
    if(a > b)return a;
    return b;
}
long long mn(long long a,long long b)
{
    if(a < b)return a;
    return b;
}
main()
{
    int n;
    scanf("%d",&n);
    for(int t=0;t<n;t++)
    {
        long long k,p;
        scanf("%lld %lld",&k,&p);
        priority_queue<long long> q;
        map<long long,long long> m;
        q.push(k);
        m[k]=1;
        long long l,r;
        while(p>0)
        {
            long long tmp = q.top();
            q.pop();
            //printf("%d\n",tmp);
            p-=m[tmp];
            if(tmp%2 == 0)l = (tmp/2)-1;
            else l = tmp/2;
            r = tmp-l-1;
            if(r<0)r = 0;
            if(m[r] == 0)q.push(r);
            m[r]+=m[tmp];
            if(m[l] == 0)q.push(l);
            m[l]+=m[tmp];
        }
        printf("Case #%d: ",t+1);
        printf("%lld %lld\n",mx(l,r),mn(l,r));
    }
}
