#include<iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string s;
		int k;
		cin >> s >> k;
		int res = 0;
		int j = 0;
		while (j < s.size() && j+k <= s.size())
		{
			if (s[j] == '+')
				j++;
			else
			{
				//cout << j << endl;
				for (int m = j; m < j+k; m++)
				{
					s[m] = (s[m] == '+' ? '-' : '+');
				}
				
				res++;
				j++;
			}
		}
		
		bool converted = true;
		for (j = 0; j < s.size(); j++)
		{
					if (s[j] == '-')
			{
				converted = false;
				break;
			}
		}
		
		cout << "Case #" << i+1 << ": ";	
		if (converted)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}
