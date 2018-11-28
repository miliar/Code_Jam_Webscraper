#include <bits/stdc++.h>

using namespace std;

#define N 100
#define P 4

int g[N + 1];
int c[P + 1];
int n, p;

bool comp(int a, int b){
	return a % p < b % p;
}

int main(){
	int ans, cur, tc, ic, i;
	
	scanf("%d", &tc);
	
	for (ic = 1; ic <= tc; ic++){
		scanf("%d%d", &n, &p);

		for (i = 0; i < n; i++){
			scanf("%d", g + i);

			c[g[i] % p]++;
		}

		if (p == 2){
			ans = c[0] + (c[1] + 1) / 2;
		}
		else if (p == 3){
			cur = min(c[1], c[2]);

			ans = c[0] + cur;

			c[1] -= cur;
			c[2] -= cur;

			ans += (c[1] + c[2] + 2) / 3;
		}
		else{
			cur = min(c[1], c[3]);

			// 0 Ok
			// 1 with 3 Ok
			ans = c[0] + cur;

			c[1] -= cur;
			c[3] -= cur;

			// 2 with 2 Ok
			cur = c[2] / 2;

			ans += cur;

			c[2] -= 2 * cur;

			cur = c[1] + c[3];

			if (c[2]){
				if (cur >= 2){
					ans++;
					cur -= 2;
					ans += (cur + 3) / 4;
				}
				else{
					ans++;
				}
			}
			else{
				ans += (cur + 3) / 4;
			}
		}
		
		printf("Case #%d: %d\n", ic, ans);

		memset(c, 0, sizeof(c));
	}

	return 0;
}