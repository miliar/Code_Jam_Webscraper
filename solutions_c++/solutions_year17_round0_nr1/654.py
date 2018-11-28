/*
 * main.cpp
 *
 *  Created on: 9 Apr 2016
 *      Author: ljchang
 */

#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int K;
char str[1008];

void input() {
	scanf("%s%d", str, &K);
}

void solve() {
	int res = 0;
	for(int i = 0;i + K <= strlen(str);i ++) if(str[i] == '-') {
		++ res;
		for(int j = 0;j < K;j ++) {
			if(str[i+j] == '+') str[i+j] = '-';
			else str[i+j] = '+';
		}
	}
	for(int i = 1;i <= K;i ++) if(str[strlen(str)-i] == '-') {
		printf(" IMPOSSIBLE\n");
		return ;
	}
	printf(" %d\n", res);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 0; cas < t;cas ++) {
		input();
		printf("Case #%d:", cas+1);
		solve();
	}
	return 0;
}
