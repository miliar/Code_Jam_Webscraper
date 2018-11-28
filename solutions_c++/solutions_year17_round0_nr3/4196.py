#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ull unsigned long long
#define null NULL
#define PI M_PI
#define sc(x) scanf("%d", &x)
#define sc64(x) scanf("%I64d", &x)
#define scln(x) scanf("%d\n", &x)
#define sc64ln(x) scanf("%I64d\n", &x)
#define pr(x) printf("%I64d", x)
#define prln(x) printf("%I64d\n", x)
#define prsp(x) printf("%I64d ", x)
#define pr64(x) printf("%I64d", x)
#define pr64ln(x) printf("%I64d\n", x)
#define pr64sp(x) printf("%I64d ", x)
#define rep(i,n) for (int i = 1;i <= (n); ++i)
#define repr(i,n) for (int i = (n);i > 0; --i)
#define repab(i,a,b) for (int i = a;i <= b; ++i)
#define Rep(i,n) for (int i = 0;i < (n); ++i)
#define Repr(i,n) for (int i = (n)-1;i >= 0; --i)
#define Repab(i,a,b) for (int i = a;i < b; ++i)
#define SET(__set, val) memset(__set, val, sizeof __set)

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pll;

template<class T> T gcd(T a, T b){if(!b)return a;return gcd(b,a%b);}
template<class T> T power(T a, T b){T res(1);while(b){if(b&1)res=res*a;a=a*a;b>>=1;}return res;}
template<class T> T powerM(T a, T b, T mod){T res(1);while(b){if(b&1)res=res*a%mod;a=a*a%mod;b>>=1;}return res;}

const int infi = 2147483647;
const ll infl = 9223372036854775807;

#define N 1000
#define M 1000
int m, T;
ll n, k;
int main(){
//	freopen("C-large.in", "r", stdin);
//	freopen("C-small-2-attempt0.in", "r", stdin);
//	freopen("1", "w", stdout);
	sc(T);
	rep(xxxx,T){
		printf("Case #%d: ", xxxx);
		sc64(n), sc64(k);
		ll a=1, b=0;
		while (1){
			if (n&1){
				n>>=1;
				if (k > a+b)
					k -= a+b;
				else{
					if (k > a){
						prsp(n), prln(n-1);
						break;
					}else{
						prsp(n), prln(n);
						break;
					}
				}
				ll x = a+a+b;
				ll y = b;
				a = x;
				b = y;
			}else{
				n>>=1;
				if (k > a+b)
					k -= a+b;
				else{
					if (k > a){
						prsp(n-1), prln(n-1);
						break;
					}else{
						prsp(n), prln(n-1);
						break;
					}
				}
				ll x = a;
				ll y = a+b+b;
				a = x;
				b = y;
			}
		}
	}
	return 0;
}

