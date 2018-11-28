#include <iostream>

using namespace std;

int main()
{
	int a, b, ct = 0;
	string str;
	bool t = false;
	cin >> a;
	for (int i = 0; i < a; i++)
	{
		cin >> str >> b;
		ct = 0;
		t = false;
		for (int j = 0; j < str.size(); j++)
		{
			if (str[j] == '+')
			{
			 	if (j == str.size() - 1)
					t = true;
				continue;
			}
			if (str[j] == '-' && ((j + b) <= str.size()))
			{
			//	cout << "rrr" << j + b - 1 << " " << str.size() << endl;
				ct++;
				for (int k = 0; k < b; k++)
				{
					if (str[j + k] == '-')
						str[j + k] = '+';
					else
						str[j + k] = '-';
				}
				
			}
			if (str[j] == '-')
			{
				t = false;
				break;
			}

		}	
		if (!t)
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl; 
		else
			cout << "Case #" << i + 1 << ": " << ct << endl; 
	}	
	
		
	return 0;
}
