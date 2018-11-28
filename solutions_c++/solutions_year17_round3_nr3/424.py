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



double a[1005];
int main()
{
    ll t,p,i,j,r,c1=1,max1=0,m,c,b,x,y,n;
    double u,k;

    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("output3.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lf",&n,&k);
        scanf("%lf",&u);
        double x=0;
        for(i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
            x+=a[i];
            a[i]=-a[i];
            //x+=a[i];
        }
        double ans=1;
        sort(a,a+n);
        for(i=0;i<n;i++)
        {
            a[i]=-a[i];
        }
        x+=u;
        for(i=0;i<n;i++)
        {
            if(a[i]<=x/k)
            break;
            x-=a[i];
            k--;
        }
        for(;i<n;i++)
        {
            a[i]=x/k;
        }
        ans=1;
        for(i=0;i<n;i++)
        {
            ans*=a[i];
        }

        printf("Case #%lld: ",c1++);
        printf("%lf\n",ans);

      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
