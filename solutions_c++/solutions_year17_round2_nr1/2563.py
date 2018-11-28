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

double mxd(double a, double b) {if (a > b) return a; return b;};

/*-----------------END TEMPLATE-----------------*/

int main() {

	ll a, b, c, d, e, f, n, m;

	scanf("%lld", &a);
	for (int z = 1; z <= a; z++) {
		scanf("%lld %lld", &d, &n);

		vii horses;
		for (int i = 0; i < n; i++) {
			scanf("%lld %lld", &b, &c);
			horses.pb(ii(b, c));
		}

		sort(horses.begin(), horses.end(), std::greater<ii>());

		double t1 = -1, t2;
		for (auto h : horses) {
			t2 = (double(d)-double(h.ff))/double(h.ss);

			t1 = mxd(t1, t2);
		}
		printf("Case #%d: %.6lf\n", z, d/t1);


	}

}