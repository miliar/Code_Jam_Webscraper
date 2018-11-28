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
		int n, k;
		cin >> n >> k;
		pair<long long, long long> arr[1000];
		for (int i = 0; i < n; i++) {
			cin >> arr[i].first >> arr[i].second;
		}
		sort(arr, arr + n);
		reverse(arr, arr + n);
		double tmp[1000];
		double ans = -1;
		for (int i = 0; i <= n - k; i++) {
			double h = PI * arr[i].second * 2 * arr[i].first;
			for (int j = 1; i + j < n; j++) 
				tmp[j - 1] = PI * 2 * arr[i + j].second * arr[i + j].first;
			sort(tmp, tmp + n - 1 - i);
			reverse(tmp, tmp + n - 1 - i);
			for (int j = 0; j < k - 1; j++) 
				h += tmp[j];
			ans = max(ans, PI * arr[i].first * arr[i].first + h);
		}
		printf("%.9lf\n", ans);
	}
	return 0;
}