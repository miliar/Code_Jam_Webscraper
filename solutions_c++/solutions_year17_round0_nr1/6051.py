#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007

char s[1004];
int k;

int main(){
//ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

// freopen("in.txt","r",stdin);
// freopen("out.txt","w",stdout);

int T;
cin >> T;
for(int t = 1; t <= T; t++){
	scanf("%s", s + 1);
	scanf("%d", &k);
	int n = strlen(s + 1);

	int ans = 0;
	for(int i = 1; (i + k - 1) <= n; i++){
		if(s[i] == '+') continue;
		ans++;
		for(int j = 0; j < k; j++){
			int pos = i + j;
			s[pos] = (s[pos] == '+' ? '-' : '+');
		}
	}
	for(int i = 1; i <= n; i++){
		if(s[i] == '-'){
			ans = -1;
			break;
		}
	}
	printf("Case #%d: ", t);
	if(ans == -1)printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);
}
return 0;
}