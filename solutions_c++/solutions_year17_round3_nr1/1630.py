// #include "CodeLikeMartian.h"

#include<bits/stdc++.h>

using namespace std;

typedef long long int LL;
typedef double	D;
typedef long double LD;

#define SI(N) scanf("%d",&N)
#define SLL(N) scanf("%lld",&N)
#define SLF(N) scanf("%lf",&N)
#define MP make_pair
#define PB push_back
#define SZ(x) (x.size())
#define P(x) printf("%d",(x))
#define PLL(x) printf("%lld",(x))
#define line puts("")
#define X first
#define Y second
#define FOR(i,M,N) for(int i=(M);i<=(N);++i)
#define FORN(i,N,M)for(int i=(N);i>=(M);--i)
#define MIN(a,b) ( (a)<(b) ? (a) : (b))
#define MAX(a,b) ( (a)>(b) ? (a) : (b))
#define VI vector<int>
#define VLL vector<ll>
#define PII pair<int,int>
#define VPII vector<PII>
#define FILL(arr,n)memset((arr),n,sizeof((arr)))
#define fastInput ios_base::sync_with_stdio(false)

template<class T> T gcd(T a, T b){if(a==0)return b;if(b==0)return a;return gcd(b,a%b);}
template<class T> T lcm(T a, T b){return a*b/gcd(a,b);}
template<class T>inline bool isPrime(T n){if(n<=1)return false;for(T i=2;i*i<=n;++i)if(n%i==0)return false;return true;}
const int MAXN = 100007;
double pi = 3.14159265359;
bool comp(const pair<int,int> &a, const pair<int,int> &b)
{
    double a1 = 2.0*pi*a.X*(double)a.Y;
    double b1 = 2.0*pi*b.X*(double)b.Y;
    return a1 > b1;
}

int main()
{
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T = 1;
	cin>>T;
	FOR(test, 1, T)
	{
        int N,K;
        cin>>N>>K;
        vector<pair<int,int> > v;
        FOR(i,1,N){
            int t,tt;
            cin >> t >> tt;
            v.PB(MP(t, tt));
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        double ans = 0.0;
        FOR(i,0,N-1){
             vector<pair<int,int> > tm;
             FOR(j,i+1,N-1){

                tm.PB(v[j]);
             }

             double val = 0.0;
                if(tm.size() > 0) {
                 sort(tm.begin(), tm.end(), comp);

                 FOR(j,0,tm.size()-1){
                    if(j == K - 1)
                        break;
                    val += 2.0*pi*tm[j].X*(double)tm[j].Y;
                 }
             }
             val += pi*v[i].X*(double)v[i].X;
             val += 2.0*pi*v[i].X*v[i].Y;
            ans = MAX(ans, val);
        }
        printf("Case #%d: %.9lf\n", test, ans);
	}
	return 0;
}

