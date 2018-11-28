#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <ctime>
using namespace std;

void solve()
{
	string s;
	cin >> s;
	for (int i = s.size() - 1; i > 0; --i)
	{
		if (s[i] < s[i - 1]) {
			--s[i - 1];
			for (int j = i; j < s.size(); ++j)
				s[j] = '9';
		}
	}
	while (s[0]=='0')
	{
		s = s.substr(1);
	}
	cout << s << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		clock_t start = clock();
		printf("Case #%d: ", test);
		solve();
		clock_t finish = clock();
		cerr << "Test" << test << ": " << (finish - start + .0) / CLOCKS_PER_SEC << endl;
	}
	

	return 0;
}