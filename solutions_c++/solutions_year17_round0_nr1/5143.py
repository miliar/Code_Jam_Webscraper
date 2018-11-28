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

int k;
char s[1005];

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%s", s);
		scanf("%d", &k);
		int len = strlen(s);
		int ans = 0; 
		for(int i = 0; i <= len - k; i++) {
			if(s[i] == '-') {
				for(int j = 0; j < k; j++) 
					if(s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				ans++;
			}
		}
		bool ok = 1;
		for(int i = 0; i < len; i++) 
			if(s[i] == '-') ok = 0;
		printf("Case #%d: ", ++cas);
		if(ok) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	fclose(stdin);
	fclose(stdout);
}
