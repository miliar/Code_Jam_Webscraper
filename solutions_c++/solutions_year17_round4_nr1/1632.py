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
ll a[105];
int val[105][105];
int main()
{
    ll t,p,i,j,r,c1=1,k,n,s=0,max1=0,m,c;

    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld",&n,&p);
        ll count1=0,count2=0,count3=0,ans=0;

        for(i=0;i<n;i++)
        {
            scanf("%lld",&a[i]);

        }
        for(i=0;i<n;i++)
        {
            a[i]=a[i]%p;
        }
        sort(a,a+n);
        count1=0;
        if(p==2)
        {
            for(i=0;i<n;i++)
            {
                if(a[i]==0)
                count1++;
                else
                count2++;
            }
            ans=count1+(count2+1)/2;
        }
        else
        {
            for(i=0;i<n;i++)
            {
                if(a[i]==0)
                count1++;
                else
                if(a[i]==1)
                count2++;
                else
                count3++;

            }
            ans=count1;
            ll x=min(count2,count3);
            count2-=x;
            count3-=x;
            ans+=x;


            ans+=count2/3+count3/3;
            count2-=(count2/3)*3;
            count3-=(count3/3)*3;

            if(count2>0 || count3>0)
            ans+=1;




        }
        printf("Case #%lld: ",c1++);
            printf("%lld\n",ans);


        //printf("Case #%lld:\n",c1++);
        //for(i=0;i<r;i++)
        //printf("%s\n",a[i]);
      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
