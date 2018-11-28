#include <bits/stdc++.h>
using namespace std;

char zamien(char a)
{
	if(a == '-')
		return '+';
	return '-';
}

int solve()
{
	string s;
	int k, wyn = 0;
	cin >> s >> k;
	for(int i = 0 ; i < s.size() - k + 1 ; i++)
	{
		if(s[i] == '-')
		{
			wyn++;
			for(int j = i ; j <= i + k - 1 ; j++)
				s[j] = zamien(s[j]);
		}
	}
	for(char c : s)
		if(c == '-')
			return -1;
	return wyn;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
	{
		cout << "Case #" << i << ": ";
		int wyn = solve();
		if(wyn == -1)
			cout << "Impossible\n";
		else
			cout << wyn << "\n";
	}
}
