#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>
typedef long long ll;
using namespace std;
const int N = 20;
char str[N];
ll add9(ll v, int n) {
	while (n--) 
		v = v * 10 + 9;
	return v;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int cas=1;cas<=t;++cas) {
		printf("Case #%d: ", cas);
		scanf("%s", str);
		int n = strlen(str);
		ll k = 0;
		ll mx = 0;
		char last = '0';
		bool can = true;
		for (int i = 0; i < n; ++i) {
			for (int j = last; j < str[i]; ++j) {
				ll tmp = k * 10 + (j - '0');
				mx = max(mx, add9(tmp, n - i - 1));
			}
			if (last > str[i]) {
				can = false;
				break;
			}
			last = str[i];
			k = k * 10 + (str[i] - '0');
		}
		if (can)
			mx = max(mx, k);
		printf("%lld\n", mx);


	}


	return 0;
}
