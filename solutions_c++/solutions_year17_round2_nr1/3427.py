#define _CRT_SECURE_NO_WARNINGS


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map> //C++11
using namespace std;

typedef long long ll;

int t;
int d, n;
int k[1001], s[1001];
double max_t;

int main() {
	cin >> t;
	for (int time = 1; time <= t; time++) {
		max_t = 0;
		cin >> d >> n;
		for (int i = 0; i < n; i++) {
			cin >> k[i] >> s[i];
			if (max_t < (double)(d - k[i]) / s[i]) {
				max_t = (double)(d - k[i]) / s[i];
			}
		}
		printf("Case #%d: %f\n", time, d/max_t);
	}
	return 0;
}

/*
#define R 1
#define O 2
#define Y 3
#define G 4
#define B 5
#define V 6

int t;
int n, r, o, y, g, b, v, res;

int main() {
	cin >> t;
	for (int time = 0; time < t; time++) {
		cin >> n >> r >> o >> y >> g >> b >> v;
		res = n;
	}

	return 0;
}

bool search(int c) {
	if (res == 0) {

	}
}
*/