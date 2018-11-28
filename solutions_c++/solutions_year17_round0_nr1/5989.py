
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout <<"Case #"<<t <<": ";
		string s;
		int k;
		cin >> s >> k;
		int count = 0;
		for(int i = 0; i <= s.length()-k; i++)
		{
			if (s[i] == '-')
			{
				count ++;
				for(int j = i; j <i+k; j++)
				{
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+'; 
				}
			}
		}
		int flag = 1;
		for(int i = 0; i < s.length(); i++)
			if (s[i] == '-')
				flag = 0;
		if (flag)
			cout << count << endl;
		else
			cout <<"IMPOSSIBLE\n";
	}
	return 0;
}