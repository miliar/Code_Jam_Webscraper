#include <bits/stdc++.h>
using namespace std;

bool good(string str)
{
	for(int i = 0; i < (int)str.length(); i++)
	{
		if(str[i] == '-')
			return false;
	}
	return true;
}

int main()
{
	int t, x = 1;
	cin >> t;
	while(t--)
	{
		string str;
		int k, n = 0;
		cin >> str >> k;
		for(int i = 0; i <= (int)str.length() - k; i++)
		{
			if(str[i] == '-')
			{
				for(int j = i; j < i + k; j++)
				{
					if(str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
				n++;
			}
		}
		if(good(str))
		    cout << "Case #" << x << ": " << n << endl;
	    else
		    cout << "Case #" << x << ": " << "IMPOSSIBLE" << endl;
		x++;
	}
    return 0;
}
