#include <bits/stdc++.h>
using namespace std;
const int N = 1000 + 5;
int n;
char str[N];
int a[N];
int len;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++ cas){
		memset(a, 0, sizeof(a));
		scanf("%s%d", str, &n);
		len = strlen(str);
		for(int i = 0; i < len; ++ i){
			a[i] = str[i] == '+' ? 0 : 1;
		}
		int ans = 0;
		for(int i = 0; i < len-n+1; ++ i){
			if(a[i] == 1){
				++ ans;
				for(int j = i; j < i + n; ++ j){
					a[j] ^= 1;
				}
			}
		}
		int flag = 0;
		for(int i = len-n+1; i < len; ++ i){
			if(a[i] == 1){
				flag = 1;
			}
		}
		printf("Case #%d: ", cas);
		if(flag) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}
