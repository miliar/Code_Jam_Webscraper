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
ll a[1005],b[1005];

ll mat[1005][1005];
ll val[1005][1005];
ll count1[1005];
int main()
{
    ll t,p,i,j,r,c1=1,k,n,s=0,max1=0,m,c,x1,x2,y1,y2;

    freopen("B-small-attempt1.in","r",stdin);
    freopen("output4.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        ll max1=0,max2=0;
        scanf("%lld%lld%lld",&n,&c,&m);
        memset(mat,-1,sizeof(mat));
        memset(count1,0,sizeof(count1));
        memset(val,0,sizeof(val));
        ll count2=0,count3=0,ans=0,count4=0;

        for(i=0;i<m;i++)
        {
            scanf("%lld%lld",&a[i],&b[i]);
            count1[b[i]]++;
            max1=max(max1,count1[b[i]]);
            j=count1[b[i]];
            while(mat[j][a[i]]!=-1)
            j++;
            max2=max(max2,j);

            val[b[i]][j]=1;
            mat[j][a[i]]=b[i];
        }
        /*for(i=1;i<=m;i++)
        {
            for(j=1;j<=n;j++)
            {
                printf("%lld ",mat[i][j]);
            }
            printf("\n");
        }*/
        ll prom=0;
        //printf("%lld %lld\n",max1,max2);
        for(i=max2;i>max1;i--)
        {
            ll fl=0;
            for(j=1;j<=n;j++)
            {
                if(mat[i][j]!=-1)
                {
                    ll x=mat[i][j];
                    ll flag=0;
                    for(ll i1=1;i1<i;i1++)
                    {
                       // printf("%lld %lld %lld  %lld %lld\n",i,j,i1,x,val[x][i1]);
                        if(val[x][i1]==0)
                        {
                            for(ll j1=1;j1<j;j1++)
                            {
                                if(mat[i1][j1]==-1)
                                {
                                    mat[i1][j1]=x;
                                    val[x][i1]=1;
                                    prom++;
                                    flag=1;
                                    break;
                                }
                            }
                            if(flag==1)
                            break;
                        }
                    }
                    if(flag==0)
                    {
                        fl=1;
                        break;
                    }
                }
            }
            if(fl==1)
            break;

        }
        ans=i;
        /*for(i=1;i<=m;i++)
        {
            for(j=1;j<=n;j++)
            {
                printf("%lld ",mat[i][j]);
            }
            printf("\n");
        }*/

        //if(max2==max1)
       // {
            printf("Case #%lld: ",c1++);
            printf("%lld %lld\n",ans,prom);
        //}

            //scanf("%lld%lld",&x2,&y2);

        /*if(y1==y2)
        {
            printf("Case #%lld: ",c1++);
            printf("2 0\n");
        }
        else
        {
            if(x1==x2)
            {
                if(x1==1)
                {

                    printf("Case #%lld: ",c1++);
                    printf("2 0\n");
                }
                else
                {
                    printf("Case #%lld: ",c1++);
                    printf("1 1\n");

                }
            }
            else
            {
                printf("Case #%lld: ",c1++);
                printf("1 0\n");
            }
        }*/

        //}
        /*for(i=0;i<n;i++)
        {
            a[i]=a[i]%p;
        }


        printf("%lld\n",ans);*/


        //printf("Case #%lld:\n",c1++);
        //for(i=0;i<r;i++)
        //printf("%s\n",a[i]);
      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
