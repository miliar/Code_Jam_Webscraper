#include <bits/stdc++.h>
using namespace std;

const int N = 1010;

char s[N];

int main(){
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++){
		int k;
		scanf("%s %d", s, &k);
		
		bool ok = true;
		int n = strlen(s), cnt = 0;
		for(int l = 0; l < n; l++){
			if(s[l] == '-'){
				int r = l + k - 1;
				if(r >= n){
					ok = false;
					break;
				}
				for(int i = l; i <= r; i++){
					s[i] = (s[i] == '+')? '-' : '+';
				}
				cnt++;
			}
		}
		printf("Case #%d: ", tc);
		if(ok) printf("%d\n", cnt);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
