#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

char s[1100];
int a[1100];

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc) {
		int k;
		scanf("%s%d", s, &k);
		int l = strlen(s);
		for(int i = 0; i < l; ++i) {
			if(s[i] == '+') a[i] = 1;
			else a[i] = 0;
		}
		int ans = 0;
		for(int i = 0; i < l - k + 1; ++i) {
			if (a[i] == 0) {
				ans++;
				for(int j = 0; j < k; ++j) {
					a[i + j] = 1 - a[i + j];
				}
			}
		}
		for(int i = 0; i < l; ++i) {
			if(a[i] == 0) ans = -1;
		}
		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", cc);
		} else {
			printf("Case #%d: %d\n", cc, ans);
		}
	}
	return 0;
}

