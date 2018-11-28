#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	cout.precision(7);
	for (int t = 1; t <= T; t++) {

		int d, n;
		cin >> d >> n;
		int x[1010], v[1010];
		double xx = 0;
		for (int i = 0; i < n; i++) {
			cin >> x[i] >> v[i];
			xx = max(xx, 1. * (d - x[i]) / v[i]);
		}
		
		cout << fixed << "Case #" << t << ": " << d / xx << endl;
	}
	return 0;
}
