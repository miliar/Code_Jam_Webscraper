// BathroomStalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <tuple>

using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int n, k;
		cin >> n >> k;

		vector<bool> v;
		while (k != 1) {
			if (k % 2 == 0) v.push_back(false);
			else v.push_back(true);
			k = k / 2;
		}
		tuple<int, int> vals(n / 2, (n - 1) / 2);
		for (int j = 0; j < v.size(); j++) {
			if (!v[j]) {
				int a = get<0>(vals);
				vals = tuple<int, int>(a / 2, (a - 1) / 2);
			}
			else {
				int a = get<1>(vals);
				vals = tuple<int, int>(a / 2, (a - 1) / 2);
			}
		}
		cout << "Case #" << (i+1) << ": " << get<0>(vals) << " " << get<1>(vals) << endl;
	}
    return 0;
}

