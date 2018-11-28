#include <iostream>
#include <cstring>

using namespace std;

char s[1005];

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> s+1;
		int n = strlen(s+1);

		int k;
		cin >> k;

		int ans = 0;
		for(int j=1;j<=n-k+1;j++){
			if(s[j] == '+') continue;
			ans++;
			for(int l=j;l<=j+k-1;l++){
				if(s[l] == '-') s[l] = '+';
				else s[l] = '-';
			}
		}

		for(int j=1;j<=n;j++){
			if(s[j] == '-'){
				ans = -1;
				break;
			}
		}

		if(ans == -1) printf("Case #%d: IMPOSSIBLE\n", i);
		else printf("Case #%d: %d\n", i, ans);
	}
}