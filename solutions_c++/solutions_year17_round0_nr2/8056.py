#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int n, m, i, j, T, ti, ans;
int s[20];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	for (ti = 1; ti <= T; ++ti) {
		string str;
		cin >> str;
		n = str.length();
		for (i = 0; i < n; ++i) 
			s[i] = str[i] - '0';
		bool flag = true;
		while (flag) {
			for (i = 0; i < n - 1; ++i) 
				if (s[i] > s[i + 1]) {
					s[i]--;
					for (j = i + 1; j < n; ++j) 
						s[j] = 9;
				}
			flag = false;
			for (i = 0; i < n - 1; ++i) 
				if (s[i] > s[i + 1]) 
					flag = true;
		}
		printf("Case #%d: ", ti);
		i = 0;
		while (s[i] == 0) i++;
		for (; i < n; ++i) 
			cout << s[i];
		cout << endl;
	}
	return 0;
}