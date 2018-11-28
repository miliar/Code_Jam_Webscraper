#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <iterator>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define TASK ""
#define X first
#define Y second
#define inb push_back
#define utp pop_back
#define INF 2e9
#define LING 9e18

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen(TASK".in", "r", stdin);
	freopen(TASK".out", "w", stdout);
#endif
	int t = 0;
	cin >> t;
	int p = 0;
	while (t--)
	{
		string s;
		cin >> s;
		bool f = 0;
		cout << "Case #" << p + 1 << ": ";
		for (int i = 1; i < s.size(); ++i)
			if (s[i] < s[i - 1])
			{
				s[i - 1]--;
				for (int j = i; j < s.size(); ++j) s[j] = '9';
				if (i > 1 && s[i - 2] > s[i - 1])
				{
					int j = i - 2;
					while (j >= 0 && s[j + 1] < s[j])
						s[j + 1] = '9', s[j]--, j--;
				}
				if (s[0] == '0') s = s.substr(1, s.size() - 1);
				cout << s << '\n';
				f = 1;
				break;
			}
		if (!f)
			cout << s << '\n';
		++p;
	}
}