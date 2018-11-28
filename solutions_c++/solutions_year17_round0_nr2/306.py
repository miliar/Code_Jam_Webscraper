#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long long ll;

int t;
ll n;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		cin >> n;
		stringstream ss; ss << n;
		string s; ss >> s;
		int lst = 0;
		bool was = false;
		for (int i = 1; i < s.length(); i++)
			if (s[i] > s[i - 1]) { lst = i; }
			else if (s[i] < s[i - 1]) { was = true; break; }
		if (was) {
			s[lst]--;
			for (int i = lst + 1; i < s.length(); i++)
				s[i] = '9';
			int pnt = 0;
			while (s[pnt] == '0') pnt++;
			s = s.substr(pnt);
		}
		printf("Case #%d: %s\n", tc, s.c_str());
	}
	return 0;
}