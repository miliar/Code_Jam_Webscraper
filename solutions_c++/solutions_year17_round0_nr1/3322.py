#include<iostream>
#include<string>
using namespace std;
int main(void)
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; ++z)
	{
		int ans = 0, k;
		string s;
		cin >> s >> k;
		for (int i = 0; i+k <= s.size(); ++i)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j < i + k; ++j)
				{
					if ( s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';	
				}	
			}
		}
		
		for (int i = s.size() - k + 1; i < s.size(); ++i)
			if (s[i] == '-')
			{
				ans = -1;
				break;
			}
		
		if (ans < 0)
			cout << "Case #" << z << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << z << ": " << ans << endl;

	}
}
