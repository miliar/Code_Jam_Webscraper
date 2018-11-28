#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdio>
#include <sstream>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		
		string s;
		int fpos = -1;
		cin >> s;
		string res = s;
		for (int i = 0; i < s.size() - 1; i++) 
			if (s[i] > s[i + 1]) {
				fpos = i;
				while (fpos >= 1 && s[fpos] == s[fpos - 1])
					fpos--;
				break;
			}
		if (fpos != -1) {
			res[fpos]--;
			for (int i = fpos + 1; i < res.size(); i++)
				res[i] = '9';
			if (res[0] == '0')
				res = res.substr(1);
		}

		cout << "Case #" << c + 1 << ": " << res << endl;
	}
	return 0;
}
