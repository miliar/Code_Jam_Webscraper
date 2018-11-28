#include <bits/stdc++.h>
using namespace std;
const int inf = 0x7ffffff;
int T, k, ca = 1; char s[55], tmp[55];
inline char flip(char x){
	if(x == '+') return '-';
	else return '+';
}
void mark(int pos) {
	for(int i = 0; i < k; ++i) {
		tmp[pos] = flip(tmp[pos]);
		pos++;
	}
}
bool ok() {
	for(int i = 0; tmp[i]; ++i) {
		if(tmp[i] == '-') return false;
	}
	return true;
}
int main(int argc, const char* agrv[]) {
	//freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--) {
		scanf("%s %d", s, &k);
		int n = strlen(s);
		int up = 1<<(n-k+1), ans = inf;
		for(int i = 0; i < up; ++i) {
			for(int k = 0; k <= n; ++k) tmp[k] = s[k];
			int cnt = 0;
			for(int j = 0; j < n-k+1; ++j) {
				if(i&(1<<j)) {
					mark(j);
					cnt ++;
				}
			}
			if(ok()) {
				ans = min(ans, cnt);
			}
		}
		if(ans == inf) printf("Case #%d: IMPOSSIBLE\n", ca++);
		else printf("Case #%d: %d\n", ca++, ans);
	}
}

