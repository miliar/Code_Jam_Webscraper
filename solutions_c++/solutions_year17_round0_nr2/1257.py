#define _CRT_SECURE_NO_WARNINGS


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map> //C++11
using namespace std;

typedef long long ll;

int t;
ll n;
string s;

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		s = to_string(n);
		for (int i = 1; i < s.length(); i++) {
			if (s.at(i) < s.at(i - 1)) {
				s.at(i - 1) = s.at(i - 1) - 1;
				for (int j = i; j < s.length(); j++) {
					s.at(j) = '9';
				}
				i = 0;
			}
		}
		cout << "Case #" << i << ": " << stoll(s) << endl;
	}
	return 0;
}
