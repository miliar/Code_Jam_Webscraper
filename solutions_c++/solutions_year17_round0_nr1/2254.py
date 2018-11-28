#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
 
int main() {  
	freopen("in.txt", "r", stdin);
 	freopen("out.txt", "w", stdout);
	char ipt[1003];
	int T, len, K, ans, num;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf(" %s %d", ipt, &K);
		len = strlen(ipt);
		num = 0; ans = 0;
		for (int i = 0; i < len; i++) {
			if (ipt[i] == '-') num++;
		}
		for (int i = 0; i < len; i++) {
			if (ipt[i] == '-') {
				ans++;
				if (i + K - 1 >= len) {
					num = 1000; 
					break;
				}
				for (int j = 0; j < K; j++) {
					if (ipt[i + j] == '-') {
						ipt[i + j] = '+'; 
						num--;
					}
					else {
						ipt[i + j] = '-';
						num++;
					}
				}
			}
		} 

		if (num != 0) printf("Case #%d: IMPOSSIBLE\n", t + 1);
		else printf("Case #%d: %d\n", t + 1, ans);
	}
  	return 0;
}
