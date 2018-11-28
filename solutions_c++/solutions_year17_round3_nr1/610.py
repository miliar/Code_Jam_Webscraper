#include<cstdio>
#include<algorithm>
#include<limits.h>
#include<string>
#include<vector>
#include<functional>
#include<iostream>
#include<stdlib.h>
#pragma warning(disable : 4996)
#define int long long
#define PI 3.14159265358979323846
#define P pair<int,int>
using namespace std;

P e[1000];
signed main() {
	freopen("X.txt", "w", stdout);
	int a; scanf("%lld", &a);
	for (int b = 0; b < a; b++) {
		int c, d; scanf("%lld%lld", &c, &d);
		for (int f = 0; f < c; f++) {
			scanf("%lld%lld", &e[f].first, &e[f].second);
		}
		int ans = 0;
		for (int f = 0; f < c; f++) {
			vector<int>V;
			for (int g = 0; g < c; g++) {
				if (f == g)continue;
				if (e[g].first <= e[f].first) {
					V.push_back(e[g].second * 2 * e[g].first);
				}
			}
			if (V.size() < d-1)continue;
			sort(V.begin(), V.end(),greater<int>());
			int K = e[f].first*e[f].first;
			K += e[f].second * 2 * e[f].first;
			for (int i = 0; i < d-1; i++) {
				K += V[i];
			}
			ans = max(ans, K);
		}
		printf("Case #%lld: %.20lf\n", b + 1, ans*PI);
	}
}