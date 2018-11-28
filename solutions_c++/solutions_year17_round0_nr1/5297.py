#include<iostream>

using namespace std;

char opp(char c)
{
	if (c == '-') return '+';
	return '-';
}

int main()
{
	ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		bool ok = true;
		int cnt = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				for (int j = 0; j < k; j++)
				{
					if (j+i >= s.size()) 
					{
						ok = false;
						break;
					}
					s[j+i] = opp(s[j+i]);
				}
				cnt++;
			}
		}
		if (ok)
			cout << "Case #" << t << ": " << cnt << "\n";
		else
			cout << "Case #" << t << ": IMPOSSIBLE\n";
	}
	return 0;
}
