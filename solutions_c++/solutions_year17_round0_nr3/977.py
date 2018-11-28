#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;

template<class T> inline
void read(T& x) {
	int f = 1; x = 0;
	char ch = getchar();
	while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
	while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
	x *= f;
}

/*============ Header Template ============*/

const int N = 1000 + 5;

LL n, k;

set<LL> S;
map<LL, LL> mp;

int main() {
	int T;
	read(T);
	for (int id = 1; id <= T; id++) {
		read(n), read(k);
		LL L;
		S.clear(); S.insert(n);
		mp.clear(); mp[n] = 1;
		while (!S.empty()) {
			auto it = S.end(); it--;
			LL p = *it; S.erase(it);
			if (k - mp[p] <= 0) {L = p; break;}
			else k -= mp[p];
			// printf("%d\n", p);
			LL len = (p + 1) / 2;
			mp[len - 1] += mp[p];
			mp[p - len] += mp[p];
			S.insert(len - 1);
			S.insert(p - len);
			// S.insert(node(len - 1, p.l));
			// S.insert(node(p.w - len, p.l + len));
		}
		// printf("L = %d\n", L);
		LL tmp1 = (L + 1) / 2 - 1;
		LL tmp2 = L - (L + 1) / 2;
		if (tmp1 < tmp2) swap(tmp1, tmp2);
		cerr << id << endl;
		printf("Case #%d: %lld %lld\n", id, tmp1, tmp2);
	}
	return 0;
}