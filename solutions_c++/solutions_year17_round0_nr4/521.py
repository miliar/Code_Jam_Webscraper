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
char a[101][101];
int main()
{
	//freopen("D-small-attempt2.in", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		for (int j = 0; j < 101; j++)
			for (int q = 0; q < 101; q++)
				a[j][q] = '.';
		cout << "Case #" << i + 1 << ": ";
		int n, m;
		cin >> n >> m;
		bool flag = false;
		int y = -1;
		vector <pair<int, int>> r[3];
		for (int i = 0; i < m; i++) {
			char q;
			int w, e;
			cin >> q >> w >> e;
			if (q == 'o')
				flag = true;
			if (q == 'x')
				y = e-1;
			a[w - 1][e - 1] = q;
		}
		if (!flag) {
			if (y != -1) {
				a[0][y] = 'o';
				r[2].push_back(make_pair(1, y+1));
			}
			else {
				a[0][0] = 'o';
				r[2].push_back(make_pair(1, 1));
			}
		}
		for (int j = 0; j < n; j++)
			if (a[0][j] != 'o')
				if (a[0][j] == '.') {
					a[0][j] = '+';
					r[0].push_back(make_pair(1, j + 1));
				}
		if (a[0][0] == 'o') {
			int k = n-1;
			for (int j = n-1; j >= 0; j--)
				if (a[0][j] != 'o') {
					a[k][j] = 'x';
					r[1].push_back(make_pair(k + 1, j + 1));
					k--;
				}
		}
		else {
			int k = n - 1;
			for (int j = 0; j < n; j++)
				if (a[0][j] != 'o') {
					a[k][j] = 'x';
					r[1].push_back(make_pair(k + 1, j + 1));
					k--;
				}
		}
		for (int j = 1; j < n - 1; j++)
			if (a[n-1][j] == '.') {
				a[n-1][j] = '+';
				r[0].push_back(make_pair(n, j + 1));
			}
		int answer = 0;
		for (int j = 0; j < n; j++)
			for (int q = 0; q < n; q++)
				if (a[j][q] == '+' || a[j][q] == 'x')
					answer++;
				else if (a[j][q] == 'o')
					answer += 2;
		cout << answer << ' ' << r[0].size() + r[1].size() + r[2].size() << "\n";
		for (int j = 0; j < r[0].size(); j++)
			cout << "+ " << r[0][j].first << ' ' << r[0][j].second << "\n";
		for (int j = 0; j < r[1].size(); j++)
			cout << "x " << r[1][j].first << ' ' << r[1][j].second << "\n";
		for (int j = 0; j < r[2].size(); j++)
			cout << "o " << r[2][j].first << ' ' << r[2][j].second << "\n";
	}
	return 0;
}