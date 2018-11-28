#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <cctype>
#include <utility>
#include <exception>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

class Round1A {
public:
	bool checkvertical(vector<string>& cake, int col, int n, int s, char name) {
		for (int r = n+1; r < s; ++r) {
			if (cake[r][col] != '?') {
				return false;
			}
		}
		for (int r = n+1; r < s; ++r) {
			cake[r][col] = name;
		}
		return true;
	}
	void greedy(vector<string>& cake, int row, int col) {
		// vertical
		int n, s, e ,w;
		for (n = row-1; n >=0; --n) {
			if (cake[n][col] == '?') {
				cake[n][col] = cake[row][col];
			}
			else {
				break;
			}
		}
		for (s = row + 1; s < (int)cake.size(); ++s) {
			if (cake[s][col] == '?') {
				cake[s][col] = cake[row][col];
			}
			else {
				break;
			}
		}
		// horizon
		for (w = col - 1; w >= 0; --w) {
			if (!checkvertical(cake, w, n, s, cake[row][col])) {
				break;
			}
		}

		for (e = col + 1; e < (int)cake[row].size(); ++e) {
			if (!checkvertical(cake, e, n, s, cake[row][col])) {
				break;
			}
		}


	}
	void printCake(vector<string> cake) {
		// check for 1
		unordered_set<char> visit;
		visit.insert('?');

		for (int col = (int)cake[0].size() - 1; col >= 0; --col) {
			for (int row = (int)cake.size() - 1; row >= 0; --row) {
				if (visit.count(cake[row][col]) == 0) {
					// new char
					greedy(cake, row, col);
					visit.insert(cake[row][col]);
				}
			}
		}
		for (int r = 0; r < (int)cake.size(); ++r) {
			cout << cake[r] << endl;
		}
	}
};

int main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	cin.ignore();
	Round1A round1;
	int row = 0;
	int col = 0;
	for (int i = 1; i <= t; ++i) {
		cin >> row >> col;
		cin.ignore();
		string line;
		vector<string> cake;
		for (int r = 0; r < row; ++r) {
			getline(cin, line);
			cake.push_back(line);
		}
		cout << "Case #" << i << ": " << endl;
		round1.printCake(cake);
	}
}
