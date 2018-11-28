#include <stdio.h>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
#ifndef WIN32
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif // !WIN32
	int tc;
	scanf("%d", &tc);
	int tc_o = tc;
	while (tc--) {
		char ps[1010];
		int k;
		scanf("%s %d", &ps, &k);
		int i = 0, l = strlen(ps);
		int cnt = 0;
		while (i < l-k+1) {
			if (ps[i] == '-') {
				cnt++;
				for (int j = 0; j < k; j++) {
					if (ps[i + j] == '-') ps[i + j] = '+';
					else ps[i + j] = '-';
				}
			}
			while (ps[i] == '+') i++;
		}
		bool ch = true;
		while (i < l) {
			if (ps[i] == '-') ch = false;
			i++;
		}
		if(ch) printf("Case #%d: %d\n", tc_o - tc,cnt);
		else printf("Case #%d: IMPOSSIBLE\n", tc_o - tc);
		/*
		vector<int> res(k, 0);
		int l = strlen(ps);

		for (int i = 0; i < l; i++) {
			if (ps[i] == '-') res[i%k]++;
		}
		*/
	}
	return 0;
}