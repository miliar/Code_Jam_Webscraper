#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> llp;

int main() {
	ll t;
	cin >> t;

	for (ll q = 0; q < t; q++) {
		string s;
		vector<ll> vec;
		cin >> s;
		for (ll i = 0; i < s.length(); i++) {
			vec.push_back(s[i] - '0');
		}

		ll p = 10000;
		for (ll i = vec.size() - 1; i > 0; i--) {
			if (vec[i] < vec[i - 1]) {
				vec[i - 1]--;
				p = i;
			}
		}

		for (ll i = p; i < vec.size(); i++) {
			vec[i] = 9;
		}

		cout << "Case #" << q + 1 << ": ";
		ll k = 0;
		while (k < vec.size() - 1 && vec[k] <= 0) { k++; }
		while (k < vec.size()) { cout << vec[k]; k++; }
		cout << "\n";
	}

	return 0;
}