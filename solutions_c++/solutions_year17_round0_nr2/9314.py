#include <iostream>
#include <stdio.h>
#define ll long long
using namespace std;

string ans = "", inp;

void dfs(char ls, int pos, bool rock)
{
	char f;

	if(rock)
		f = '9';
	else
		f = inp[pos];

	for(char i = f; i >= ls; i--)
	{
		string tmp = ans;

		while(tmp.size() != inp.size())
			tmp += i;

		if(stoll(tmp) <= stoll(inp))
		{
			if(ans.size() == inp.size())
				return;
			else
			{
				ans += i;
				dfs(i, pos + 1, rock || i < inp[pos]);
			}
		}
	}
}

string solve()
{
	ll inp2 = stoll(inp);
	ans = "";

	dfs('0', 0, 0);

	return ans;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> inp;
		cout << "Case #" << i + 1 << ": " << stoll(solve()) << '\n';
	}
	return 0;
}