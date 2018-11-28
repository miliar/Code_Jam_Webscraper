// Khaled Alam - KhaledAlam.net
// Google Code Jam 2017 | Problem B
#include <bits/stdc++.h>
using namespace std;

long long tests, n;

string run(long long x) {
	if (x < 10)return to_string(x);
	stringstream ss;
	string s, result;
	string::iterator start, end;
	ss << x, ss >> s;
	const unsigned long long len = (unsigned long long) s.length();
	for (unsigned long long j = len - 1ull; j > 0ull; j--) {
		if (s[j - 1ull] > s[j]) {
			for (unsigned long long k = j; k < len && s[k] != '9'; k++)s[k] = '9';
			s[j - 1ull] = s[j - 1ull] - 1;
		}
	}
	start = s.begin();
	while ((*start) == '0')start++;
	end = s.end();
	result.assign(start, end);
	return result;
}

int main() {
	freopen("data.in", "r", stdin);
//	freopen("data.out", "w", stdout);

//	brute(0, '0');

	cin >> tests;
	for (long long t = 1; t <= tests; ++t) {
		cin >> n;
		cout << "Case #" << t << ": " << run(n) << '\n';
	}

}

//Bruteforce
//set<long long> sot;
//map<short, bool> vis;
//
//string s;
//
//void brute(int idx, char prev) {
//
//	if (idx >= 10) {
//		cout << s << endl;
//		return;
//	}
//	for (int i = idx; i < 10; ++i) {
//		for (char k = '1'; k <= '9'; ++k) {
//			if (k >= prev) {
//				s.push_back(k);
//				brute(i+1, k);
//				s.pop_back();
//			}
//		}
//	}
//}
