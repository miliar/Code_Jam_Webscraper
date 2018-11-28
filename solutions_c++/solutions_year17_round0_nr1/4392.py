#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>

using namespace std;

#define mp(a, b) make_pair(a,b)


void f()
{
	string s;
	cin >> s;
	int n = s.size();
	int k;
	cin >> k;
	int cnt = 0;
	for (int i = 0;i < n - k+1;i++)
	{
		if (s[i]=='+')
		{
			continue;
		}
		cnt++;
		for (int j = 0;j < k;j++)
		{
			if (s[i+j]=='+')
			{
				s[i + j] = '-';
			}
			else
			{
				s[i + j] = '+';
			}
		}
	}
	for (int i = n - k + 1;i < n;i++)
	{
		if (s[i]=='-')
		{
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << cnt;

}
int main() {
	int n;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> n;
	for (int i = 0;i < n;i++)
	{
		cout << "Case #" << i + 1 << ": ";
		f();
		cout << endl;
	}

	return 0;
}