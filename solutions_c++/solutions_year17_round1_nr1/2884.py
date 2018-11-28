// Round1ProblemA2015.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <iostream>
#define _CRTDBG_MAP_ALLOC  
#include <stdlib.h>  
#include <crtdbg.h>  
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <list>
#include <unordered_map>
#include <stack>
#include <functional>
#include <queue>
#include <math.h>
#include <set>
#include <map>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void printCase(int i) {
	cout << "Case #" << i << ": ";
}


int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		printCase(t);
		//cout.precision(10);

		int R, C;
		cin >> R >> C;
		vector<string> cake(R);
		for (int i = 0; i < R; i++) {
			cin >> cake[i];
		}
		cout << endl;
		map<char, pair < pair<int, int>, pair<int, int >> > cake_map;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (cake[i][j] != '?') {
					if (cake_map.find(cake[i][j]) != cake_map.end()) {
						pair<int, int> pair_1 = cake_map[cake[i][j]].first;
						pair<int, int> pair_2 = cake_map[cake[i][j]].second;
						int min_x = pair_1.first;
						int min_y = pair_1.second;
						int max_x = pair_2.first;
						int max_y = pair_2.second;
						if (i < min_x) {
							min_x = i;
						}
						if (i > max_x) {
							max_x = i;
						}
						if (j > max_y) {
							max_y = j;
						}
						if (j < min_y) {
							min_y = j;
						}
						cake_map[cake[i][j]] = { pair<int, int>(min_x, min_y), pair<int, int>(max_x, max_y) };
					}
					else {
						cake_map[cake[i][j]] = { pair<int, int>(i, j), pair<int, int>(i, j) };
					}
				}
			}
		}

		for (auto elem : cake_map) {
			char initial = elem.first;
			auto pairs = elem.second;

			pair<int, int> pair_1 = pairs.first;
			pair<int, int> pair_2 = pairs.second;

			int min_x = pair_1.first;
			int min_y = pair_1.second;
			int max_x = pair_2.first;
			int max_y = pair_2.second;

			for (int i = min_x; i <= max_x; i++) {
				for (int j = min_y; j <= max_y; j++) {
					cake[i][j] = initial;
				}
			}
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (cake[i][j] == '?') {
					for (auto& elem : cake_map) {
						char initial = elem.first;
						auto pairs = elem.second;
						pair<int, int> pair_1 = pairs.first;
						pair<int, int> pair_2 = pairs.second;

						int min_x = pair_1.first;
						int min_y = pair_1.second;
						int max_x = pair_2.first;
						int max_y = pair_2.second;

						if (i < min_x) {
							min_x = i;
						}
						if (i > max_x) {
							max_x = i;
						}
						if (j > max_y) {
							max_y = j;
						}
						if (j < min_y) {
							min_y = j;
						}

						bool good = true;
						for (auto elem2 : cake_map) {
							if (elem2 != elem) {
								auto pairs2 = elem2.second;
								pair<int, int> pair2_1 = pairs2.first;
								pair<int, int> pair2_2 = pairs2.second;

								int min2_x = pair2_1.first;
								int min2_y = pair2_1.second;
								int max2_x = pair2_2.first;
								int max2_y = pair2_2.second;


								if (min2_x >= min_x && min2_y >= min_y && min2_x <= max_x && min2_y <= max_y) {
									good = false;
								}
								else {
									
								}
								if (max2_x >= min_x && max2_y >= min_y && max2_x <= max_x && max2_y <= max_y) {
									good = false;
								}
							}
						}

						if (!good) {
							continue;
						}
						for (int ii = min_x; ii <= max_x; ii++) {
							for (int jj = min_y; jj <= max_y; jj++) {
								cake[ii][jj] = initial;
							}
						}

						elem.second = { pair<int, int>(min_x, min_y), pair<int, int>(max_x, max_y) };
						break;
					}
				}
			}
		}
		for (auto elem : cake) {
			cout << elem << endl;
		}
	}

	return 0;
}
