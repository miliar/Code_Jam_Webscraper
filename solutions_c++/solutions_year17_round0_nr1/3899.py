#include<bits/stdc++.h>
using namespace std;

int T, n, k;
char s[1100];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		printf("Case #%d: ", t);
		scanf("%s%d", s, &k);
		int n = strlen(s);
		bool flag = 1;
		int cnt = 0;
		for(int i = 0; i < n; ++i){
			if(s[i] == '-'){
				if(i > n - k) { flag = 0; break; }
				for(int j = i; j < i + k; ++j)
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				cnt++;
			}
		}
		if(flag) printf("%d\n", cnt);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
