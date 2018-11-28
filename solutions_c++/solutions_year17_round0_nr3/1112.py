#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long n;
		long long m;
		cin >> n >> m;

		long long a = n / 2;
		long long b = (n - 1) / 2;
		long long aCount = 1;
		long long bCount = 1;
		long long idx = 1;
		long long empties = n;
		while (idx < m) {
			//cout << " IDX : " << idx <<  " , a : " << a << " , b : " << b;
			//cout << " , aCount : " << aCount << " , bCount : " << bCount << endl;;
			if (idx + aCount >= m) {
				empties = a;
				break;
			} else if (idx + aCount + bCount >= m) {
				empties = b;
				break;
			}
			idx += aCount + bCount;

			if (a == b) {
				aCount = bCount = aCount + bCount;
			} else if (a % 2) {
				aCount = aCount * 2 + bCount;
			} else {
				bCount = bCount * 2 + aCount;
			}
			a = a / 2;
			b = (b - 1) / 2;
		}
		a = empties / 2;
		b = (empties - 1) / 2;
		cout << "Case #" << t << ": " << a << " " << b << endl;
	}
}

