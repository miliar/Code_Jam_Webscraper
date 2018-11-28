#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<list>
#include <algorithm>
#include<string>
#pragma warning(disable:4996)
using namespace std;

int main() {
	int  t, i1 = 0;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A.txt", "w", stdout);
	cin >> t;
	while (t--) {
		i1++;
		int i, j, k, l, count = 0, n, m;
		string s;
		cin >> s;
		cin >> k;
		n = s.size();
		for (i = 0; i < n; i++)
			if (s[i] == '-') {
				if (k + i <= n) {
					for (j = i; j < k + i; j++)
					{
						if (s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
					}
					count++;
				}
			}
		int flag = 1;
		for (i = 0; i < n; i++)
			if (s[i] == '-')
				flag = 0;
		if (flag == 1)
			cout << "Case #" << i1 << ": " << count << endl;
		else
			cout << "Case #" << i1 << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
