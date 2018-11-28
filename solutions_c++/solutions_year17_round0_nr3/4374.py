#include <cstdio>
#include <map>

using namespace std;

map<long long,int> q;

long long mid;

long long solve(long long l)
{
    if(l<=0) return 0;
    if(l<mid) return 0;
    if(q.count(l)) return q[l];
    if(l%2==1)
    {
        long long a=l/2;
        return 2*solve(a)+1;
    }
    else
    {
        long long a=l/2-1,b=l/2;
        return 1+solve(a)+solve(b);
    }
}

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t;
    long long n,k,a,b;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%lld%lld",&n,&k);
        long long st=0,dr=n;
        while(st<=dr)
        {
            q.clear();
            mid=(st+dr)/2;
            long long nr=solve(n);
            if(nr>=k) st=mid+1;
            else dr=mid-1;
        }
        printf("Case #%d: ",test);
        if(dr%2==1) {a=dr/2;b=dr/2;}
        else {a=dr/2-1;b=dr/2;}
        printf("%lld %lld\n",b,a);
    }
    return 0;
}
