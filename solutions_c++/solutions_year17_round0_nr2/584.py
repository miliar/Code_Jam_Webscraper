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

bool istidy(ll n) {
	int last = 9;
	while (n > 0) {
		int k = n % 10;
		if (k > last) return false;
		last = k;
		n /= 10;
	}
	return true;
}

int main() {

	ll n, m, ans;
	scanf("%lld", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%lld", &m);
		if (m < 10) ans = m;

		ll tt = 10;
		ll t;

		while (!istidy(m)) {
			t = m % tt;
			m -= t+1;
			tt *= 10;
		}
		cout << "Case #" << i << ": " << m << endl;

	}

}