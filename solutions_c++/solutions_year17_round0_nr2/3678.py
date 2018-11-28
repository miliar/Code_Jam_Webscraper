#include <iostream>
#include <string>

using namespace std;

void upd(string &s, int j)
{
	s[j] = '9';
	int i;
	for(i = j - 1; i >= 0; i++)
	{
		if(s[i] == '0')
			s[i] = '9';
		else
		{
			s[i]--;
			break;
		}
	}
	if(i + 1 < s.size() && s[i + 1] == '9')
		for(int k = i + 2; k < s.size(); k++)
			s[k] = '9';
}	
int main()
{
	int t;
	string s;

	cin >> t;
	
	for(int i = 0; i < t; i++)
	{
		cin >> s;
		for(int k = 0; k < s.size(); k++)
		{
			for(int j = s.size() - 1; j > 0; j--)
			{
				if(s[j] < s[j - 1])
					upd(s, j);
			}
		}
		s.erase(0, s.find_first_not_of('0'));
		cout << "Case #" << i + 1 << ": " << s << endl;
	}
		
	return 0;
}	
