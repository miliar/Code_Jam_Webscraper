#include <bits/stdc++.h>

using namespace std;

const int LEN = 1010;

int tc, k, len, ans;
char s[LEN];
bool ok;

int main(){
	scanf("%d\n", &tc);
	for(int t = 1; t <= tc; t++){
		ok = true;
		ans = 0;
		scanf("%s %d\n", s, &k);
		len = strlen(s);
		for(int i = 0; i + k <= len; i++)
			if( s[i] == '-' ){
				ans++;
				for(int j = i; j < i + k; j++)
					if( s[j] == '-' ) s[j] = '+';
					else s[j] = '-';
			}
		for(int i = 0; i < len; i++) if( s[i] == '-' ) ok = false;
		if( ok ) printf("Case #%d: %d\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return(0);
}
