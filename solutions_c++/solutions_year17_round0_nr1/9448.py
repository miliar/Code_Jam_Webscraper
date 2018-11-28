#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <math.h>
#include <unordered_map>
#include <vector>
#include <queue>
using namespace::std;


int main() {
	freopen("A-large2017.in", "r", stdin);
	freopen("A-large2017.out", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int sum = 0;
		int i = 0;
		for (; i<s.length(); i++) {
			if (s[i] == '-') {
				// cout<<i<<" ";
				if (i + k - 1 >= s.length())
					break;
				sum++;
				for (int j = i; j<i + k; j++) {
					s.replace(j, 1, (s[j] == '-' ? "+" : "-"));
				}
			}
		}
		cout << "Case #" << tt << ": ";
		if (i == s.length())
			cout << sum;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}