#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
const int MAXN = 10010, MAXL = 1000010;

char s[1010];
int size, n;

void flip(int index);
bool ok();

int main() {
	// freopen("A-large.in", "r", stdin);
	// freopen("output-large.txt", "w", stdout);

	int t, caso = 0;
	scanf("%d", &t);
	while(t--) {
		caso++;
		scanf("%s %d", s, &n);
		size = strlen(s);

		int ans = 0;
		for(int i=0; i<=size-n; i++) {
			if(s[i] == '-') {
				flip(i);
				ans++;
			}
		}

		printf("Case #%d: ", caso);
		if(ok()) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
}

void flip(int index) {
	for(int i=index; i<index+n; i++) {
		s[i] = s[i] == '-' ? '+' : '-';
	}
}

bool ok() {
	bool ans = true;
	for(int i=0; i<size; i++) {
		if(s[i] == '-') {
			ans = false;
		}
	}
	return ans;
}
