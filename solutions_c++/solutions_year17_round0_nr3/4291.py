// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int t;

int main()
{
	cin >> t;
	for (int testcase = 0; testcase < t; testcase++) {
		long long n, k;
		cin >> n >> k;
		map<long long, long long> state;
		vector<long long> pile;
		state[n] = 1;
		pile.push_back(n);
		long long nb = 0;
		long long res = 0;
		while (1) {
			long long cur = pile[pile.size() - 1];
			while (pile[pile.size() - 1] == cur) {
				pile.pop_back();
				if (pile.size() == 0) {
					break;
				}
			}
			long long curState = state[cur];
			nb += curState;
			if (nb >= k) {
				res = cur;
				break;
			}
			long long nextA, nextB;
			if (cur % 2 == 0) {
				nextA = (cur / 2) - 1;
				nextB = cur / 2;
			}
			else {
				nextA = (cur - 1) / 2;
				nextB = (cur - 1) / 2;
			}
			state[nextA] += curState;
			state[nextB] += curState;
			pile.push_back(nextA);
			pile.push_back(nextB);
			sort(pile.begin(), pile.end());
		}
		long long curMax, curMin;
		long long LS, RS;
		if (res % 2 == 0) {
			LS = (res / 2) - 1;
			RS = res / 2;
		}
		else {
			LS = (res - 1) / 2;
			RS = (res - 1) / 2;
		}
		curMax = max(LS, RS);
		curMin = min(LS, RS);
		cout << "Case #" << testcase + 1 << ": " << curMax << " " << curMin << endl;
	}
	return 0;
}