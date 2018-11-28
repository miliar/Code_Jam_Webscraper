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
int a[1005];
int main()
{
    ll t,p,i,j,r,c=1,k,n,s=0,max1=0,m;

    freopen("B-large (1).in","r",stdin);
    freopen("output1.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld",&n);
        //printf("%s %lld\n",a,k);
        for(i=0;i<25;i++)
        {
            a[i]=n%10;
            n=n/10;
        }
        for(int x=0;x<25;x++)
        {
            int flag=0;
            for(i=20;i>=1;i--)
            {
                if(a[i-1]<a[i])
                {
                    a[i]--;
                    a[i-1]=9;
                    flag=1;
                    break;
                }

            }
            if(flag==1)
            {

                for(j=i-1;j>=0;j--)
                {
                    a[j]=9;
                }
            }
        }


        printf("Case #%lld: ",c++);
        for(i=20;i>=0;i--)
        {
            if(a[i]!=0)
            break;
        }
        for(j=i;j>=0;j--)
        {
            printf("%d",a[j]);
        }
        printf("\n");
      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
