#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cassert>
#include <functional>
using namespace std;
typedef pair<int, int> PII;
typedef pair<int, PII> PPII;
typedef vector<int> VI;
typedef priority_queue<PPII, vector<PPII>, less<PPII>> PQ;
void TestBathroomStalls() {
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int qq = 0; qq < t; ++qq) {
		int n, k;
		cin >> n >> k;
		PQ pq;
		VI v(n, 0);
		pq.push(make_pair(n, make_pair(0, n - 1)));
		int lst = -1;
		int counter = 0; 
		while (!pq.empty() && counter < k) {
			PPII ppii = pq.top(); pq.pop();
			lst = (ppii.first - 1) / 2 + ppii.second.first;
			if (lst < 0 || lst >= n) continue;
			v[lst] = 1;
			if (ppii.first % 2 == 0) {
				pq.push(make_pair(ppii.first / 2 - 1, make_pair(ppii.second.first, lst - 1)));
			}
			else {
				pq.push(make_pair(ppii.first / 2, make_pair(ppii.second.first, lst - 1)));
			}
			pq.push(make_pair(ppii.first / 2, make_pair(lst + 1, ppii.second.second)));
			counter++;
		}
		int ls = 0, rs = 0;
		for (int i = lst - 1; i >= 0 && v[i] == 0; i--) ls++;
		for (int i = lst + 1; i <= n - 1 && v[i] == 0; i++) rs++;
		int y = max(ls, rs);
		int z = min(ls, rs);
		cout << "Case #" << (qq + 1) << ": " << y << " " << z << "\n";
	}
	fflush(stdout);
}