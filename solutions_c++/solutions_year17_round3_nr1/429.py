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
struct x
{
    double r,h;
};
 x a[100005];
 bool cmp(x p,x q)
 {
     if(p.r>q.r)
     {
         return 1;
     }
     else
     {
         if(p.r==q.r)
         {
             return p.h>q.h;
         }
         else
         return 0;
     }
 }
 ll n,K;
 ll dp[1005][1005];
 double func(ll i,ll k)
 {

     if(k==K)
     {
         return 0;
     }
     if(i==n)
     {
         return INT_MIN;
     }
     if(dp[i][k]!=-1)
     {
         return dp[i][k];
     }
     if(n-i==K-k)
     {
         if(k==0)
         {
             dp[i][k]= 2*a[i].r*a[i].h+a[i].r*a[i].r + func(i+1,k+1);
         }
         else
         {
              dp[i][k]=2*a[i].r*a[i].h + func(i+1,k+1);
         }
         return dp[i][k];
     }
     if(k==0)
     {
         dp[i][k]= max(2*a[i].r*a[i].h+a[i].r*a[i].r + func(i+1,k+1),func(i+1,k));
         return dp[i][k];
     }
     else
     {
         dp[i][k]=max(2*a[i].r*a[i].h + func(i+1,k+1),func(i+1,k));
         return dp[i][k];

     }
 }
int main()
{
    ll t,p,i,j,r,c1=1,s=0,max1=0,m,c;

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld",&n,&K);
        double ans=0;
        for(i=0;i<n;i++)
        {
            scanf("%lf%lf",&a[i].r,&a[i].h);
        }
        sort(a,a+n,cmp);
        memset(dp,-1,sizeof(dp));
        /*for(i=0;i<n;i++)
        {
            printf("%lf %lf\n",a[i].r,a[i].h);
        }*/

        /*for(i=0;i<k;i++)
        {
            ans+=2*M_PI*a[i].r*a[i].h;
        }
        ans+=M_PI*a[0].r*a[0].r;*/

        ans=M_PI*func(0,0);



        printf("Case #%lld: ",c1++);
        printf("%lf\n",ans);

      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
