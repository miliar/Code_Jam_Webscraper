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
		cout << "Case #" << casee << ": ";
		int k;
		int cnt = 0;
		cin >> k;
		for (int i = 0; i < s.length()-k+1; i++)
		{
			if (s[i] == '-')
			{
				for (int j = i; j < i+k; j++)
					s[j] =  (s[j] == '-' ? '+' : '-');
				cnt++;
			}
		}
		bool ok = true;
		for (int i = 0; i < s.length() && ok; i++)
			if (s[i] == '-')
				ok = false;
		if (!ok)
			cout << "IMPOSSIBLE" << endl;
		else cout << cnt << endl;
	}
}
