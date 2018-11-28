#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <cmath>

#define INF 20000000000000000
#define MOD 1000000007
#define PI acos(-1.0)

using namespace std;

int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum <<": ";
		double arr[50];
		int n, k;
		double u;
		cin >> n >> k >> u;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		sort(arr, arr + n);
		double ans = 1;
		for (int i = 0; i < n; i++)
			ans *= arr[i];
		double tmp[50];
		for (int i = 0; i < n; i++) {
			for (int x = 0; x < n; x++)
				tmp[x] = arr[x];
			double diff = 0;
			for (int j = 0; j <= i; j++) {
				diff += tmp[i] - tmp[j];
			}
			double uu = u - diff;
			if (u >= diff) {
				for (int j = 0; j <= i; j++) {
					tmp[j] = tmp[i];
					tmp[j] = min(1.0, tmp[j] + uu / (i + 1.0));
				}
				double cur = 1.0;
				for (int j = 0; j < n; j++)
					cur *= tmp[j];
				ans = max(ans, cur);
			}
			else {
				break;
			}
		}
		printf("%.9lf\n", ans);
	}
	return 0;
}