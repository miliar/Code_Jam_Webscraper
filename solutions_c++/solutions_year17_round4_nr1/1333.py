#include <bits/stdc++.h>

using namespace std;

int cnt[5];

int P[3];

int check() {
	int cur = cnt[1] / 4 + cnt[2] / 2 + cnt[3] / 4;
	
	int a = cnt[1] % 4, b = cnt[2] % 2, c = cnt[3] % 4;
	
	if (a + b + c > 0) cur++;
	return cur;
}

int main() {
	int t;
	scanf("%d", &t);
	
	for (int test = 1; test <= t; test++) {
		int n, p;
		scanf("%d %d", &n, &p);
		
		fill(cnt, cnt + 5, 0);
		
		for (int i = 0; i < n; i++) {
			int t;
			scanf("%d", &t);
			cnt[t % p]++;
		}
		
		int ans;
		if (p == 2) {
			ans = cnt[0] + (cnt[1] + 1) / 2;
		} else if (p == 3) {
			
			ans = cnt[0];
			
			int q = min(cnt[1], cnt[2]);
			ans += q;
			cnt[1] -= q, cnt[2] -= q;
			
			int t = cnt[1] + cnt[2];
			
			ans += t / 3 + (t % 3 > 0);
		} else {
			ans = cnt[0];
			
			int cur = 0;
		
			int c1 = min(cnt[1] / 2, cnt[2]);
			
			for (int a = 0; a <= c1; a++) {
				
				cnt[1] -= 2 * a;
				cnt[2] -= a;
				
				int c2 = min(cnt[2], cnt[3] / 2);
				
				for (int b = 0; b <= c2; b++) {
					cnt[2] -= b;
					cnt[3] -= 2 * b;
					
					int c3 = min(cnt[1], cnt[3]);
					
					for (int c = 0; c <= c3; c++) {
						cnt[1] -= c;
						cnt[3] -= c;
						
						cur = max(cur, a + b + c + check());
						
						cnt[1] += c;
						cnt[3] += c;
					}
					cnt[2] += b;
					cnt[3] += 2 * b;
				}
				cnt[1] += 2 * a;
				cnt[2] += a;
			}
			ans += cur;
		}
		
		printf("Case #%d: %d\n", test, ans);
	}
	
	return 0;
}
