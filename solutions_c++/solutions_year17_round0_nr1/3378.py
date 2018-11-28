#include <bits/stdc++.h>
#define ll long long
using namespace std;
int find_first_minus(string &s)
{
	for(int i = 0; i < s.length(); i++)
		if(s[i] == '-')
			return i;
	return -1;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t, k, index;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> s >> k;
		bool flag = true;
		int ans = 0;
		while(flag && (index = find_first_minus(s)) != -1)
		{
			if(index + k > s.length())
			{
				flag = false;
				break;
			}
			ans++;
			for(int j = index; j < index + k; j++)
				s[j] = (s[j] == '+')? '-': '+';
		}
		cout << "Case #" << i << ": ";
		if(flag)
			cout << ans << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}
