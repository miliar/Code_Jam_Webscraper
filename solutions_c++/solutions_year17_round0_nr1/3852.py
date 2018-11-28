#include <bits/stdc++.h>
using namespace std;

int n;
char s[10000];

int main(){
	int T;
	scanf(" %d", &T);
	
	for (int k = 0; k < T; k++){
		int a[10000] = {0};

		scanf(" %s", s);
		scanf(" %d", &n);
		
		int ans = 0, l = strlen(s);
		for (int i = 0; i < l; i++){
			if (s[i] == '-'){
				if (i + n > l)
					continue;
				for (int j = i; j < i + n; j++){
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
				ans++;
			}
		}

		for (int i = 0; i < l; i++){
			if (s[i] == '-'){
				ans = -1;
				break;
			}
		}

		
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", k + 1);
		else
			printf("Case #%d: %d\n", k + 1, ans);
	}
	return 0;
}
