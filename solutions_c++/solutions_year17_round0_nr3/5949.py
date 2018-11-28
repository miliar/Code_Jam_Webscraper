#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
#define LL long long
typedef pair<int, int>ii;
typedef pair<ii, int> iii;
#define N 1009
int tc, tcn;
LL n, k,re,le[N],ri[N],p[N];
vector<iii> v;

void solve() {
	scanf("%d", &tc);
	while (tc--) {
		scanf("%lld %lld", &n, &k);
		for (int i = 1; i <= n; i++) {
			le[i] = i;
			ri[i] = n+1 - i;
		}
		memset(p, 0, sizeof(p));
		for (int i = 1; i <= k; i++) {
			v.clear();
			for (int j = 1; j <= n; j++) {
				if (p[j])
					continue;
				v.push_back(iii(ii(-min(le[j], ri[j]), -max(le[j], ri[j])), j));
			}
			sort(v.begin(), v.end());
			int cur = (*v.begin()).second;
			p[cur] = k;
			if (k == i) {
				printf("Case #%d: %d %d\n", ++tcn, -(*v.begin()).first.second-1, -(*v.begin()).first.first-1);
				break;
			}
			
			for (int j = 1; j <= n; j++) {
				if (p[j])
					continue;
				if (cur < j && (j-cur) < le[j]) 
					le[j] = j - cur;
				if (j < cur && (cur - j) < ri[j])
					ri[j] = cur - j;
			}
		}
	}
}

int main(void) {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	solve();
	return 0;
}