#include <stdio.h>
#include <bits/stdc++.h>			

#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e6 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;

void megaRandom() {
	unsigned int FOR;
 	asm("rdtsc" : "=A"(FOR));
  	srand(FOR);
}

double d, a, b, mx;
int k;

void solve(int test) {
	mx = -1e18;
	cin >> d >> k;
	for(int i = 1; i <= k; i ++) {
		cin >> a >> b;
		mx = max(mx, (d - a) / b);
	}
	cout << "Case #" << test << ": " << fixed << setprecision(6) << d / mx << "\n";
}

int main() {
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
	megaRandom();
	int t;
	cin >> t;
	for(int it = 1; it <= t; it ++)
		solve(it);
	return 0;
}
