#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair

int main(){	
	char s[1004];
	int t,k,caso = 1;
	scanf("%d",&t);
	while(t--){
		scanf("%s",s);
		scanf("%d",&k);
		int n = strlen(s), ans = 0;
		for(int i = 0; i <= n - k; i++){
			if(s[i] == '-'){
				ans++;
				for(int j = i; j < i + k; j++){
					s[j] = s[j] == '-' ? '+' : '-';
				}
			}
		}
		int f = 1;
		for(int i = 0; i < n; i++){
			if(s[i] == '-') f = 0;
		}
		printf("Case #%d: ",caso);
		caso++;
		if(!f) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
return 0;
}