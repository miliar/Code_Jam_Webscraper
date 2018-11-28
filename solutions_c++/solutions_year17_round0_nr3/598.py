#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define eb emplace_back
#define fff ff
#define sss ss.ff
#define ttt ss.ss
#define INF (1 << 30)
#define LLF (1ll << 60)


#define FASTIO std::ios::sync_with_stdio(false)

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef unsigned int ui;

ll min(ll a, ll b) {if (a < b) return a; return b;};
ll max(ll a, ll b) {if (a > b) return a; return b;};
ll gcd(ll a, ll b) {return b == 0 ? a : gcd(b, a % b);};

/*-----------------END TEMPLATE-----------------*/

ll log2(ll a) {
	ll t = 0;
	while (a >= 2) {
		a /= 2;
		t++;
	}
	return t;
}

int main() {

	ll n, a, b, c;
	scanf("%lld", &n);
	for (ll i = 1; i <= n; i++) {
		scanf("%lld %lld", &a, &b);




		ll a1, a2;
		ll lg2 = log2(b);

		ll div = (1ll << lg2);
		ll aa = a-div+1;
		aa /= div;
		ll qty = (a-div+1)-(aa*div);

		ll k = aa;
		if (b-div < qty) k++;
		
		a1 = k/2;
		a2 = k/2;
		if (k%2 == 0) a2--;


		printf("Case #%lld: %lld %lld\n", i, a1, a2);

	}

}