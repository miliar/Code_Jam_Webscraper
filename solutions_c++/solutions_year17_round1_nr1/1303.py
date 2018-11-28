#define  _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream> 
#include<map>
#include <iomanip>
#include <time.h>
#include <random>
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#define LONG_INF 10000000000000000
#define MAX_MOD 1000000007
#define REP(i,n) for(long long i = 0;i < n;++i)
int main() {
	int t;
	cin >> t;
	REP(test_case, t) {
		int a, b;
		cin >> a >> b;
		vector<string> hoge;
		REP(i, a) {
			string s;
			cin >> s;
			hoge.push_back(s);
		}
		int grid[30][30] = {};
		for (int i = 0;i < a;++i) {
			for (int q = 0;q < b;++q) {
				if (hoge[i][q] != '?') {
						grid[i][q] = hoge[i][q] - 'A';
				}
				else {
					grid[i][q] = 50;
				}
			}
		}
		for (int i = 0;i < a;++i) {
			for (int q = 0;q < b;++q) {
				if (grid[i][q] == 50) {
					if (q != 0) {
						grid[i][q] = grid[i][q-1];
					}
				}
			}
		}
		for (int i = 0;i < a;++i) {
			for (int q = b - 1;q >= 0;--q) {
				if (grid[i][q] == 50) {
					if (q != b - 1) {
						grid[i][q] = grid[i][q + 1];
					}
				}
			}
		}
		for (int i = 1;i < a;++i) {
			for (int q = 0;q < b;++q) {
				if (grid[i][q] == 50) {
					grid[i][q] = grid[i - 1][q];
				}
			}
		}
		for (int i = a - 2;i >= 0;--i) {
			for (int q = 0;q < b;++q) {
				if (grid[i][q] == 50) {
					grid[i][q] = grid[i + 1][q];
				}
			}
		}
		vector<string> ans;
		REP(i, a) {
			string s;
			for (int q = 0;q < b;++q) {
				s.push_back(grid[i][q] + 'A');
				if (grid[i][q] == 50) {
					cout << "ERROR" << endl;
					return 0;
				}
			}
			ans.push_back(s);
		}
		cout << "Case #" << test_case + 1 << ":" << endl;
		for (int i = 0;i < a;++i) {
			cout << ans[i] << endl;
		}
	}
}