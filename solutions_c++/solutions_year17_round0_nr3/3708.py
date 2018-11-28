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
	for (int test = 0; test < tests; test++) {
		long long n, k;
		cin >> n >> k;
		map<long long, long long> mp;
		mp[-n] = 1;
		int y, z;
		while (k > 0) {
			long long cur = -mp.begin()->first;
			long long cnt = mp.begin()->second;
			mp.erase(mp.begin());
			if (cnt >= k) {
				y = (cur) / 2;
				z = (cur - 1) / 2;
				break;
			}
			else {
				k -= cnt;
				mp[-((cur - 1) / 2)] += cnt;
				mp[-(cur / 2)] += cnt;
			}
		}


		cout << "Case #" << test + 1 << ": " << y << " " << z << endl;
	}


	//system("pause");
	return 0;
}