#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

char st[10500];

int main(){
    freopen("A-large.in","rt",stdin);
	freopen("A-large.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		int k;
		scanf("%s%d", st, &k);
		int n = strlen(st);
		int ans = 0;
		for (int i = 0; i < n; i++) if (st[i] == '-'){
			if (i + k > n){
				ans = -1;
				break;
			}
			ans++;
			for (int j = 0; j < k; j++) st[i + j] = (st[i + j] == '-') ? '+' : '-';
		}
		if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %d\n", tc, ans);
	}
}
