#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000;

const int N = 4;

vector <pair <long long, long long> > spaces;


int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;

	int t;
	cin >> t;
	for (int it = 0; it < t; it++) {
		cout << "Case #" << it + 1 << ": ";
		spaces.clear();
		long long n;
		long long k;
		cin >> n >> k;
		spaces.push_back(make_pair(n, 1));
		int d = 0;
		while (k > 0) {
			// cout << "k = " << k << endl;
			// cout << "spaces = ";
			// for (int i = 0; i < spaces.size(); i++)
			// 	cout << "(" << spaces[i].first << ", " << spaces[i].second << ") ";
			// cout << endl;
			// cout << "d = " << d << endl;
			if (spaces[d].second >= k) {
				cout << spaces[d].first / 2 << " " << (spaces[d].first - 1) / 2 << endl;
				break;
			} else {
				k -= spaces[d].second;
				if (spaces[d].first % 2 == 1) {
					bool flag = false;
					for (int i = 1; d + i < spaces.size(); i++) {
						if (spaces[d + i].first == spaces[d].first / 2) {
							spaces[d + i].second += spaces[d].second * 2;
							flag = true;
							break;
						}
					}
					if (!flag)
						spaces.push_back(make_pair((spaces[d].first - 1) / 2, spaces[d].second * 2));
				} else {
					bool flag = false;
					for (int i = d + 1; i < spaces.size(); i++) {
						if (spaces[i].first == spaces[d].first / 2) {
							spaces[i].second += spaces[d].second;
							flag = true;
							break;
						}
					}
					if (!flag)
						spaces.push_back(make_pair((spaces[d].first / 2), spaces[d].second));
					flag = false;
					for (int i = d + 1; i < spaces.size(); i++) {
						if (spaces[i].first == spaces[d].first / 2 - 1) {
							spaces[i].second += spaces[d].second;
							flag = true;
							break;
						}
					}
					if (!flag)
						spaces.push_back(make_pair(spaces[d].first / 2 - 1, spaces[d].second));
				}
			}
			d++;
		}
	}

	return 0;
}