#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>
using namespace std;

#define LL long long int
#define uLL unsigned long long int

#define S(a) scanf("%d",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SLL(a) scanf("%lld",&a)
#define SLL2(a,b) scanf("%lld%lld",&a,&b)
#define SLL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define SC(a) scanf("%c",&a)
#define P(a) printf("%d",a)
#define PS(a) printf("%s",a)
#define PLL(a) printf("%lld",a)
#define PCASE(kk) printf("Case %d: ",kk++)
#define PCASENL(kk) printf("Case %d:\n",kk++)
#define NL puts("")

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define pi (2.0*acos(0.0))
#define pii pair<int,int>

template <class T> inline T BMOD(T p,T e,T m)
{
    T ret=1;
    while(e)
    {
        if(e&1) ret=(ret*p)%m;
        p=(p*p)%m;
        e>>=1;
    }
    return (T)ret;
}
template<typename T>inline T POW(T B,T P)
{
    if(P==0) return 1;
    if(P&1) return B*POW(B,P-1);
    else return SQR(POW(B,P/2));
}
template <typename T>inline T ModInv (T b,T m)
{
    return BMOD(b,m-2,m);
}
template<typename T>inline T ABS(T a)
{
    if(a<0)return -a;
    else return a;
}
template<typename T>inline T gcd(T a,T b)
{
    if(a<0)return gcd(-a,b);
    if(b<0)return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}
template<typename T>inline T lcm(T a,T b)
{
    if(a<0)return lcm(-a,b);
    if(b<0)return lcm(a,-b);
    return a*(b/gcd(a,b));
}

//for(__typeof(pp.begin()) i=pp.begin(); i!=pp.end(); i++ )

//knight and king move....



//int Dx[]={-2,-1,1,2,1,2,-2,-1};
//int Dy[]={-1,-2,2,1,-2,-1,1,2};
//int dx[]={-1,1,0,0};
//int dy[]={0,0,-1,1};
//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
int dx[]= {-1,-1,-1,0,0,1,1,1};
int dy[]= {-1,0,1,-1,1,-1,0,1};
//////////////

LL n,k;
struct horse
{
    int pos,speed;
} arr[10005];

bool cmp(horse p,horse q)
{
    if(p.pos<q.pos)return true;
    else return false;
}
double dis;
double BS(double lo , double hi,int ii,int j)
{
    double mid;
    double ans=0.0;
//    cout<<lo<<" "<<hi<<" "<<dis<<endl;
    for(int i=1; i<=100; i++)
    {
        mid=(lo+hi)/2.0;

        double t1=((1.0)*(mid-dis))/((1.0)*arr[ii].speed);
        double t2=((1.0)*(mid-arr[j].pos*1.0))/((1.0)*arr[j].speed);
//        cout<<t1<<" "<<t2<<" "<<mid<<" "<<(mid-dis)<<endl;
        if(fabs(t1-t2)<=0.000000001)
        {
            ans=t1;
            dis=mid;
            break;
        }
        else if(t1<t2)hi=mid;
        else lo=mid;
    }
//    cout<<ans<<endl;
//    if(ans==0.0)printf("*****\n");
    return ans;
}


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t,tc=1;
    S(t);
    while(t--)
    {
        SLL2(k,n);
        int id=1;
        for(int i=1; i<=n; i++)
        {
            LL a,b;
            SLL2(a,b);
            arr[id]= {a,b};
            id++;
        }

        sort(arr+1,arr+id,cmp);
        double tot=0.0;

        if(n==1)
        {
            tot=((k-arr[n].pos)*(1.0))/((1.0)*arr[n].speed);
//            cout<<arr[n].pos<<" "<<arr[n].speed<<endl;
        }
        else
        {
            int lst=1;
            dis=arr[1].pos*1.0;
            for(int i=1; i<n-1; i++)
            {
                double t1=((arr[i+2].pos-arr[i+1].pos)*1.0)/(arr[i+1].speed*1.0);
                double t2=((arr[i+2].pos-dis)*1.0)/(arr[lst].speed*1.0);
                if(t1<t2)
                {
                    //tot+=(k*1.0-dis)/(1.0*arr[lst].speed);
                }
                else
                {
                    tot+=BS(arr[i+1].pos,arr[i+2].pos,lst,i+1);
                    //tot+=(1.0*(arr[i+2].pos*1.0-dis))/(arr[i+1].speed*1.0);
                    lst=i+1;
                }
            }

            double t1=((k-arr[n].pos)*1.0)/(arr[n].speed*1.0);
            double t2=((k-arr[lst].pos)*1.0)/(arr[lst].speed*1.0);
            if(t1<t2)
            {
                tot+=((k*1.0-dis)*1.0)/(arr[lst].speed*1.0);
            }
            else
            {
                tot+=BS(arr[n].pos,k,lst,n);
//                cout<<tot<<" "<<dis<<endl;

                tot+=(1.0*(k*1.0-dis))/(arr[n].speed*1.0);
            }

        }
//        cout<<tot<<endl;
        double ans=((1.0)*k)/((1.0)*tot);

        printf("Case #%d: %0.6lf\n",tc++,ans);

    }
    return 0;
}
