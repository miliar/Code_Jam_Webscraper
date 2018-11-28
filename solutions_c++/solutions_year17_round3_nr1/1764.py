#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <queue>
#include <iomanip>  

using namespace std;

# define M_PIl          3.141592653589793238462643383279502884L /* pi */

const string IMP = "IMPOSSIBLE";
typedef unsigned long long int ll;

ll solve(int n, int k, vector<pair<ll, ll>>& v) {
	sort(v.begin(), v.end());
	ll best = 0;
	for (int top = n - 1 ; top>= 0; --top) {
		ll loc = v[top].first*v[top].first+2*v[top].first*v[top].second;
		vector<ll> pre;
		for(int i=0; i<top; ++i) {
			pre.push_back(v[i].first * v[i].second);
		}
		if (pre.size() < k - 1 || pre.size() ==0) {
			best = max(best, loc);
			continue;
		}
		sort(pre.begin(), pre.end());
		for(int i=pre.size() - 1; i >= (int)pre.size() + 1 - k; --i) {
			loc+=2*pre[i];
		}
		best = max(best, loc);
	}
	return best;
}

int main() {
  freopen("in", "r", stdin);
	freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
		int n, k;
		cin>>n >>k;
		vector<pair<ll, ll>> v;
		for(int i=0; i<n; ++i) {
			ll x, y;
			cin>>x >>y;
			v.push_back(make_pair(x, y));
		}
		ll res = solve(n, k, v);
		cout << std::setprecision(100)<< M_PIl * res << endl;
		//cout << M_PIl * res << endl;
  }
  return 0;
}
