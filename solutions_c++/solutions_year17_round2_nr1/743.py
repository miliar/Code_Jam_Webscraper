#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <numeric>
#include <algorithm>
#include <vector>
#include <map>
#include <random>
#include <cstdio>
#include <cmath>
using namespace std;

string s;
const int MAXN = 4;
char ch;
int tests, test, n, m, x, y;
double C, F, X;
int D;
int N; 
vector<pair<int, int>> horses;

int main() {
	freopen("H:\\Projects\\Codejam2017\\1_in.txt", "r", stdin);
	freopen("H:\\Projects\\Codejam2017\\1_out.txt", "w", stdout);

	scanf("%d", &tests);

	for (test = 1; test <= tests; ++test) {
		scanf("%d %d", &D, &N);
		vector<pair<int, int>> horses = vector<pair<int, int>>(N, { 0, 0 }); 


		for (int i = 0; i < N; ++i) {
			scanf("%d %d", &horses[i].first, &horses[i].second); 
		}

		sort(horses.begin(), horses.end());

		auto &slower = horses[0];
		double ans = D / ((double)(D - slower.first) / slower.second);

		for (int i = 1; i < N; ++i) {
			auto &faster = horses[i];
			if (slower.second <= faster.second) continue; 
			double deltaTime = (double)(faster.first - slower.first) / (slower.second - faster.second);
			if (deltaTime > 0 && deltaTime < (double)(D - faster.first) / faster.second) {
				double meetLocation = (double)slower.first + deltaTime * slower.second;
				double totalTime = deltaTime + (double)(D - meetLocation) / faster.second;
				ans = min(ans, (double)D / totalTime);
				slower = faster; 
			}
		}
		printf("Case #%d: %.6f\n", test, ans);
	}

	return 0;
}
