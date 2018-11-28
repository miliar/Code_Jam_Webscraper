#include <bits/stdc++.h>
using namespace std;

int tcn, n, k, ans;
char str[1010];

void fl(int x){
	ans++;
	for(int i = x; i < x + k; i++) str[i] ^= 1;
}

int main(){
	freopen("Al.in", "r", stdin);
	freopen("Al.out", "w", stdout);
	scanf("%d", &tcn); for(int tc = 1; tc <= tcn; tc++){
		scanf("%s%d", str, &k);
		for(n = 0; str[n]; n++) str[n] = (str[n] == '+');
		ans = 0;
		for(int i = 0; i <= n - k; i++){
			if(!str[i]) fl(i);
		}
		printf("Case #%d: ", tc);
		for(int i = 0; i <= n; i++){
			if(i == n){ printf("%d\n", ans); break; }
			if(!str[i]){ puts("IMPOSSIBLE"); break; }
		}
	}
}
