#include <iostream>

using namespace std;

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		string s;
		cin >> s;
		for (int i = 0; i < s.length(); i++)
		{
			bool good = true;
			int lastp = i;
			for (int j = i + 1; j < s.length(); j++)
				if (s[i] > s[j])
				{
					good = false;
					break;
				}
				else if (s[i] < s[j])
					lastp = j;
			if (!good)
			{
				s[lastp]--;
				for (int j = lastp + 1; j < s.length(); j++)
					s[j] = '9';
				break;
			}
		}
		for (int i = 0; i < s.length(); i++)
			if (s[i] != '0')
			{
				s = s.substr(i);
				break;
			}
		cout << "Case #" << tc << ": " << s << endl;
	}
}
