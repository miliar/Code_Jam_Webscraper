#include <iostream>
#include <string>

using namespace std; 

int main() 
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t; 
	for (int x = 1; x <= t; x++)
	{
		string s;
		int k;
		cin >> s >> k;

		int i, tries = 0;
    bool flag = false;
		while ( ( i = int(s.find('-')) ) != string::npos )
		{
			if (i >= s.length() - k + 1)
      {
        flag = true;
        break;
      }

			for (unsigned int j = i; j < i + k; j++)
      {
        if (s[j] == '+')
          s[j] = '-';
        else
          s[j] = '+';
      }

			tries++;
		}

		if (flag)
			cout << "Case #" << x << ": " << "IMPOSSIBLE" << "\n"; 
		else
			cout << "Case #" << x << ": " << tries << "\n"; 
	}
	return 0;
}

