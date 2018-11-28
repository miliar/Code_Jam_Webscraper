#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

typedef long long ll;
typedef pair<ll, ll> llpair;

int T;
ll N, K;

map<ll, map<llpair, ll>> cache;

void add_occ(map<llpair, ll>& dest, const llpair& data, ll occ) {
	if (!dest.count(data)) {
		dest[data] = occ;
	}
	else {
		dest[data] += occ;
	}
}

void merge_occ(map<llpair, ll>& src, map<llpair, ll>& dest) {
	for (auto entry : src) {
		add_occ(dest, entry.first, entry.second);
	}
}

map<llpair, ll> obtain_occ(ll n) {
	if (cache.count(n)) return cache[n];
	
	map<llpair, ll> result;
	
	if (n > 0) {
		if (n & 1) { // odd
			ll half = (n - 1) / 2;
			add_occ(result, llpair(half, half), 1);
			map<llpair, ll> sub_result = obtain_occ(half);
			merge_occ(sub_result, result);
			merge_occ(sub_result, result);
		}
		else { // even
			ll half = n / 2;
			add_occ(result, llpair(half, half - 1), 1);
			map<llpair, ll> sub_result1 = obtain_occ(half);
			map<llpair, ll> sub_result2 = obtain_occ(half - 1);
			merge_occ(sub_result1, result);
			merge_occ(sub_result2, result);
		}
	}
	
	cache[n] = result;
	return result;
}

int main()
{
	// freopen("C-small-1-attempt0.in", "r", stdin);
	// freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("qr_c.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		printf("Case #%d: ", t);
		scanf("%lld %lld", &N, &K);
		
		map<llpair, ll> data_occ = obtain_occ(N);
		
		for (auto entry = data_occ.rbegin(); entry != data_occ.rend(); ++entry) {
			K -= entry->second;
			if (K <= 0) {
				printf("%lld %lld", entry->first.first, entry->first.second);
				break;
			}
		}

		printf("\n");
	}
	return 0;
}
