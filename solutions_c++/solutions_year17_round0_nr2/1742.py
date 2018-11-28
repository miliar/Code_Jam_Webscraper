#include<cstring>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
int a[30];
ll work(ll n)
{
    int len=0;
    while(n)
    {
        a[++len]=n%10;
        n/=10;
    }

    for(int i=len;i>1;i--)
    {
        if(a[i]>a[i-1])
        {
            a[i]--;
            int j;
            for(j=i;j<len;j++)
                if(a[j+1]>a[j])
                {
                    a[j+1]--;
                }
                else break;
            for(--j;j>=1;--j)
                a[j]=9;
            break;
        }
    }
    ll ans=0;
    for(int i=len;i>=1;i--)
        ans=ans*10+a[i];
    return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        ll n;
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",cas,work(n));
    }
}
