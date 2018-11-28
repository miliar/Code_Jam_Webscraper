#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
const int maxn = 1100;
int n, k;
int a[maxn];
char tmp[maxn];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%s %d", tmp, &k);
		n = strlen(tmp);
		for(int i = 0; i < n; i++) {
			a[i] = (tmp[i] == '+') ? 1 : 0;
		}
		int ret = 0;
		for(int i = 0; i < n - k + 1; i++) {
			if(a[i] == 0) {
				ret++;
				for(int j = i; j < i + k; j++) {
					a[j] = 1 - a[j];
				}
			}
		}
		cout << "Case #" << _++ << ": ";
		bool ok = 1;
		for(int i = 0; i < n; i++) {
			if(a[i] == 0) ok = 0;
		}
		if(!ok) puts("IMPOSSIBLE");
		else printf("%d\n", ret);
	}
	return 0;
}