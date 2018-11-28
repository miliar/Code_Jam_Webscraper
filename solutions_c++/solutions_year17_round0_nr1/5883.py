#include <bits/stdc++.h>
using namespace std;
int tc;
int main(){
	scanf("%d", &tc);
	for(int t = 1; t <= tc; ++t){
		int ans = 0;
		string s; int k;
		cin>>s>>k;
		int len = s.length();
		for(int i = 0; i <= len - k; ++i){
			if(s[i] == '-') {
				ans++;
				for(int j = i;j < i + k; ++j){
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		for(int i = len-k+1; i < len && ans != -1; ++i) if(s[i] == '-'){
			ans = -1;
		}
		printf("Case #%d: ", t);
		if(ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
