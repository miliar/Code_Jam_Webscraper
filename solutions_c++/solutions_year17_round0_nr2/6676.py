#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		string s;
		cin >> s;
		
		int n = s.size();
		char mn = s[n-1];
		int index = -1;
		for (int i = n-2; i >= 0; --i)
		{
			if (s[i] == '0')
			{
				while (s[i] == '0')
				{
					i--;
				}
				index = i+1;
				mn = 9;
			}
			else if (s[i] > mn)
			{
				index = i+1;
				mn = s[i] - 1;
			}
			else
			{
				mn = s[i];
			}
		}
		
		cout << "Case #" << t+1 << ": ";
		
		if (index == -1)
		{
			cout << s;
		}
		else
		{		
			for (int i = 0; i < index - 1 ; i++)
			{
				cout << s[i];
			}
			
			if (!((index == 1) && (s[0] == '1')))  
			{
				cout << char(s[index-1]-1);
			}
			
			for (int i = index; i < n ; i++)
			{
				cout << '9' ;
			}
		}
		cout << endl;
	}
}