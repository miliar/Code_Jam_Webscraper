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

bool arr[MAXN];
int l[MAXN], r[MAXN];
LL N,K;

int pos = 0;
int mini = N + 1;
int maxa = 0;

int find()
{
    FILL(l, 0);
    FILL(r, 0);
    int lprev = 0;
    //From left
    FOR(i,1,N) {
        if(arr[i]) {
            lprev = i;
        }
        l[i] = i - lprev - 1;
    }
    int rprev = N+1;
    FORN(i,N,1) {
        if(arr[i]) {
            rprev = i;
        }
        r[i] = rprev - i - 1;
    }

    pos = 0;
    mini = 0;
    maxa = 0;

    FOR(i,1,N)
    {
        if(!arr[i])
        {
            int mi = MIN(l[i], r[i]);
            int ma = MAX(l[i], r[i]);
            if(mi > mini) {
                mini = mi;
                maxa = ma;
                pos = i;
            }
            else if(mi == mini)
            {
                if(ma > maxa)
                {
                    mini = mi;
                    maxa = ma;
                    pos = i;
                }
            }
        }
    }
    return pos;
}
int main()
{
	int T = 1;
	SI(T);
	int val=1;
	while(T--)
	{
        SLL(N);
        SLL(K);
        FILL(arr, 0);
        arr[0] = true;
        arr[N+1] = true;
        FOR(i,1,K-1){
            int pos = find();
            arr[pos] = true;
        }
        find();
        cout<<"Case #"<<val<<": ";
        cout<<maxa <<" "<<mini << endl;
        val++;
    }
	return 0;
}
