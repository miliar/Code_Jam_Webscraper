#include <bits/stdc++.h>
using namespace std;

const int N = 1005;
int t, k, c, nc = 1, n;
bool s[N];

int main(){

	scanf("%d%*c", &t);
	while(t--){
		
		n = 0;
		while((c = getchar()) != ' ')
			s[n++] = c == '-';
		
		scanf("%d%*c", &k);		

		int r = 0;
		for(int i = 0; i+k <= n; ++i)
			if(s[i] == 1){
				for(int j = 0; j < k; ++j)
					s[i+j] ^= 1; 
				r++;
			}

		bool ok = true;
		for(int i = 0; i < n; ++i)
			ok &= (not s[i]);

		if(not ok) printf("Case #%d: IMPOSSIBLE\n", nc++);		
		else printf("Case #%d: %d\n", nc++, r);
	}

	return 0;
}
