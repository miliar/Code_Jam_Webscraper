#include <string>
#include <vector>
#include <iostream>

using namespace std;

const string IMP = "IMPOSSIBLE";
typedef unsigned long long int ll;
ll solve(ll n) {
	vector<ll> v;
	ll temp = 1;
	for (ll i=0; i<22; ++i) {
		v.push_back(temp);
		temp*=10;
	}

	ll k = 0;
	ll r = 1;
	while(r<=n) {
		k++;
		r*=10;
	}
	k--;
	for (ll i = k; i>0; --i) {
		ll x = (n / v[i])%10;
		ll y = (n / v[i-1])%10;
		if (x>y) {
			ll head = n/v[i];
			head--;
			ll tail = v[i] - 1;
			return solve(head*v[i] + tail);
		}
	}
	return n;
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
		long long int n;
		cin >> n;
		cout << solve(n) << endl;
  }
  return 0;
}
