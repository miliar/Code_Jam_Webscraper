#pragma comment(linker, "/STACK:100000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <stdio.h>
#include <set>
#include <queue>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <list>
#include <functional>
#include <unordered_set>
#include <unordered_map>
using namespace std;
int main()
{
	//freopen("A-large (1).in", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		long long D, n;
		cin >> D >> n;
		vector <long long> a(n);
		vector <long long> b(n);
		for (int j = 0; j < n; j++)
			cin >> a[j] >> b[j];
		long double r = 10e18;
		long double l = 0;
		long double mid;
		while (r / l > 1.00000001) {
			mid = (r + l) / 2;
			bool flag = true;
			for (int j = 0; j < n; j++)
				if (mid != b[j] && mid*(a[j] + 0.0) / (mid - b[j]) < D && mid*(a[j] + 0.0) / (mid - b[j]) > 0)
					flag = false;
			if (!flag)
				r = mid;
			else l = mid;
		}
		cout << fixed << setprecision(7);
		cout << r << endl;
	}
	return 0;
}