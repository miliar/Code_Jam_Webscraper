// 1a1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;



int main()
{
	ifstream cin("C://Users//shicheng//Desktop//A-large.in");
	ofstream cout("C://Users//shicheng//Desktop//A-large.out");
	int t;
	int r, c;
	cin >> t;
	for (int num = 1; num <= t; ++num) {
		cin >> r >> c;
		vector<vector<char>> vec(r, vector<char>(c, 0));
		vector<pair<int, int>> c_vec;
		char ch;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cin >> ch;
				if (ch != '?') {
					c_vec.push_back(pair<int, int>(i, j));
				}
				vec[i][j] = ch;
			}
		}
		for (int k = 0; k < c_vec.size(); ++k) {
			int x = c_vec[k].first;
			int y = c_vec[k].second;
			ch = vec[x][y];
			int min = y, max = y;
			for (int i = 1; i < c; ++i)
			{
				if (y - i >= 0 && vec[x][y - i] == '?') {
					vec[x][y - i] = ch;
					min = y - i;
				}
				else {
					break;
				}
			}
			for (int i = 1; i < c; ++i)
			{
				if (y + i < c && vec[x][y + i] == '?') {
					vec[x][y + i] = ch;
					max = y + i;
				}
				else {
					break;
				}
			}
			bool check = true;
			for (int i = 1; i < r; ++i)
			{
				if (!check)
				{
					break;
				}
				if (x - i >= 0) {
					for (int j = min; j <= max; ++j) {
						if (vec[x - i][j] != '?') {
							check = false;
							break;
						}
					}
				}
				else {
					check = false;
				}
				if (check) {
					for (int j = min; j <= max; ++j) {
						vec[x - i][j] = ch;
					}
				}
			}
			check = true;
			for (int i = 1; i < r; ++i)
			{
				if (!check)
				{
					break;
				}
				if (x + i < r) {
					for (int j = min; j <= max; ++j) {
						if (vec[x + i][j] != '?') {
							check = false;
							break;
						}
					}
				}
				else {
					check = false;
				}
				if (check) {
					for (int j = min; j <= max; ++j) {
						vec[x + i][j] = ch;
					}
				}
			}
		}
		cout << "Case #" << num << ":" << endl;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j) {
				cout << vec[i][j];
			}
			cout << endl;
		}
	}
    return 0;
}