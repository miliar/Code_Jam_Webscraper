#pragma warning(disable:4996)

#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <climits>
#include <string>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int test;
	int n, d, di, speed;
	double time,max = 0.0,fs;
	scanf("%d", &test);
	for (int test_i = 1; test_i <= test; test_i++) {
		printf("Case #%d: ", test_i);
		//enter here
		max = 0;
		scanf("%d%d", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &di, &speed);
			di = d - di;
			time = (double)di / speed;
			if (time > max) {
				max = time;
			}
		}
		printf("%lf\n", d / max);
	}
	return 0;
}