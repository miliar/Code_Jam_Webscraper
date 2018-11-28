#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll floor(ll n, ll d) {return n / d;}
ll ceil(ll n, ll d) {return (n + d - 1) / d;}

pair<ll, ll> f(ll N) {
  return make_pair(floor(N - 1, 2L), ceil(N - 1, 2L));
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int cases; cin >> cases;
	for (int cc = 0; cc < cases; ++cc) {
		cout << "Case #" << cc + 1 << ": ";

		ll N, K; cin >> N >> K;

		// A map from a subsection's length to the count of subsections that have this length
		map<ll, ll> lengthsCount; lengthsCount[-N] = 1L;
		ll entered = 0L;
		while(entered + lengthsCount.begin()->second < K) {
		  map<ll, ll>::iterator curIt = lengthsCount.begin();
		  entered += curIt->second;
		  pair<ll, ll> minMax = f(-curIt->first);
		  lengthsCount[-minMax.first] += curIt->second; lengthsCount[-minMax.second] += curIt->second;
		  lengthsCount.erase(lengthsCount.begin());
		}

    map<ll, ll>::iterator curIt = lengthsCount.begin();
    pair<ll, ll> minMax = f(-curIt->first);

		cout << minMax.second << " " << minMax.first << "\n";
	}
	return 0;
}
