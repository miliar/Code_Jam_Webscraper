#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <cstring>
using namespace std;

int T, D, n;

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		scanf("%d %d", &D, &n);
		double max_hours = 0;
		for (int i = 0; i < n; i++) {
			int x, s;
			scanf("%d %d", &x, &s);
			max_hours = max(max_hours, 1.0 * (D - x) / s);
		}
		printf("Case #%d: %.9lf\n", it, D / max_hours);
	}
	return 0;
}