#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string.h>
#include <memory.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <bitset>

#define F first
#define S second
#define MP make_pair

typedef long long ll;

using namespace std;

double const PI = acos(-1);
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };
// int dx[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
// int dy[] = { 1, 0, -1, 0, 1, -1, -1, 1 };

long long gcd(long long a, long long b) {
	return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b) {
	return a * (b / gcd(a, b));
}

vector<pair<int, int> > arr;
vector<int> indexes;
double res;
int n, k;

void trY(int index) {
	if(index == n) {
		if(indexes.size() == k) {
			double tmp = (PI * arr[indexes[0]].first * arr[indexes[0]].first);

			for(int i = 0; i < indexes.size(); ++i)
				tmp += (2 * PI * arr[indexes[i]].first * arr[indexes[i]].second);

			res = max(res, tmp);

			return;
		}

		return;
	}

	if(indexes.size() == k) {
		double tmp = (PI * arr[indexes[0]].first * arr[indexes[0]].first);

		for(int i = 0; i < indexes.size(); ++i)
			tmp += (2 * PI * arr[indexes[i]].first * arr[indexes[i]].second);

		res = max(res, tmp);

		return;
	}

	trY(index + 1);

	indexes.push_back(index);
	trY(index + 1);
	indexes.pop_back();
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	int a, b, c = 0;
	while(t-- != 0) {
		scanf("%d%d", &n, &k);
		arr.clear();
		arr.resize(n);
		for(int i = 0; i < n; ++i)
			scanf("%d%d", &arr[i].first, &arr[i].second);

		sort(arr.begin(), arr.end());
		reverse(arr.begin(), arr.end());

		indexes.clear();
		res = 0;
		trY(0);
		printf("Case #%d: %.9lf\n", ++c, res);
	}

  return 0;
}
