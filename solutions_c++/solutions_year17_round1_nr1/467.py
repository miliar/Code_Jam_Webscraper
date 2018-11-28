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

char matrix[30][30];
int R, C;

void input() {
	scanf("%d%d", &R, &C);
	for(int i = 0;i < R;i ++) scanf("%s", matrix[i]);
}

void solve() {
	int first = 0;
	for(int i = 0;i < R;i ++) {
		int found = 0;
		for(int j = 0;j < C;j ++) if(matrix[i][j] != '?') found = 1;
		if(found) {
			first = i;
			break;
		}
	}
	for(int i = first;i < R;i ++) {
		char ch = '?';
		for(int j = 0;j < C;j ++) if(matrix[i][j] != '?') {
			ch = matrix[i][j];
			break;
		}
		if(ch == '?') {
			strcpy(matrix[i], matrix[i-1]);
			continue;
		}
		for(int j = 0;j < C;j ++) {
			if(matrix[i][j] != '?') ch = matrix[i][j];
			else matrix[i][j] = ch;
		}
	}
	for(int i = first-1;i >= 0;i --) strcpy(matrix[i], matrix[i+1]);

	printf("\n");
	for(int i = 0;i < R;i ++) printf("%s\n", matrix[i]);
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
