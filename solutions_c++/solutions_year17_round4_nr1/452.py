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
#define OC printf("Case #%d:",cs);
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

int v[5];

int call2() {
    int ans = v[0];
    int tmp = v[1] / 2;
    ans += tmp;
    v[1] -= (tmp*2);
    ans += v[1];
    return ans;
}

int call3() {
    int ans = v[0];
    int tmp = min(v[1],v[2]);
    ans += tmp;
    v[1] -= tmp;
    v[2] -= tmp;
    if(v[1]) {
        tmp = v[1] / 3;
        ans += tmp;
        v[1] -= (tmp*3);
        ans += bool(v[1] > 0);
    } else if(v[2]) {
        tmp = v[2] / 3;
        ans += tmp;
        v[2] -= (tmp*3);
        ans += bool(v[2] > 0);
    }
    return ans;
}

int call4(){
    int ans = v[0];
    int tmp = min(v[1],v[3]);
    ans += tmp;
    v[1] -= tmp;
    v[3] -= tmp;
    tmp = v[2] / 2;
    ans += tmp;
    v[2] -= (tmp*2);
    if(v[1] && v[2]) {
        ans++;
        v[1] -= 2;
        if(v[1] > 0) {
            tmp = v[1] / 4;
            ans += tmp;
            v[1] -= (tmp*4);
            ans += bool(v[1] > 0);
        }
    } else if(v[3] && v[2]) {
        ans++;
        v[3] -= 2;
        if(v[3] > 0) {
            tmp = v[3] / 4;
            ans += tmp;
            v[3] -= (tmp*4);
            ans += bool(v[3] > 0);
        }
    } else if(v[1]) {
        tmp = v[1] / 4;
        ans += tmp;
        v[1] -= (tmp*4);
        ans += bool(v[1] > 0);
    } else if(v[2]) {
        ans++;
    } else if(v[3]) {
        tmp = v[3] / 4;
            ans += tmp;
            v[3] -= (tmp*4);
            ans += bool(v[3] > 0);
    }
    return ans;
}




int main() {
#ifdef Sanim
    freopen ("in.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
#endif
    int t = II;
    For(cs,t) {
        int n = II, p = II;
        memo(v,0);
        rep(i,n) {
            int x = II%p;
            ++v[x];
        }
        OC;
        if(p == 2) {
            printf(" %d\n", call2());
        } else if(p == 3) {
            printf(" %d\n", call3());
        } else if(p == 4) {
            printf(" %d\n", call4());
        }
        __(cs)
    }
}
