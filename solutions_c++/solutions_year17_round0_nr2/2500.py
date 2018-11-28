
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

int main()
{
    freopen("inputB.txt", "r", stdin);
    freopen("outputB.txt", "w", stdout);

	int T = 1;
	SI(T);
	FOR(test,1,T)
	{
        string s;
        cin>>s;
        int n = s.length();
        VI v(n+5);
        FOR(i,1,n){
            v[i] = s[i-1]-48;
        }
        int limit = 1;
        FORN(i,n-1,limit){
            if(v[i] > v[i+1]){
                FOR(k,i+1,n)
                    v[k] = 9;
                int j = i;
                while(j >= limit && --v[j] < 0) {
                    v[j] = 9;
                    --j;
                }
                if(v[limit]==0)
                    ++limit;
            }
        }
        int startPos = 1;
        while(v[startPos]==0)
            ++startPos;
        cout<<"Case #"<<test<<": ";
        FOR(i,startPos,n)
            cout<<v[i];
        cout<<endl;
	}
	return 0;
}
