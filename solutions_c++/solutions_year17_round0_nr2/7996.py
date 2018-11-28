#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <sstream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <stack>
using namespace std;

vector<int> d;
vector<int> newd;

int main() {
	int t;
	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		d.clear(); newd.clear();
		long long n;
		cin >> n;
		long long tmp = n;
		// cout << "number: " << tmp << endl;
		while (tmp) {
			d.push_back(tmp % 10);
			tmp /= 10;
		}
		// // DEBUG
		// cout << "its digits are: " << endl;
		// for (int i = 0; i < d.size(); i++) {
		// 	cout << d[i] << " ";
		// }
		// cout << endl;
		bool carry = false;
		for (int i = 0; i < d.size(); i++) {
			// cout << "on digit " << d[i] << endl;
			if (i != d.size()-1) {
				int cur = d[i];
				int prv = d[i+1];
				if (carry) {
					cur--;
				}
				if (cur >= prv && cur != 0) {
					newd.push_back(cur);
					// cout << "adding to newdigit " << cur << endl;
					carry = false;
				} else {
					newd.push_back(9);
					for (int i = 0; i < newd.size(); i++) {
						newd[i] = 9;
					}
					// cout << "adding to newdigit " << 9 << endl;
					carry = true;
				}
			} else {
				int cur = d[i];
				if (carry) {
					cur--;
				}
				if (cur > 0) {
					// cout << "adding to newdigit " << cur << endl;
					newd.push_back(cur);
				}
			}
		}
		long long res = 0;
		for (int i = 0; i < newd.size(); i++) {
			res = res*10 + newd[newd.size()-1-i];
		}
		cout << "Case #" << tc+1 << ": " << res << endl;
	}
}















