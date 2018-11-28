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
    ll val,ind;
};
x a[3];
bool cmp(x p,x q)
{
    return p.val<q.val;
}
int main()
{
    ll t,i,j,r,c1=1,k,n,s=0,max1=0,m,c,d,d1,o,y,g,b,v;

    double p,ans;
    freopen("B-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%lld%lld%lld%lld%lld%lld%lld",&n,&r,&o,&y,&g,&b,&v);

        printf("Case #%lld: ",c1++);

        if(o>b)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        else
        {
            if(o==b && o>0 )
            {
                if(r!=0 || y!=0 || g!=0 || v!=0)
                {
                    printf("IMPOSSIBLE\n");
                    continue;
                }
                else
                {
                    for(i=0;i<n;i++)
                    {
                        if(i%2==0)
                        {
                            printf("O");
                        }
                        else
                        {
                            printf("B");
                        }
                    }
                    printf("\n");
                    continue;
                }
            }
            b=b-o;
        }

        if(g>r)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        else
        {
            if(g==r && g>0)
            {
                if(o!=0 || y!=0 || b!=0 || v!=0)
                {
                    printf("IMPOSSIBLE\n");
                    continue;
                }
                else
                {
                    for(i=0;i<n;i++)
                    {
                        if(i%2==0)
                        {
                            printf("G");
                        }
                        else
                        {
                            printf("R");
                        }
                    }
                    printf("\n");
                    continue;
                }
            }
            r=r-g;

        }
       // printf("HEY\n");
        if(v>y)
        {
          //  printf("%lld\n",y);
            printf("IMPOSSIBLE\n");
            continue;
        }
        else
        {
            if(v==y && v>0)
            {
                if(r!=0 || o!=0 || g!=0 || b!=0)
                {
                    printf("IMPOSSIBLE\n");
                    continue;
                }
                else
                {
                    for(i=0;i<n;i++)
                    {
                        if(i%2==0)
                        {
                            printf("V");
                        }
                        else
                        {
                            printf("Y");
                        }
                    }
                    printf("\n");
                    continue;
                }
            }
            y=y-v;
        }
        a[0].val=r;
        a[0].ind=1;
        a[1].val=y;
        a[1].ind=2;
        a[2].val=b;
        a[2].ind=3;


        //printf("%lld %lld %lld\n",a[0],a[1],a[2]);

        sort(a,a+3,cmp);

       ll max1=a[2].ind;
       ll min1=a[0].ind;
       ll mid1=a[1].ind;


     //   printf("%lld %lld %lld\n",min1,mid1,max1);


        if(a[0].val+a[1].val<a[2].val)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        else
        {
            while(n>0)
            {
                if(min1==1 && r>0)
                {
                    printf("R");
                    n--;
                    while(g>0)
                    {
                        printf("GR");
                        n=n-2;
                        g--;
                    }
                    r--;
                    a[0].val--;
                }
                if(min1==2 && y>0)
                {
                    printf("Y");
                    n--;
                    while(v>0)
                    {
                        printf("VY");
                        n=n-2;
                        v--;
                    }
                    y--;
                    a[0].val--;
                }
                if(min1==3 && b>0)
                {
                    printf("B");
                    n--;
                    while(o>0)
                    {
                        printf("OB");
                        n=n-2;
                        o--;
                    }
                    b--;
                    a[0].val--;
                }

                while(a[1].val-a[0].val>0)
                {
                    if(max1==1)
                    {
                        printf("R");
                        n--;
                        while(g>0)
                        {
                            printf("GR");
                            n=n-2;
                            g--;
                        }
                        r--;

                    }
                    if(max1==2)
                    {
                        printf("Y");
                        n--;
                        while(v>0)
                        {
                            printf("VY");
                            n=n-2;
                            v--;
                        }
                        y--;
                    }
                    if(max1==3)
                    {
                        printf("B");
                        n--;
                        while(o>0)
                        {
                            printf("OB");
                            n=n-2;
                            o--;
                        }
                        b--;
                    }
                    a[2].val--;
                    if(mid1==1)
                    {
                        printf("R");
                        n--;
                        while(g>0)
                        {
                            printf("GR");
                            n=n-2;
                            g--;
                        }
                        r--;
                    }
                    if(mid1==2)
                    {
                        printf("Y");
                        n--;
                        while(v>0)
                        {
                            printf("VY");
                            n=n-2;
                            v--;
                        }
                        y--;
                    }
                    if(mid1==3)
                    {
                        printf("B");
                        n--;
                        while(o>0)
                        {
                            printf("OB");
                            n=n-2;
                            o--;
                        }
                        b--;
                    }
                    a[1].val--;


                }
                if(a[2].val>a[1].val)
                {
                    if(max1==1)
                    {
                        printf("R");
                        n--;


                    }
                    if(max1==2)
                    {
                        printf("Y");
                        n--;

                    }
                    if(max1==3)
                    {
                        printf("B");
                        n--;

                    }
                    a[2].val--;
                }




            }
            printf("\n");
        }




    }
    return 0;
}
