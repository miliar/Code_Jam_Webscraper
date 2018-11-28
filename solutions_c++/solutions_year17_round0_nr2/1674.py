#include <bits/stdc++.h>
using namespace std;
typedef long long int LL;

LL f[21][11]; char str[21];

inline void update(LL &a, LL b){if(a < b) a = b;}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int testcase, kase = 0, n, i, j, k;
	LL cur, sum;
	scanf("%d", &testcase);
	while(testcase --){
		scanf("%s", str + 1);
		n = strlen(str + 1);
		for(i = 1; i <= n; ++ i) str[i] -= '0';
		memset(f, -1, sizeof(f));
		for(i = 1; i < str[1]; ++ i)
			f[1][i] = i;
		for(i = 1, sum = str[1]; i < n; ++ i){
			for(k = 1; k < 10; ++ k)
				update(f[i + 1][k], k);
			for(j = 1; j < 10; ++ j){
				if((cur = f[i][j]) == -1LL) continue;
				for(k = j; k < 10; ++ k)
					update(f[i + 1][k], cur * 10LL + k);
			}
			for(j = str[i]; j < str[i + 1]; ++ j)
				update(f[i + 1][j], sum * 10LL + j);
			if(str[i] <= str[i + 1]) sum = sum * 10LL + str[i + 1];
			else sum = -1;
		}
		for(i = 1; i < 10; ++ i)
			sum = max(sum, f[n][i]);
		printf("Case #%d: %lld\n", ++ kase, sum);
	}
	return 0;
}
