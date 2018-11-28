#include <iostream>
#include <string>
using namespace std;

void DecrementStringFrom(string &s, int pos)
{
	for (int i = pos; i >= 0; --i)
	{
		if (s[i] == '0')
			s[i] = '9';
		else
		{
			s[i] = s[i] - 1;
			break;
		}
	}

}

void Set9sFrom(string &s, int pos)
{
	for (int i = pos; i < s.length(); ++i)
		s[i] = '9';

}

bool StringIsZero(string &s)
{
	for (int i = 0; i < s.length(); ++i)
	{
		if (s[i] != '0')
			return false;
	}
	return true;
}

void main()
{
	int numInputs;
	string n;

	cin >> numInputs;
	cin.get();
	for (int i = 0; i < numInputs; ++i) 
	{
		getline(cin, n);
		bool isTidy = false;
		while (!isTidy)
		{
			isTidy = true;
			int largestNum = 0;
			for (int j = 0; j < n.length(); ++j)
			{
				if (n[j] - '0' < largestNum)
				{
					isTidy = false;
					DecrementStringFrom(n, j - 1);
					Set9sFrom(n, j);
					break;
				}
				else
				{
					largestNum = n[j] - '0';
				}
			}
		}
		n.erase(0, n.find_first_not_of('0'));

		cout << "Case #" << i+1 << ": " << n << '\n';
			
	}
}