/********************************
*MAHBUBCSEJU                    *
*CSE 22                         *
*JAHANGIRNAGAR UNIVERSITY       *
*TIMUS:164273FU                 *
*UVA>>LIGHTOJ>>HUST:mahbubcseju */
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>
#include <deque>
#include <climits>
#include <complex>
#include <bitset>
#include <limits>
#define ll long long int
#define ull unsigned long long int
#define I(a) scanf("%d",&a)
#define I2(a,b) scanf("%d%d",&a,&b)
#define I3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define L(a) scanf("%lld",&a)
#define L2(a,b) scanf("%lld%lld",&a,&b)
#define L3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define PI(a) printf("%d",a)
#define PL(a) printf("%lld",a)
#define PT(t) printf("Case %d: ",t)
#define PB push_back
#define x first
#define y second
#define xx first.first
#define xy first.second
#define yx second.first
#define yy second.second
#define SC scanf
#define PC printf
#define NL printf("\n")
#define SET(a) memset(a,0,sizeof a)
#define SETR(a) memset(a,-1,sizeof a)
#define SZ(a) ((int)a.size())-1
#define f(i,a,b) for(int i=a;i<=b; i++)
#define fr(i,a,b) for(int i=a;i<=b; i++)
#define frr(i,a,b) for(int i=a;i>=b; i--)
#define frv(i,a)  for(int i=0;i<a.size();i++)
//#define pi 2.0*acos(0.0)
#define R(a) freopen(a, "r", stdin);
#define W(a) freopen(a, "w", stdout);
#define CB(x) __builtin_popcount(x)
#define STN(a) stringtonumber<ll>(a)
#define lol printf("BUG\n")
#define Endl "\n"
#define mk make_pair
using namespace std;
template <class T> inline T BM(T p, T e, T M) {
    ll ret = 1;
    for (; e > 0; e >>= 1) {
        if (e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a, T b) {
    if (b == 0)return a;
    return gcd(b, a % b);
}
template <class T> inline T mdINV(T a, T M) {
    return BM(a, M - 2, M);
}
template <class T> inline T PW(T p, T e) {
    ll ret = 1;
    for (; e > 0; e >>= 1) {
        if (e & 1) ret = (ret * p);
        p = (p * p);
    }
    return (T)ret;
}
template <class T>string NTS ( T Number ) {
    stringstream ss;
    ss << Number;
    return ss.str();
}
template <class T>T stringtonumber ( const string &Text ) {
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
template <class T>bool ISLEFT ( T a, T b, T c) {
    if (((a.xx - b.xx) * (b.yy - c.yy) - (b.xx - c.xx) * (a.yy - b.yy)) < 0.0)return 1; //Uporer dike //A,b,c, x okkher ordera sorted
    else return 0;
}


typedef pair<int ,char> P;
typedef vector<int> V;

//////////////////////
///////////////////////////
#define mx 2000000
#define md 1000000001ull

int main() {
    R("in.txt");
    W("out.txt");
    int tc,cs=0;
    I(tc);
    while(tc--) {
        int n;
        I(n);

        int r,y,b;
        I(r);
        int x;
        I(x);
        I(y);
        I(x);
        I(b);
        I(x);

        PC("Case #%d: ",++cs);
        if(r>y+b||y>r+b||b>r+y)PC("IMPOSSIBLE\n");
        else {
            P a[5];
            a[1]=mk(r,'R');
            a[2]=mk(y,'Y');
            a[3]=mk(b,'B');

            sort(a+1,a+3+1);
    // cout<<a[1].x<<" "<<a[2].x<<" "<<a[3].x<<endl;
            string s;

            while(a[2].x>a[1].x) {
                s+=a[3].y;
                a[3].x--;
                s+=a[2].y;
                a[2].x--;
              //  cout<<s<<Endl;
            }
           // lol;
            bool fl=0;

            while(a[3].x>0) {
                if(fl==0) {
                    a[3].x--;
                    s+=a[3].y;
                    s+=a[2].y;
                    a[2].x--;
                } else {
                    a[3].x--;
                    s+=a[3].y;
                    s+=a[1].y;
                    a[1].x--;
                }
                fl^=1;
                //cout<<s<<endl;
            }
            while(a[2].x+a[1].x>0) {
                if(fl==0) {
                    s+=a[2].y;
                    a[2].x--;
                } else {
                    s+=a[1].y;
                    a[1].x--;
                }
                fl^=1;
            }
            cout<<s<<Endl;
        }



    }

    return 0;
}

