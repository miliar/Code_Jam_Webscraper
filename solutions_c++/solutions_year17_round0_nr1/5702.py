#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define eps 1e-9

typedef long long ll;

const int INF = 0x7fffffff;
const int maxn = 1e3 + 10;
int T, K, len;
char str[maxn];
int num[maxn];

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    int kase = 0;
    while (T--) {
    	printf("Case #%d: ", ++kase);
    	scanf("%s %d", str, &K); len = strlen(str);
    	bool flag = true; int ans = 0;
    	for (int i = 0; i < len; ++i) {
    		if (str[i] == '+') { continue; }
    		if (i + K > len) { flag = false; break; }
    		++ans;
    		for (int j = i; j < i + K; ++j) {
				if (str[j] == '-') { str[j] = '+'; }
				else { str[j] = '-'; }
			}
		}
		if (flag) { printf("%d\n", ans); }
		else { printf("IMPOSSIBLE\n"); }
	}
    return 0;
}
