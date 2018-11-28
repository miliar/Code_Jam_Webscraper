#include <bits/stdc++.h>

using namespace std;

#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair< b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};

#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

const int nax = 105;
int dp[nax][nax][nax][4];
const int inf = 1e9 + 5;

void maxi(int & a, int b) {
	a = max(a, b);
}

void test_case() {
	int n, p;
	scanf("%d%d", &n, &p);
	vector<int> cnt(4, 0);
	for(int i = 0; i < n; ++i) {
		int x;
		scanf("%d", &x);
		++cnt[x%p];
	}
	for(int i = 0; i <= cnt[1]; ++i)
		for(int j = 0; j <= cnt[2]; ++j)
			for(int k = 0; k <= cnt[3]; ++k)
				for(int r = 0; r < 4; ++r)
					dp[i][j][k][r] = -inf;
	dp[0][0][0][0] = cnt[0];
	for(int i = 0; i <= cnt[1]; ++i)
		for(int j = 0; j <= cnt[2]; ++j)
			for(int k = 0; k <= cnt[3]; ++k)
				for(int r = 0; r < p; ++r) {
					int me = dp[i][j][k][r];
					debug() << imie(i) << imie(j) << imie(k) << imie(r) << "val = " << me;
					if(me < 0) continue;
					for(int a = 1; a < p; ++a) {
						int r2 = (a + r) % p;
						maxi(dp[i+(a==1)][j+(a==2)][k+(a==3)][r2], me + (r == 0));
					}
				}
	int answer = 0;
	for(int r = 0; r < 4; ++r)
		maxi(answer, dp[cnt[1]][cnt[2]][cnt[3]][r]);
	assert(1 <= answer && answer <= n);
	printf("%d\n", answer);
}

int main(int argc, char * argv[]) {
	int T;
	scanf("%d", &T);
	for(int nr = 1; nr <= T; ++nr) {
		printf("Case #%d: ", nr);
		test_case();
	}
}
