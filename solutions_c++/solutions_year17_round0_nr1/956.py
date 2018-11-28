/*cf handle: visitR*/

#include <bits/stdc++.h>
using namespace std;

#define pi acos(-1)
#define inf (1 << 30)
#define linf (1llu << 60)

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vp;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;

int main() {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; ++t) {
		char str[1111];
		int k;
		scanf("%s%d", str, &k);
		int len = strlen(str);
		vi arr;
		for (int i=0; i<len; ++i)
			arr.push_back((str[i]=='-' ? 1 : 0));
		vi flag(2, 0);
		int sum[2];
		for (int z=0; z<2; ++z) {
			vi x(len, 0);
			int curr = 0, i = 0;
			while (i < k && i+k-1 < len) {
				x[i] = curr ^ arr[i];
				curr ^= x[i];
				++i;
			}
			while (i+k-1 < len) {
				curr ^= x[i-k];
				x[i] = curr ^ arr[i];
				curr ^= x[i];
				++i;
			}
			while (i < len) {
				if (i >= k)
					curr ^= x[i-k];
				if (curr != arr[i]) {
					flag[z] = 1;
					break;
				}
				++i;
			}
			sum[z] = accumulate(x.begin(), x.end(), 0);
			for (int i=0; i<len/2; ++i) {
				swap(arr[i], arr[len-i-1]);
			}
		}
		printf("Case #%d:", t);
		if (flag[0] == 1 && flag[1] == 1) {
			printf(" IMPOSSIBLE\n");
			continue;
		}
		int ans = inf;
		if (flag[0] == 0)
			ans = min(ans, sum[0]);
		if (flag[1] == 0)
			ans = min(ans, sum[1]);
		printf(" %d\n", ans);
	}
	return 0;
}