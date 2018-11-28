#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

void solve(int test)
{
	printf("Case #%d: ", test + 1);

	string s;
	cin >> s;

	forn(i, (int)s.size() - 1)
	{
		if (s[i + 1] < s[i])
		{
			int j = i;
			while (j > 0 && (s[j] == '0' || s[j] == s[j-1])) j--;
			s[j]--;
			for (int k = j + 1; k < (int)s.size(); k++) s[k] = '9';
			if (s[0] == '0')
			{
				s = s.substr(1, s.size());
			}
			cout << s << endl;
			return;
		}
	}
	cout << s << endl;
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; cin >> tc;
	forn(it, tc) solve(it);

	return 0;
}
