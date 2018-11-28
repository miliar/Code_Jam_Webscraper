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
 ll w[1445];
 ll dp[1445][725][2];
 ll s[10005];
 ll start;
 ll func(ll i,ll val,ll p)
 {
     if(dp[i][val][p]!=-1)
     return dp[i][val][p];
     //printf("%lld %lld %lld\n",i,val,p);
     if(i==1440)
     {
         if(val!=720)
         {
             return 5000;
         }
         if(p!=start)
         {
             return 1;
         }
         else
         {
             return 0;
         }
     }
     if(val>720)
     {
         return 50000;
     }
     if(i-val>720)
     {
         return 50000;
     }


    if(s[i]==0)
    {
        if(p==0)
        dp[i][val][p]= func(w[i],val+w[i]-i,p);
        else
        dp[i][val][p]= 1+func(w[i],val+w[i]-i,1-p);
        return dp[i][val][p];
    }
    if(s[i]==1)
    {
        if(p==0)
        dp[i][val][p]= 1+func(w[i],val,1-p);
        else
        dp[i][val][p]= func(w[i],val,p);
        return dp[i][val][p];
    }
    if(p==0)
    {

        dp[i][val][p]= min(func(i+1,val+1,p),1+func(i+1,val,1-p));
        return dp[i][val][p];
    }
    else
    {
        dp[i][val][p]= min(func(i+1,val,p),1+func(i+1,val+1,1-p));
        return dp[i][val][p];
    }

 }

int main()
{
    ll t,p,i,j,r,c1=1,max1=0,m,c,a,b,x,y;

    freopen("B-large (1).in","r",stdin);
    freopen("output2.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld",&a,&b);
        memset(s,-1,sizeof(s));
        for(i=0;i<a;i++)
        {

            scanf("%lld%lld",&x,&y);
            for(j=x;j<y;j++)
            {
                s[j]=1;
                w[j]=y;
            }
        }
        for(i=0;i<b;i++)
        {
            scanf("%lld%lld",&x,&y);
            for(j=x;j<y;j++)
            {
                s[j]=0;
                w[j]=y;

            }
        }
        start=0;
        memset(dp,-1,sizeof(dp));
        ll ans=func(0,0,0);
        start=1;
        memset(dp,-1,sizeof(dp));
         ans=min(func(0,0,1),ans);



        /*for(i=0;i<n;i++)
        {
            printf("%lf %lf\n",a[i].r,a[i].h);
        }*/

        /*for(i=0;i<k;i++)
        {
            ans+=2*M_PI*a[i].r*a[i].h;
        }
        ans+=M_PI*a[0].r*a[0].r;*/





        printf("Case #%lld: ",c1++);
        printf("%lld\n",ans);

      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
