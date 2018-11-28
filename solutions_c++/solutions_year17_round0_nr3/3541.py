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
#define CB(x) __builtin_popcountll(x)
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


typedef pair<ll , ll > P;
typedef vector<int> V;
//////////////////////////
/////////////////////////
#define md 1000000007ll
#define mx 1000000

int main() {
    R("C-large.in");
    W("C-large.txt");
    int tc,cs=0;
    I(tc);
    while(tc--) {
        ll n,m;
        L2(n,m);
        queue<P>q;        q.push(mk(n,1));
        map<ll,ll>mp;
        mp[n]=1;
        P ar[2000];
        ll sz=0;
        ar[++sz]=mk(n,1);
        while(!q.empty()) {
            P f=q.front();
            q.pop();
            P f1=f;
             if(q.size()>0&&q.front().y==f.y){
                f1=q.front();
                q.pop();
             }
          //   cout<<f.x<<" "<<f1.x<<" "<<f.y<<" "<<f1.y<<Endl;
//             getchar();

            if(f==f1) {
                ll x=f.x;
                if(x%2==1) {
                    ll x1=x/2;
                    ll x2=x1;

                    mp[x1]+=2*mp[x];
                    if(x1!=0)
                        ar[++sz]=mk(x1,mp[x1]);
                    if(x1!=0) {
                           // cout<<ar[sz].x<<endl;
                        q.push(mk(x1,f.y+1));
                    }
                } else {
                    ll x1=x/2-1;
                    ll x2=x/2;
                    mp[x1]+=mp[x];
                    mp[x2]+=mp[x];
                    if(x1!=0)
                        ar[++sz]=mk(x1,mp[x1]);
                    if(x2!=0)
                        ar[++sz]=mk(x2,mp[x2]);
                    if(x1!=0)
                        q.push(mk(x1,f.y+1));
                    if(x2!=0)
                        q.push(mk(x2,f.y+1));

                }
            } else {
                P a[5];
                int l=0;
                ll x=f.x;
                ll x1,x2;
                if(x%2==1)x1=x2=x/2;
                else x1=x/2-1,x2=x/2;


                if(x1!=0)
                    a[++l]=mk(x1,mp[x]);
                if(x2!=0)
                    a[++l]=mk(x2,mp[x]);
                x=f1.x;

                if(x%2==1)x1=x2=x/2;
                else x1=x/2-1,x2=x/2;

                if(x1!=0)
                    a[++l]=mk(x1,mp[x]);
                if(x2!=0)
                    a[++l]=mk(x2,mp[x]);


                for(int j=1; j<=l; j++) {
                    if(a[j].x==-1)continue;
                    ll kop=a[j].x;
                    for(int k=j; k<=l; k++) {
                        if(kop==a[k].x) {
                            mp[kop]+=a[k].y;
                            a[k].x=-1;
                        }
                    }
                    ar[++sz]=mk(kop,mp[kop]);
                    q.push(mk(kop,f.y+1));

                }

            }
        }

        for(int i=1; i<=sz; i++)ar[i].x*=-1;

        sort(ar+1,ar+sz+1);
        ll ko=0;
        ll t=0;
        for(ll i=1; i<=sz; i++) {
               // cout<<ar[i].x<<" "<<ar[i].y<<endl;
            ko+=ar[i].y;
            if(ko>=m) {
                t=-ar[i].x;
                break;
            }
        }

     //cout<<t<<endl;
        ll ans=0,sum=0;
        if(t%2==1) {
            ans=t/2;
            sum=t/2;
        } else
            ans=t-t/2,sum=t/2-1;
        PC("Case #%d: %lld %lld\n",++cs,ans,sum);

    }


    return 0;
}

