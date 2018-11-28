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

int N, P;
int matrix[50][50];
int low[50][50], high[50][50];
int target[50];

void input() {
	scanf("%d%d", &N, &P);
	for(int i = 0;i < N;i ++) scanf("%d", &target[i]);
	for(int i = 0;i < N;i ++) for(int j = 0;j < P;j ++) scanf("%d", &matrix[i][j]);
}

void solve() {
	for(int i = 0;i < N;i ++) {
		int *array = matrix[i];
		sort(array, array+P);
	}
	for(int i = 0;i < N;i ++) for(int j = 0;j < P;j ++) {
		low[i][j] = (matrix[i][j]*100 + target[i]*110-1)/(target[i]*110);
		high[i][j] = (matrix[i][j]*100)/(target[i]*90);
	}
	int idx[50];
	for(int i = 0;i < N;i ++) idx[i] = 0;
	int res = 0;
	while(true) {
		int ok = 1;
		for(int i = 0;i < N;i ++) if(idx[i] >= P) ok = 0;
		if(!ok) break;

		ok = 1;
		for(int i = 0;i < N;i ++) if(low[i][idx[i]] > high[i][idx[i]]) {
			++ idx[i];
			ok = 0;
		}
		if(!ok) continue;

		ok = 1;
		for(int i = 0;i < N&&ok;i ++) for(int j = i+1;j < N&&ok;j ++) {
			if(high[i][idx[i]] < low[j][idx[j]]) {
				ok = 0;
				++ idx[i];
			}
			else if(low[i][idx[i]] > high[j][idx[j]]) {
				ok = 0;
				++ idx[j];
			}
		}

		if(ok) {
			++ res;
			for(int i = 0;i < N;i ++) ++ idx[i];
		}
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
