#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
//string a1[200],a2[200];
//string ans1,ans2;
//int b1[100005],b2[100005],n;

int min1=INT_MAX;


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
ll ans1=0,ans2=0,k;
void func(ll n,ll x)
{
    if(n==0)
    {
        return ;
    }
    else
    {

        ll mid=(n+1)/2;
        ll m1=mid-1;
        ll m2=n-mid;
        if(x==k)
        {
            ans1=max(m1,m2);
            ans2=min(m1,m2);
            return ;
        }
        if(m1>=m2)
        {
            func(m1,2*x);
            func(m2,2*x+1);
        }
        else
        {
            func(m2,2*x);
            func(m1,2*x+1);
        }

    }
}
typedef pair<ll,ll> ii;
ll func1(ll n)
{
   // priority_queue<pair<ll,ll> > pq;
   map<ll,ll> mp;
   priority_queue<ll> pq;

   // pq.push(ii(n,1));
   pq.push(n);
   mp[n]=1;
    ll count1=0;
    while(!pq.empty())
    {
        ll p=pq.top();
       // ll q=pq.top().second;
       // printf("%lld \n",p);
        ll mid=(p+1)/2;
        pq.pop();
        count1+=mp[p];

        //ll mid=(n+1)/2;
        ll m1=mid-1;
        ll m2=p-mid;
        if(count1>=k)
        {
            ans1=max(m1,m2);
            ans2=min(m1,m2);
            break;
        }
        if(m1==m2)
        {
            if(mp.find(m1)==mp.end())
            {
                pq.push(m1);
            }
            mp[m1]+=2*mp[p];
        }
        else
        {

            if(m1>0)
            {
                if(mp.find(m1)==mp.end())
                {
                    pq.push(m1);
                }
                mp[m1]+=mp[p];
            }
            if(m2>0)
            {
                if(mp.find(m2)==mp.end())
                {
                    pq.push(m2);
                }
                mp[m2]+=mp[p];
            }
        }

    }
}
int main()
{
    ll t,p,i,j,r,c=1,n,s=0,max1=0,m;

   freopen("C-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld",&n,&k);

        func1(n);
        //a[0]=1;
        //a[n+1]=1;
        /*for(i=0;i<k;i++)
        {
            for(j=1;j<=n;j++)
            {

                for(j1=j-1;j1>=0;j1--)
                {
                    if(a[j1]==1)
                    break;
                }
                for(j2=j+1;j2<=n+1;j2++)
                {
                    if(a[j2]==1)
                    break;
                }
                b[j]=min(j-j1-1,j2-j-1);
                c[j]=max(j-j1-1,j2-j-1);

            }
        }*/

        printf("Case #%lld: ",c++);
        printf("%lld %lld\n",ans1,ans2);
      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
