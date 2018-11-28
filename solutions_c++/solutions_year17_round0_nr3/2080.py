/*
Author :: MD. Musfiqur Rahman Sanim
Aust cse 28th Batch
ID:11.02.04.097
*/


//{ Template
using namespace std;
//{ headers
#include<bits/stdc++.h>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS 1e-7
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2*acos (0.0)
//}
typedef long long int64;
typedef unsigned long long int64u;
#define memo(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define db double
#define pb push_back
#define pii pair<int ,int >
#define NL puts("")
#define ff first
#define ss second
//{
//Intput_Output
#define gc getchar
template<class T>inline bool read(T &x){int c=gc();int sgn=1;while(~c&&c<'0'|c>'9'){if(c=='-')sgn=-1;c=gc();}for(x=0;~c&&'0'<=c&&c<='9';c=gc())x=x*10+c-'0';x*=sgn;return ~c;}
#define II ({ int a; read(a); a;})
#define IL ({ int64 a; read(a);  a;})
#define ID ({ db a; scanf("%lf",&a);  a;})
#define IC ({ char a; scanf("%c",&a);  a;})
#define IS ({ string a; cin >> a;  a;})
#define OC printf("Case #%d: ",cs);
//}
//}
#define __(args...) {dbg,args; cerr<<endl;}
struct debugger{template<typename T> debugger& operator , (const T& v){cerr<<v<<"    "; return *this; }}dbg;
template <class T, class U> inline T max (T &a, U &b)
{
    return a > b ? a : b;
}
template <class T, class U> inline T min (T &a, U &b)
{
    return a < b ? a : b;
}
template <class T, class U> inline T swap (T &a, U &b)
{
    T tmp = a;
    a = b;
    b = tmp;
}
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 Direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[6]={2,1,-1,-2,-1,1};int dy[6]={0,1,1,0,-1,-1}; //Hexagonal Direction

const int64 INF = (1ll)<<50;
const int mx = 1e5 + 7;
const int mod = 1000000007 ;
const db pi = PI;
int EQ(double d) {
    if ( fabs(d) < EPS ) return 0;
    return d > EPS ? 1 : -1 ;
}

int64 dp[2];
int64 a,b;

int main() {
#ifdef Sanim
    freopen ("in.txt", "r", stdin);
     freopen ("output.txt", "w", stdout);
#endif
    int t = II;
    For(cs,t) {
        int64 n = IL, k = IL;
        OC;
        if(k == 1) {
            int64 tmp = n/2;
            cout << tmp << " " << (n - tmp - 1) << endl;
            continue;
        }
        int64  p = 1, pre = 0, tot = 0, l = 0;
        while(true) {
            pre = tot;
            tot += p;
            if(tot >= k) break;
            p <<= 1ll;
            ++l;
        }
        a = n/2, b = n - (n/2) - 1;
        dp[0] = dp[1] = 1;
        rep(i,l-1) {
            int64 x1 = dp[0];
            int64 y1 = dp[1];
            dp[0] = dp[1] = 0;
            int64 x = a/2;
            if((a/2) == x) dp[0] += x1;
            else dp[1] += x1;

            if((a - (a/2)-1) == x) dp[0] += x1;
            else dp[1] += x1;

            if((b/2) == x) dp[0] += y1;
            else dp[1] += y1;

            if((b - (b/2) - 1) == x) dp[0] += y1;
            else dp[1] += y1;

            a = x;
            b = (b - (b/2) - 1);
        }
        k -= pre;
        int64 ans ;
        if(k > dp[0]) ans = b;
        else ans = a;
        cout << (ans/2) << " " << (ans - (ans/2) - 1) << endl;
    }
}
