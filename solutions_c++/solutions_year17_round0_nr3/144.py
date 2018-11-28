#include <bits/stdc++.h>
#define intl long long
using namespace std;

struct cmp {
	bool operator () (intl a, intl b) {
		return (a > b);
	}
};

map<intl, intl, cmp> st;

int T, t_;
int top, ans;
intl n, k;
intl val[1010000], cnt[1010000];

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		scanf("%lld %lld",&n,&k);
		st.clear();
		top = 0;
		st[n] = 1LL;		
		while (st.begin() -> first > 0LL) {
			auto u = st.begin();
			st[u -> first / 2LL] = st[u -> first / 2LL] + u -> second;
			st[(u -> first - 1LL) / 2LL] = st[(u -> first - 1LL) / 2LL] + u -> second;
			val[++top] = u -> first;
			cnt[top] = u -> second;
			st.erase(st.begin());			
		}
		for (ans = 1; cnt[ans] < k; k -= cnt[ans++]);
		printf("Case #%d: %lld %lld\n",++t_, val[ans] / 2LL, (val[ans] - 1LL) / 2LL);
	}
	return 0;
}
