#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
#include<stdlib.h>
#include<bitset>
#include<algorithm>
using namespace std;
#define ll long long
vector<pair<int, int> >v;
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // !ONLINE_JUDGE
	int t,d,n;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%d%d", &d, &n);
		v.resize(n);
		double slow = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &v[i].first, &v[i].second);
			double dis = (double)d - v[i].first;
			double ti = dis / v[i].second;
			slow = max(slow, ti);
		}
		double ans = d / slow;
		printf("Case #%d: %.6lf\n", i, ans);
		v.clear();
	}
}