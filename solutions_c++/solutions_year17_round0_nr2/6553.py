#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> ii;

vector<ll> v;

int main() {
	freopen("/Users/vlwk/Documents/Victor Folder/repo/C++/GCJ 2017/Qualification/B-small-attempt0.in", "r", stdin);
	freopen("/Users/vlwk/Documents/Victor Folder/repo/C++/GCJ 2017/Qualification/B.out", "w", stdout);
	ll T, N;
	scanf("%lld", &T);
	for (ll i = 1; i <= T; i++) {
		printf("Case #%lld: ", i);
		scanf("%lld", &N);
		ll x = log10(N);
		v.clear();
		while (N != 0) {
			v.push_back(N % 10);
			N /= 10;
		}
		reverse(v.begin(), v.end());
		while (true) {
			for (ll j = 0; j < x; j++) {
				if (v[j] > v[j+1]) {
					v[j]--;
					for (ll k = j + 1; k <= x; k++) v[k] = 9;
					break;
				}
			}
			bool lb = true;
			for (ll j = 0; j < x; j++) {
				if (v[j] > v[j+1]) lb = false;
			}
			if (lb == true) {
				for (int j = 0; j <= x; j++) {
					if (j == 0 && v[j] == 0) continue;
					printf("%lld", v[j]);
				}
				printf("\n");
				break;
			}
		}
	}
}