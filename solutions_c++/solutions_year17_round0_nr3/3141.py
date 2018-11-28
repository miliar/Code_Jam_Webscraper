#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

int TC;
ll N, K;
map<ll, ll> T;

int main() {
	scanf("%d", &TC);
	rep(tc, TC) {
		cin >> N >> K;
		--K;

		T.clear();
		T[N] = 1;
		
		while (K) {
			auto it = T.end(); --it;
			ll x = it->fi, num = it->se;
			ll dec = min(K, num);

			if (x & 1) {
				T[x/2] += dec * 2;
			} else {
				T[x/2] += dec;
				T[x/2-1] += dec;
			}
			T[x] -= dec;
			K -= dec;
			if (dec == num) {
				T.erase(x);
			}
		}

		auto it = T.end(); --it;
		ll a1 = it->fi;
		ll a2 = a1 / 2;
		if (a1 % 2 == 0) --a2;
		printf("Case #%d: %lld %lld\n", tc + 1, a1 / 2, a2);

	}
	return 0;
}