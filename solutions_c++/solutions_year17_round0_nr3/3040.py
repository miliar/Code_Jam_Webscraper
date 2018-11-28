#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

struct Result {
	ll a, b;
	Result(ll _a, ll _b): a(_a), b(_b) {
	};
};

ostream& operator << (ostream& out, Result r) {
	out << r.a << " " << r.b;
	return out;
}

Result test() {
	map<ll, ll> mapa;
	ll n, k;
	cin >> n >> k;
	mapa[n] = 1;
	while (true) {
		auto it = mapa.rbegin();
		ll key = it -> first;
		ll count = it -> second;
		mapa.erase(key);
		k -= count;
		ll a = key / 2;
		ll b = (key - 1) / 2;
		if (k <= 0) return Result(a, b);
		mapa[a] += count;
		mapa[b] += count;
	}
}

int main()
{
	int t;
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		cout << "Case #" << i <<": " << test() << "\n";
	}
}
