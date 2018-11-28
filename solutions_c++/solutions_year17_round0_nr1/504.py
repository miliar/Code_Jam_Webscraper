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
	//freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": ";
		string n;
		int q;
		cin >> n >> q;
		int k = 0;
		int answer = 0;
		while (k < n.length()-q+1) {
			while (k < n.length() && n[k] == '+')
				k++;
			if (k >= n.length() - q + 1)
				break;
			for (int j = k; j < k+q; j++)
				if (n[j] == '+')
					n[j] = '-';
				else n[j] = '+';
			answer++;
			k++;
			bool flag = false;
			for (int j = 0; j < n.length(); j++)
				if (n[j] == '-')
					flag = true;
			if (!flag)
				break;
		}
		bool flag = false;
		for (int j = 0; j < n.length(); j++)
			if (n[j] == '-')
				flag = true;
		if (!flag)
			cout << answer << "\n";
		else cout << "IMPOSSIBLE" << "\n";
	}
	return 0;
}