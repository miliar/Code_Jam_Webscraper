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
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#define LONG_INF 10000000000000000
#define MAX_MOD 1000000007
#define REP(i,n) for(long long i = 0;i < n;++i)
double route[200][200] = {};
double distances[200][200] = {};
double time_todo[200][200] = {};
double gogo[200][200] = {};
int main() {
	int t;
	cin >> t;
	REP(test_case, t) {
		int n, quary;
		cin >> n >> quary;
		vector<pair<double, double>> horses;
		REP(i, n) {
			double a, b;
			cin >> a >> b;
			horses.push_back(make_pair(a, b));
		}
		REP(i, n) {
			REP(q, n) {
				cin >> route[i][q];
			}
		}
		for (int i = 0;i < n;++i) {
			for (int q = 0;q < n;++q) {
				distances[i][q] = 100000000000000;
			}
			distances[i][i] = 0;
		}
		for (int i = 0;i < n;++i) {
			priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> next;
			next.push(make_pair(0, i));
			bool done[200] = {};
			while (next.empty() == false) {
				pair<double, int> now = next.top();
				next.pop();
				if (done[now.second] == false) {
					done[now.second] = true;
					for (int q = 0;q < n;++q) {
						if (route[now.second][q] != -1) {
							if (route[now.second][q] + now.first < distances[i][q]) {
								distances[i][q] = route[now.second][q] + now.first;
								next.push(make_pair(distances[i][q], q));
							}
						}
					}
				}
			}
		}
		for (int i = 0;i < n;++i) {
			for (int q = 0;q < n;++q) {
				if (distances[i][q] > horses[i].first) {
					time_todo[i][q] = 100000000000000;
				}
				else {
					time_todo[i][q] = distances[i][q] / horses[i].second;
				}
			}
		}
		for (int i = 0;i < 200;++i) {
			for (int q = 0;q < 200;++q) {
				gogo[i][q] = 1000000000000000;
			}
			gogo[i][i] = 0;
		}
		for (int i = 0;i < n;++i) {
			priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> next;
			next.push(make_pair(0, i));
			bool done[200] = {};
			while (next.empty() == false) {
				pair<double, int> now = next.top();
				next.pop();
				if (done[now.second] == false) {
					done[now.second] = true;
					for (int q = 0;q < n;++q) {
						if (time_todo[now.second][q] + now.first < gogo[i][q]) {
							gogo[i][q] = time_todo[now.second][q] + now.first;
							next.push(make_pair(gogo[i][q], q));
						}
					}
				}
			}
		}
		cout << "Case #" << test_case + 1 << ":" << fixed << setprecision(10);
		REP(i, quary) {
			int a, b;
			cin >> a >> b;
			cout << " " << gogo[a - 1][b - 1];
		}
		cout << endl;
	}
}