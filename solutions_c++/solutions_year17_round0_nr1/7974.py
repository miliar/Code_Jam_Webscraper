#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include <string>
#include <cstdio>
#include <set>
#include <deque>
using namespace std;


int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, ans, k;
	string s;
	bool flag;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> s>>k;
		cout << "Case #" << i << ": ";

		ans = 0;
		flag = true;

		for (int j = 0; j < s.length(); j++) {

			if (s[j] == '-') {

				if (s.length() - j < k) {
					cout << "IMPOSSIBLE" << endl;
					flag = false;
					break;
				}
				
				for (int ind = j + 1; ind < j + k; ind++)
					if (s[ind] == '-')
						s[ind] = '+';
					else
						s[ind] = '-';

				ans++;
			}

		}

		if (flag)
		 cout << ans << endl;
	}

	return 0;
}

