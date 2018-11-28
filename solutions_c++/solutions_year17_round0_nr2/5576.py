#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t, casee = 0;
	cin >> t;
	while (t--)
	{
		string s;
		cin >> s;
		casee++;
		int i = 1;
		bool hapened = 0;
		for (i = 1; i < s.length(); i++)
			if (s[i] < s[i-1])
			{
				hapened = 1;
				break;
			}

		string ans="";
		if (!hapened)
			ans = s;
		else
		{
			bool found = 0;
			int j;
			for (j = i-1; j >= 0; j--)
				if (j ==0 || s[j] != s[j-1])
				{
					found = 1;
					break;
				}
			if (!found || (j == 0 && s[j] == '1'))
				for (int k = 1; k < s.length(); k++)
					ans += '9';
			else 
			{
				s[j]--;
				for (int k = j+1; k < s.length(); k++)
					s[k] = '9';
				ans = s;
			}
		}
		
		cout << "Case #" << casee << ": " << ans << endl;
	}
}
