#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
	int c;
	cin >> c;
	cin.ignore();
	for(int i = 1; i <= c; i++)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		int flips = 0;
		cin.ignore();
		for(int j = k; j <= s.size(); j++)
		{
			if(s[j - k] == '-')
			{
				flips++;
				for(int l = j - k; l < j; l++)
				{
					s[l] = (s[l] == '-' ? '+' : '-');
				}
			}
		}
		if(s.find('-') == string::npos)
		{
			cout << "Case #" << i << ": " << flips << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}