#include <iostream>

using namespace std;

int main()
{
	int n;
	string s;
	int k;

	cin >> n;

	for(int i = 0; i < n; i++)
	{
		cin >> s >> k;

		cout << "Case #" << i + 1 << ": ";
		int cpt = 0;
		for(int j = 0; j <= s.size() - k; j++)
		{
			if(s[j] == '-')
			{
				for(int l = 0; l < k; l++)
					s[j + l] = (s[j + l] == '-')?'+':'-';
				cpt++;
			}
		}
		int l;
		for(l = s.size() - k + 1; l < s.size(); l++)
		{
			if(s[l] == '-')
			{	
				cout << "IMPOSSIBLE" << endl;
				break;
			}
		}
		if(l == s.size())
			cout << cpt << endl;
	}

	return 0;
}	
