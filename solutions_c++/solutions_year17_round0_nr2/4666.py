#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<list>
#include <algorithm>
#include<string>
#include<stdlib.h>
#pragma warning(disable:4996)
using namespace std;

int main() {
	int  t, i1 = 0;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A.txt", "w", stdout);
	cin >> t;
	while (t--) {
		i1++;
		int i, j;
		int k, l, count = 0, n, m;
		string s, s1, s2;
		cin >> s;
		n = s.size();
		for (i = 0; i < n; i++)
			s1.push_back(s[0]);
		s2 = s1;
		int flag = 0;
		while (flag == 0) {
			if (atoll(s2.c_str()) == atoll(s.c_str()))
				break;
			if (atoll(s.c_str()) > atoll(s2.c_str())) {
				for (j = s2[0] - '0'; j < 9; j++) {
					s1 = s2;
					n = s1.size();
					for (i = n - 1; i > 0; i--) {
						s1[i] = s1[i] + 1;
						if (atoll(s1.c_str()) > atoll(s.c_str())) {
							flag = 1;
							break;
						}
						else
							s2 = s1;
					}
				}
				if (j == 9)
					flag = 1;
			}
			if (atoll(s2.c_str()) > atoll(s.c_str())) {
				if (s2[0] == '1')
				{
					s2[0] = '9';
					for (i = 2; i < n; i++)
						s2[i - 1] = '9';
					s2.pop_back();
				}
				else
				{
					s2[0] = s2[0] - 1;
					for (i = 1; i < n; i++)
						s2[i] = s2[0];
				}


			}

		}
		cout << "Case #" << i1 << ": " << s2 << endl;
	}

	return 0;
}
