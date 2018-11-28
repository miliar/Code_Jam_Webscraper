#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
//string a1[200],a2[200];
//string ans1,ans2;
//int b1[100005],b2[100005],n;

int min1=INT_MAX;
typedef pair<int,int> ii;

ll gcd(ll a,ll b)
{
    ll r=1;
    while(a%b!=0)
    {
        r=a%b;
        a=b;
        b=r;
    }
    return b;
}
ll modexp(ll base,ll pow1,ll mod)
{
    ll res=1;
    for(;pow1>0;pow1=pow1>>1)
    {
        if(pow1&1)
        {
            res=(res*base)%mod;
        }
        base=(base*base)%mod;
    }
    return res;
}
char a[105][105];
int val[105][105];
int main()
{
    ll t,i,j,r,c1=1,k,n,s=0,max1=0,m,c,d,d1;

    double p,ans;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld",&d,&n);
        p=0;
        for(i=0;i<n;i++)
        {
            scanf("%lld%lld",&d1,&s);
            p=max(p,(double)(d-d1)/(double)s);
        }
        ans=d/p;


        printf("Case #%lld: ",c1++);
        printf("%lf\n",ans);

      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
