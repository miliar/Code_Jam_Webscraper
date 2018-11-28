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
int k;
string s;
bool f[1010];

int main() {
	scanf("%d", &TC);
	rep(tc, TC) {
		cin >> s >> k;
		int n = s.size();
		rep(i, n) f[i] = (s[i] == '+');

		int ret = 0;
		for (int i = 0; i <= n - k; ++i) {
			if (!f[i]) {
				for (int j = i; j < i + k; ++j) {
					f[j] ^= 1;
				}
				++ret;
			}
		}

		bool ok = 1;
		rep(i, n) if (!f[i]) ok = 0;

		printf("Case #%d: ", tc + 1);
		if (ok) printf("%d\n", ret);
		else puts("IMPOSSIBLE");
	}
	return 0;
}