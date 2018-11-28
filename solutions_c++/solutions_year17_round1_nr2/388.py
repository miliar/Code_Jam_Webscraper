#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <memory.h>

using namespace std;



int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, p;
		cin >> n >> p;
		vector<long long> r(n);
		for (int i = 0; i < n; i++) {
			cin >> r[i];
		}
		vector<vector<long long> > q(n, vector<long long>(p));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				cin >> q[i][j];
			}
			sort(q[i].begin(), q[i].end());
		}

		vector<int> curp(n);
		int ans = 0;

		vector<long long> mi(n), ma(n);
		for (int i = 1; i <= 1000000; i++) {
			bool allOk = true;
			for (int j = 0; j < n; j++) {
				long long need = r[j] * i;
				ma[j] = need * 110 / 100;
				mi[j] = (need * 90 + 99) / 100;

				while (curp[j] < p && q[j][curp[j]] < mi[j]) {
					curp[j]++;
				}
				allOk = allOk && curp[j] < p && q[j][curp[j]] <= ma[j];
			}

			while (allOk) {
				ans++;
				for (int j = 0; j < n; j++) {
					curp[j]++;
					allOk = allOk && curp[j] < p && q[j][curp[j]] <= ma[j];
				}
			}
		}

		cout << "Case #" << test << ": " << ans << endl;
	}


	//system("pause");
	return 0;
}