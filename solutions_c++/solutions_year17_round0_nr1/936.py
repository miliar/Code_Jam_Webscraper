#include<bits/stdc++.h>
using namespace std;
char ch[10000];
int main(){
	freopen("A_large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);
	int T;
	cin>>T;
	for(int ii = 1; ii <= T; ii++){
		int n, k;
		scanf("%s%d",ch + 1, &k);
		n = strlen(ch + 1);
		int ans = 0;
		for(int i = 1; i <= n; i++)
			if(ch[i] == '-'){
				if(i + k - 1 <= n){
					ans++;
					for(int j = 0; j < k; j++)
						if(ch[i+j] == '-') ch[i+j] = '+';
							else ch[i+j] = '-';
				}else ans = -1;
			}
		printf("Case #%d: ", ii);
		if(ans == -1) puts("IMPOSSIBLE");
			else cout<<ans<<endl;
	}
}
