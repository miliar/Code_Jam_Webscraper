

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

map<LL,LL> m;
int main()
{
    freopen("inputC.txt", "r", stdin);
    freopen("outputC.txt", "w", stdout);

	int T = 1;
	SI(T);
	FOR(test, 1, T)
	{
	    m.clear();
        LL N,K;
        SLL(N);
        SLL(K);
        m[N] = 1;
        K--;
        while( K>=0 ) {
            map<LL,LL> ::reverse_iterator it = m.rbegin();
            LL len = it -> X;
            LL cnt = it -> Y;

            if(cnt > K) {
                LL r, c;
                if(len % 2 == 0) {
                    c = (len - 1) / 2;
                    r = len / 2;
                }
                else{
                    r = c = len / 2;
                }
                printf("Case #%d: %lld %lld\n", test, r, c);
                break;
            }
            else {

                m.erase(m.find(len));
                K -= cnt;
                //split segment
                LL len1, len2;
                if(len % 2 == 0) {
                    len1 = (len - 1) / 2;
                    len2 = len / 2;
                }
                else{
                    len1 = len2 = len / 2;
                }

                if(len1 > 0) {
                    if(m.find(len1) != m.end()) {
                        m[len1] += cnt;
                    }
                    else{
                        m[len1] = cnt;
                    }
                }

                if(len2 > 0) {
                    if(m.find(len2) != m.end()) {
                        m[len2] += cnt;
                    }
                    else{
                        m[len2] = cnt;
                    }
                }
            }
        }
    }
	return 0;
}
