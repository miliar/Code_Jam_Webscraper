#pragma comment(linker, "/stack:640000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
const double PI=acos(-1.0);

#define    READ(f) 	         freopen(f, "r", stdin)
#define    WRITE(f)   	     freopen(f, "w", stdout)
#define    MP(x, y) 	     make_pair(x, y)
#define    PB(x)             push_back(x)
#define    rep(i,n)          for(int i = 1 ; i<=(n) ; i++)
#define    repI(i,n)         for(int i = 0 ; i<(n) ; i++)
#define    FOR(i,L,R) 	     for (int i = L; i <= R; i++)
#define    ROF(i,L,R) 	     for (int i = L; i >= R; i--)
#define    FOREACH(i,t)      for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define    ALL(p) 	         p.begin(),p.end()
#define    ALLR(p) 	         p.rbegin(),p.rend()
#define    SET(p) 	         memset(p, -1, sizeof(p))
#define    CLR(p)            memset(p, 0, sizeof(p))
#define    MEM(p, v)         memset(p, v, sizeof(p))
#define    getI(a) 	         scanf("%d", &a)
#define    getII(a,b) 	     scanf("%d%d", &a, &b)
#define    getIII(a,b,c)     scanf("%d%d%d", &a, &b, &c)
#define    getL(a)           scanf("%lld",&a)
#define    getLL(a,b)        scanf("%lld%lld",&a,&b)
#define    getLLL(a,b,c)     scanf("%lld%lld%lld",&a,&b,&c)
#define    getC(n)           scanf("%c",&n)
#define    getF(n)           scanf("%lf",&n)
#define    getS(n)           scanf("%s",n)
#define    bitCheck(N,in)    ((bool)(N&(1<<(in))))
#define    bitOff(N,in)      (N&(~(1<<(in))))
#define    bitOn(N,in)       (N|(1<<(in)))
#define    iseq(a,b)          (fabs(a-b)<EPS)
#define    ff 	 first
#define    ss 	 second
#define    ll	 long long
#define    ull 	 unsigned long long


typedef pair<int,int>pii;
typedef vector<pii>vpii;
typedef vector<int>vi;
typedef vector<vi>vii;


template< class T > inline T _abs(T n) { return ((n) < 0 ? -(n) : (n)); }
template< class T > inline T _max(T a, T b) { return (!((a)<(b))?(a):(b)); }
template< class T > inline T _min(T a, T b) { return (((a)<(b))?(a):(b)); }
template< class T > inline T _swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > inline T gcd(T a, T b) { return (b) == 0 ? (a) : gcd((b), ((a) % (b))); }
template< class T > inline T lcm(T a, T b) { return ((a) / gcd((a), (b)) * (b)); }
template <typename T> string NumberToString ( T Number ) { ostringstream ss; ss << Number; return ss.str(); }

#ifdef howcum
     #define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

//// 4 direction
//int dx[]={-1,1,0,0};
//int dy[]={0,0,-1,1};
//
//// 8 direction
//int dx[]={-1,1,0,0,-1,-1,1,1};
//int dy[]={0,0,-1,1,-1,1,1,-1};
//
//// horse
//int dx[] = {-2,-2,2,2,-1,-1,1,1};
//int dy[] = {1,-1,-1,1,2,-2,-2,2};

typedef pair<int,pii> custom;

int main() {
    #ifdef howcum
        READ("inC.txt");
        WRITE("outC2.txt");
    #endif // howcum
//    ios_base::sync_with_stdio(0); cin.tie(0);

    int T;
    getI(T);
    for(int tc=1;tc<=T;tc++)
    {
        int n,k;
        getII(n,k);
        //debug(n,k)
        n+=2;
//        int a[n+1];
//        CLR(a);
//        a[1]=1;
//        a[n]=1;


        priority_queue<custom>pq;

        pq.push(MP((n-1),pii(1,n)));

        int resL,resR;
        while(k--)
        {
            custom now = pq.top();
            pq.pop();

            int mid = (now.ss.ff+now.ss.ss)/2;

            int L,R;
            L=max(0,mid-now.ss.ff-1);
            R=max(0,now.ss.ss-mid-1);
            //debug(k,mid,now.ff,now.ss.ff,now.ss.ss,L,R);
            resL=L;
            resR=R;
            pq.push(MP((L),pii(now.ss.ff,mid)));
            pq.push(MP((R),pii(mid,now.ss.ss)));
        }

//        int resL,resR;
//        for(int i=0;i<k;i++)
//        {
//            int L,R,s=-1;
//            pii origin;
//            int tempL,tempR,tempS;
//            vpii temp;
//            pii now;
//            while(!segs.empty())
//            {
//                now = segs.top();
//                segs.pop();
//                temp.PB(now);
//
//                int mid = (now.ff+now.ss)/2;
//                if(s==-1)
//                {
//                    s=mid;
//                    L=s-now.ff-1;
//                    R=now.ss-s-1;
//                    origin=now;
//                }
//                else
//                {
//                    tempS=mid;
//                    tempL=s-now.ff-1;
//                    tempR=now.ss-s-1;
//                    if(min(L,R)<min(tempL,tempR))
//                    {
//                        L=tempL;
//                        s=tempS;
//                        R=tempR;
//                        origin=now;
//                    }
//                    else if(min(L,R)==min(tempL,tempR))
//                    {
//                        if(max(L,R)<max(tempL,tempR))
//                        {
//                            L=tempL;
//                            s=tempS;
//                            R=tempR;
//                            origin=now;
//                        }
//                        else if(max(L,R)==max(tempL,tempR))
//                        {
//                            if(tempS<s)
//                            {
//                                L=tempL;
//                                s=tempS;
//                                R=tempR;
//                                origin=now;
//                            }
//                        }
//                    }
//                }
//            }
//            if(i==k-1)
//                {
//                    resL=max(0,L);
//                    resR=max(0,R);
//                    break;
//                }
//                for(int j=0;j<temp.size();j++)
//                {
//                    if(temp[j].ff==origin.ff && temp[j].ss==origin.ss)
//                    {
//                        continue;
//                    }
//                    segs.push(temp[j]);
//                    //debug(temp[j].ff,temp[j].ss)
//                }
//
//                segs.push(pii(now.ff,s));
//                segs.push(pii(s,now.ss));
//        }

        printf("Case #%d: %d %d\n",tc, max(resL,resR),min(resL,resR));


    }

    return 0;
}



