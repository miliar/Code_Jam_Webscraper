// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <cstring>
using namespace std;
#define MX 20
int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		long long n, k;
		cin >> n >> k;
		long long cnt[2] = { 0,0 }, cur = n, ret[2] = { 0,0 };
		for (long long c = 0; c < k; c = (c+1)*2-1) {
			cur = (n - c) / (c + 1);
			cnt[0] = (n-c) % (c + 1);
			cnt[1] = c+1 - cnt[1];
			if (cnt[0] >= k - c) {
				ret[1] = cur / 2;
				ret[0] = cur - ret[1];
			}
			else {
				ret[1] = (cur - 1) / 2;
				ret[0] = cur - 1 - ret[1];
			}
		}


		cout << "Case #" << c << ": ";
		cout << ret[0] << " " << ret[1] << endl;
	}

    return 0;
}

