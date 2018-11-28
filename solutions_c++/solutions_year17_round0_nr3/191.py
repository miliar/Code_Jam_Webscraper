#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include <assert.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <list>
#include <bitset>
#include <vector>
using namespace std;

#define LL long long

#define fi first
#define se second
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1
#define ls id<<1
#define rs id<<1|1
#define MID(a,b) (((a)+(b))>>1)
#define maxx(a,b) ((a)<(b)?(b):(a))
#define minx(a,b) ((a)<(b)?(a):(b))
#define absx(a) ((a)<0?-(a):(a))
#define mk(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define itr iterator
#define lowbit(x) ((x)&-(x))

typedef unsigned LL ULL;
typedef unsigned uint;
typedef map<int,int> mii;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<LL,LL> pLL;

template< typename T > inline void read(T &x) {
    bool f=0; char ch=getchar(); x=0;
    while(ch<'0' || ch>'9') {if(ch=='-') f=1; ch=getchar();}
    while(ch>='0' && ch<='9') {x=x*10+ch-'0'; ch=getchar();}
    if(f) x=-x;
}

template< typename T > inline void Max(T &a, T b) {if(a<b) a=b;}
template< typename T > inline void Min(T &a, T b) {if(b<a) a=b;}
template< typename T > inline T Abs(T a) {if(a<0) return -a; else return a;}

const double pi=(double) acos(-1.0);
const int MOD=(int) 1e9+7;
const int INF=(int) 0x3f3f3f3f;
const LL  LINF=(LL) INF<<32|INF;
const int SINF=(uint) ~0>>1;
const LL  SLINF=(ULL) (-1)>>1;
const double DINF=(double) 1e50;
const double eps=(double) 1e-4;
const int maxn=(int) 1e3+10;
const int maxm=(int) 1e4+10;
const int maxk=(int) 5e2+10;

inline int sig(double x) {return x<-eps?-1:x>eps;}

//--------------start------------------

LL n,k;



void work()
{
    int tc; read(tc);
    int T_T=0;
    while(tc--)
    {
        read(n), read(k);
        LL ans_max, ans_min;
        LL tmax,cmax,tmin,cmin;
        tmax=n, cmax=1, tmin=0, cmin=0;

        LL nk=1;
        while(1)
        {
//            cout <<"tt : " <<tmax <<" " <<cmax <<" " <<tmin <<" " <<cmin <<endl;
            if(nk>=k)
            {
                if(k<=cmax)
                {
                    ans_max = tmax/2;
                    ans_min = (tmax-1)/2;
                }
                else
                {
                    ans_max = tmin/2;
                    ans_min = (tmin-1)/2;
                }
                break;
            }
            LL t1,t2=0,t3,t4=0;

            if(tmax&1) t1=(tmax-1)/2, t2+=cmax<<1;
            else t1=(tmax)/2, t2+=cmax, t3=(tmax-1)/2, t4+=cmax;

            if(cmin)
            {
                if(tmin&1) t4+=cmin<<1;
                else t3=(tmin-1)/2, t2+=cmin, t4+=cmin;
            }

            tmax=t1;
            cmax=t2;
            tmin=t3;
            cmin=t4;

            k-=nk;
            nk<<=1;
        }

        printf("Case #%d: ",++T_T);
        cout <<ans_max <<" " <<ans_min <<endl;
    }
}

//--------------end--------------------

//#define yukihana0416
int main()
{
#ifdef yukihana0416
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
#endif // yukihana0416
    work();
    return 0;
}
