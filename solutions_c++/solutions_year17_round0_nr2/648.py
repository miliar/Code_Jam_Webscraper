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
char str[32];

void input() {
	scanf("%s", str);
}

void solve() {
	int last = 1;
	while(last < strlen(str)&&str[last] >= str[last-1]) ++ last;
	if(last >= strlen(str)) {
		printf(" %s\n", str);
		return ;
	}

	int first = last-1;
	for(int i = last-1;i >= 0;i --) if(str[i] == str[last-1]) first = i;
	for(int i = first+1;i < strlen(str);i ++) str[i] = '9';
	-- str[first];

	if(str[first] == '0') printf(" %s\n", str+first+1);
	else printf(" %s\n", str);

	/*long long dp[10][30];
	for(int i = 0;i < 10;i ++) dp[i][1] = 1;
	dp[0][1] = 0;
	for(int i = 2;i <= strlen(str);i ++) for(int j = 0;j < 10;j ++) {
		dp[j][i] = 0;
		for(int k = j;k < 10;k ++) dp[j][i] += dp[k][i-1];
	}

	int pre = 0;
	long long res = 0;
	for(int i = 0;i < strlen(str);i ++) {
		int val = str[i]-'0';
		for(int j = pre;j < val;j ++) res += dp[j][strlen(str)-i];
		//printf("#%d %d\n", i, res);
		if(val >= pre) pre = val;
		else break;
	}
	int ok = 1;
	for(int i = 1;i < strlen(str);i ++) if(str[i] < str[i-1]) ok = 0;
	if(ok) ++ res;
	printf(" %lld\n", res);*/
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
