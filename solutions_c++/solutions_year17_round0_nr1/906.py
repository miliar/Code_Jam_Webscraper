#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int T, x, C;
int K;
char s[1002];

void solve() {
	int cnt = 0;
	int len = strlen(s);
	for(int i = 0 ; i < len-K+1 ; ++i) {
		if(s[i] == '-') {
			for(int j = 0 ; j < K ; ++j) {
				s[i+j] = (s[i+j] == '+') ? '-' : '+';
			}
			cnt++;
		}
	}
	bool c = true;
	for(int i = 0 ; i < len ; ++i) if(s[i] == '-') c = false;
	if(!c) printf("IMPOSSIBLE\n");
	else printf("%d\n", cnt);
}

int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%s", s);
		scanf("%d", &K);
		printf("Case #%d: ", ++C);
		solve();
	}
}
