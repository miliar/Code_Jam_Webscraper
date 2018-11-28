#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

void solve(string s) {
	if (is_sorted(s.begin(), s.end())) {
		cout << s;
		return;
	}
	int k = 0;

	while (k < s.size() && s[k] <= s[k+1])
		++k;
	while (k > 0 && s[k - 1] == s[k])
		--k;
	s[k++]--;
	for (; k < s.size(); ++k)
		s[k] = '9';
	while (s[0] == '0')
		s.erase(0, 1);
	cout << s;
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "B"
#define ATTEMPT "0"

#define LARGE
//#define TEST

int main() {
#ifdef LARGE
	freopen(DIR PROBLEM "-large.in", "rt", stdin);
#elif defined(TEST)
	freopen("input.txt", "rt", stdin);
#else
	freopen(DIR PROBLEM "-small-attempt" ATTEMPT ".in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << (i + 1) << ": ";
		solve(s);
		cout << endl;
	}
}
