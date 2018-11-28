#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define mod 1000000007
# define MAX 200011
char flipBit(char ch)
{
	return ch == '+' ? '-' : '+';
}
int main()
{
	ifstream cin("file/a.txt");
	ofstream cout("file/b.txt");
	cin.sync_with_stdio(false);
	int t, k, n, i, var = 0, j;
	cin >> t;
	while (t--)
	{
		var++;
		cout << "Case #" << var << ": ";
		string str;
		cin >> str >> k;
		n = str.size();
		bool condition = true;
		int ans = 0;
		for (i = 0; i < n && condition; i++)
		{
			if (str[i] == '-')
			{
				if (n - i < k)
					condition = false;
				else {
					ans++;
					for (j = i; j < i + k; j++)
						str[j] = flipBit(str[j]);
				}
			}
		}
		if (condition)
			cout << ans << '\n';
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}