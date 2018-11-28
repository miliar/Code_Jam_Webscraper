#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
const int maxn = 32;
char s[maxn];
int n;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%s", s);
		cout << "Case #" << _++ << ": ";
		bool ok = 1;
		n = strlen(s);
		for(int i = 0; i < n - 1; i++) {
			if(s[i] > s[i+1]) {
				ok = 0;
				break;
			}
		}
		if(ok) puts(s);
		else {
			bool done = 1;
			int pos = 1;
			while(1) {
				for(int i = 0; i < n; i++) {
					if(s[i] < s[i-1]) {
						done = 0;
						pos = i;
						s[pos-1]--;
						for(int j = pos; j < n; j++) s[j] = '9';
						break;
					}
				}
				if(done) break;
				done = 1;
			}
			int p = 0;
			while(s[p] == '0') p++;
			puts(s+p);
		}
	}
	return 0;
}