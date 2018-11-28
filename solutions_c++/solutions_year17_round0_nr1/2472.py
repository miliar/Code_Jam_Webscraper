#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef long long ll;
char s[1001];
int k;
char Not(char x) {
	if (x == '-')
		return '+';
	return '-';
}
int calc() {
	int res = 0;
	string cur = s;
	for(int i=0;i<cur.size();++i)
		if (cur[i] == '-') {
			for (int j = 0; j < k; ++j) {
				if (i + j >= cur.size())
					return 1e9;
				cur[i + j] = Not(cur[i + j]);
			}
			++res;
		}
	for (int i = 0; i < cur.size(); ++i)
		if (cur[i] == '-')
			return 1e9;
	return res;
}
int main() {
	freopen("C:/Users/ASUS/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d:", T);
		scanf("%s%d", s, &k);
		int res = calc();
		reverse(s, s + strlen(s));
		res = min(res, calc());
		if (res > 1e7)
			puts(" Impossible");
		else
			printf(" %d\n", res);
	}
	return 0;
}