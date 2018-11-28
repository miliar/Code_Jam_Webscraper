#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <stack>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

LL n;
int a[25], b[25], ans[25], tot;

void Solve() {
	for(int i = 1; i <= tot; i++) {
		if(b[i] < b[i - 1]) {
			int pos = i;
			while(b[pos] - 1 < b[pos - 1]) pos--;
			for(int j = 1; j < pos; j++) ans[j] = b[j];
			ans[pos] = b[pos] - 1;
			for(int j = pos + 1; j <= tot; j++) ans[j] = 9;
			bool flag = 0;
			for(int j = 1; j <= tot; j++) {
				if(!flag) {
					if(ans[j] != 0) flag = 1, printf("%d", ans[j]);
				}
				else printf("%d", ans[j]); 
			}
			printf("\n");
			return;
		}
	}
	for(int i = 1; i <= tot; i++) printf("%d", b[i]);
	printf("\n");
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%lld", &n);
		tot = 0;
		while(n != 0) {
			a[++tot] = int(n % 10);
			n /= 10;
		}
		for(int i = 1; i <= tot; i++) b[i] = a[tot + 1 - i];
		b[0] = 0;
		printf("Case #%d: ", ++cas);
		Solve();
	}
	fclose(stdin);
	fclose(stdout);
}
