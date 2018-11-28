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
    ll t,p,i,j,r,c1=1,k,n,s=0,max1=0,m,c;

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld",&r,&c);
        memset(val,0,sizeof(val));
        for(i=0;i<r;i++)
        {
            scanf("%s",&a[i]);
        }
        char ch;
        ll x,y,i1,j1;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(a[i][j]!='?' && val[i][j]==0)
                {
                    ch=a[i][j];
                    x=j-1;
                    y=j+1;
                    //printf("i,j : %lld %lld\n",i,j);
                    while(x >=0 && a[i][x]=='?')
                    {
                        x--;
                    }
                    //if(x<0)
                    x++;
                    while(y<c && a[i][y]=='?')
                    {
                        y++;

                    }
                    //if(y==c)
                    y--;
                    for(j1=x;j1<=y;j1++)
                    {
                        a[i][j1]=ch;
                        val[i][j1]=1;
                    }
                   // printf("x,y: %lld %lld\n",x,y);
                    for(i1=i+1;i1<r;i1++)
                    {
                        int flag=1;
                        for(j1=x;j1<=y;j1++)
                        {
                            if( a[i1][j1]!='?')
                            {
                                flag=0;
                                break;
                            }
                        }
                        if(flag==0)
                        break;
                        else
                        {
                            for(j1=x;j1<=y;j1++)
                            {
                                a[i1][j1]=ch;
                                val[i1][j1]=1;
                            }
                        }
                    }
                    for(i1=i-1;i1>=0;i1--)
                    {
                        int flag=1;
                        for(j1=x;j1<=y;j1++)
                        {
                            if( a[i1][j1]!='?')
                            {
                                flag=0;
                                break;
                            }
                        }
                        if(flag==0)
                        break;
                        else
                        {
                            for(j1=x;j1<=y;j1++)
                            {
                                a[i1][j1]=ch;
                                val[i1][j1]=1;
                            }
                        }
                    }
                }
            }
        }

        printf("Case #%lld:\n",c1++);
        for(i=0;i<r;i++)
        printf("%s\n",a[i]);
      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
