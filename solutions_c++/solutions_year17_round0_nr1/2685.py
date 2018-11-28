#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

#define IN_FILE "A-large.in"
#define OUT_FILE "outL.txt"

char s1[4000];

int main()
{
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int i, j, t1, t2, t3, t4, t, n, k, f, ans, cnt = 0, l;
	cin >> t;
	while (t--) {
		cin >> s1 >> k;
		l = strlen(s1);
		f = ans = 0;
		for (i = 0; i<l; i++) {
			if (s1[i] == '-') {
				t1 = i + k - 1;
				if (t1 >= l) {
					f = 1;
					break;
				}
				ans++;
				for (j = i; j <= t1; j++) {
					if (s1[j] == '-')
						s1[j] = '+';
					else if (s1[j] == '+')
						s1[j] = '-';
				}
			}
		}
		cnt++;
		if (f == 1)
			cout << "Case #" << cnt << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << cnt << ": " << ans << "\n";
	}
	system("pause");
	return 0;
}
