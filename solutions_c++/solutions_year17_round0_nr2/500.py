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
	//freopen("B-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": ";
		string n;
		cin >> n;
		int k = n.length() - 1;
		while (k >= 0) {
			int j = k-1;
			while (j >= 0 && n[j] <= n[j + 1])
				j--;
			if (j < 0)
				goto L;
			n[j]--;
			k = j;
			j++;
			while (j < n.length()) {
				n[j] = '9';
				j++;
			}
		}
		L: int q = 0;
		while (n[q] == '0')
			q++;
		cout << n.substr(q) << "\n";
	}
	return 0;
}