/* ***********************************************
 	Author        : luckcul
 	Mail          : tyfdream@gmail.com
 	Created Time  : 2017-04-08 16:22:51
 	Problem       : problem
************************************************ */
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define INF 1000000000
//typedef __int64 LL;
#define N 1123
int t, k;
char ch[N];
int check() {
	int len = strlen(ch);
	int ret = 0;
	for(int i = 0; i < len - k+1; i++){
		if(ch[i] == '+') continue;
		ret ++;
		for(int j = i; j < i+k; j++) {
			if(ch[j] == '+') ch[j] = '-';
			else ch[j] = '+';
		}
	}
	for(int i = 0; i < len ;i++) {
		if(ch[i] == '-') {
			ret = -1; break;
		}
	}
	return ret;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif // ONLINE_JUDGE
	scanf("%d", &t);
	for(int ti = 0; ti < t; ti ++) {
		scanf("%s", ch);
		scanf("%d", &k);
		int ans = check();
		printf("Case #%d: ", ti+1);
		if(ans < 0) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}

	return 0;
}
