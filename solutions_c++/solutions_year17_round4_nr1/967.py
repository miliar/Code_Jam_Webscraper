#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int n, p;
		cin >> n >> p;
		vector <int> m(p, 0);
		int g;
		for (int i = 0; i < n; i++){
			cin >> g;
			m[g%p]++;
		}
		if (p == 4){
			int t1 = min(m[1], m[3]);
			m[0] += t1;
			m[1] -= t1;
			m[3] -= t1;
			t1 = max(m[1], m[3]);
			m[2] += t1 / 2;
			m[0] += m[2] / 2;
			if (t1 % 2 > 0 || m[2] % 2 > 0) m[0]++;
		}
		else if (p == 3){
			int t1 = min(m[1], m[2]);
			m[0] += t1;
			m[1] -= t1;
			m[2] -= t1;

			t1 = max(m[1], m[2]);
			m[0] += (t1 / 3);
			if (t1 % 3) m[0]++;
		}
		else if (p == 2){
			m[0] += m[1] / 2;
			if (m[1] % 2) m[0]++;
		}

		cout << "Case #" << z << ": " << m[0] << endl;
	}
	return 0;
}