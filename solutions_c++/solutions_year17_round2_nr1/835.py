#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <set>

#define INF 2000000000

using namespace std;

struct horse {
	int index;
	long long x;
	long long v;
};

int main() {
	int testCnt;
	cin >> testCnt;
	horse arr[1000];
	int n;
	long long d;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		cin >> d >> n;
		for (int i = 0; i < n; i++) {
			cin >> arr[i].x >> arr[i].v;
		}
		long long maxIndex = 0;
		for (int i = 1; i < n; i++) {
			if ((d - arr[maxIndex].x) * arr[i].v < (d - arr[i].x) * arr[maxIndex].v) {
				maxIndex = i;
			}
		}
		printf("%.9lf\n", 1.0 * d * arr[maxIndex].v / (d - arr[maxIndex].x));
	}
	return 0;
}