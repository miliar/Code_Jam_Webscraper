//Author: net12k44

#include <bits/stdc++.h>
using namespace std;
char s[100000];
int a[100000];

void solve(){
	int n, k;
	scanf("%s",s); scanf("%d",&k);
	n = strlen(s);
	for(int i = 0; i < n; ++i)
		a[i] = (s[i] == '-') ? 1 : 0;	
	
	int res = 0;
	for(int i = 0; i+k <= n; ++i)
		if (a[i] == 1){
			for(int j = i; j < i+k; ++j)
				a[j] ^= 1;
			res++;
		}
		
	for(int i = 0; i < n; ++i)
		if (a[i])
			res = -1;
		
	if (res < 0)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", res);
	
}

int main(){
	freopen("file.out","w",stdout);
	
	int test; scanf("%d",&test);
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}