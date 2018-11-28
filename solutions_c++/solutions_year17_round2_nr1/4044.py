#include<bits/stdc++.h>
#define FRU freopen("out.txt","w",stdout)
#define FRO freopen("A-small-attempt0.in","r",stdin)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mem(ara,n) memset(ara,n,sizeof ara)
#define loop(i,j,n) for(i=j;i<n;i++)
#define rloop(i,j,n) for(i=n;i>=j;i--)
#define INF 2147483647
#define ll long long
#define pii pair<int,int>
#define eps 1e-9
#define mii map<int,int>
#define vi vector<int>
#define all(n) n.begin(),n.end()
#define inf INF
#define INFLL 10000000000000000LL

//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,0,0,1,0};
//const int col[]={0,-1,1,0,0};
int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}
int lcm(int a,int b)
{
    return ((a*b)/gcd(a,b));
}

/*bool bitcheck(int n,int pos)
{
    return (bool)(n & (1<<pos));
}

int biton(int n,int pos)
{
    return n=n or (1<<pos);
}
int bitoff(int n,int pos)
{
    return n=n & ~(1<<pos);
}*/

using namespace std;

int main()
{
FRO;
FRU;
//std::ios_base::sync_with_stdio(false);
    int c,i,j,k,tc,t;
    double m,a,b;
    pair<double,double>ara[10004];
    int n,cnt=0;
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        scanf("%lf%d",&m,&n);
        for(i=0;i<n;i++)
        {
            scanf("%lf%lf",&a,&b);
            ara[i]=mp(a,b);
        }
        sort(ara,ara+n);
        double tt=0.0;
        a=ara[0].ff,b=ara[0].ss;
        for(i=1;i<n;i++)
        {
            if(ara[i].ss<b)
            {//printf("%f %f %f %f\n",a,b,ara[i].ff,ara[i].ss);
                double x=(ara[i].ff*b)-(a*ara[i].ss);
                x=x/(b-ara[i].ss);
                if(x>m|| abs(x-m)<eps)
                {
                    tt+=(m-a)/b;
                    a=m;
                    goto next;
                }
                tt+=(x-a)/b;
                a=x;
                b=ara[i].ss;
            }
        }
        if(!(abs(a-m)<eps))tt+=(m-a)/b,a=m;
        next:;
        printf("Case #%d: %f\n",t,m/tt);
    }
    return 0;
}
