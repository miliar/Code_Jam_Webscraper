#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,sv,rem,pq;
    long long int n,ans,i,add1;
    scanf("%d",&t);
    sv=t;

    while(t--)
    {
        scanf("%lld",&n);
        ans=n;
        i=10;
        add1=9;
        rem=n%10;
        n/=10;
        //ans=n;
        while(n)
        {
            pq=n%10;
            if(pq>rem)
            {
                n-=1;
                n*=i;
                n+=add1;
                ans=n;
                n/=i;
            }
            if(i<=100000000000000000)
            i*=10;
            if(add1<=99999999999999999)
            add1=(add1*10)+9;
            rem=n%10;
            //n=ans;
            n/=10;
        }

        printf("Case #%d: %lld\n",sv-t,ans);
    }

    return 0;
}
