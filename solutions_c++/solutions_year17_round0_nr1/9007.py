#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
	int T,k;
	cin >> T;
	string s;
	for (int i = 1; i <= T; i++)
	{
		int count = 0;
		cin >> s >> k;
		vector<char> c(s.length());
		for (int j = 0; j < s.length(); j++)
			c[j] = s.at(j);


		for (int j = 0; j < s.length(); j++)
		{
			if (c[j] == '-' && (s.length()-j)>=k)
			{
				count++;
				int n = 0;
				for (int w = j; n<k; w++)
				{
					n++;
					if (c[w] == '-')
						c[w] = '+';
					else
						c[w] = '-';
				}
			}
		}
		bool flag = true;
		for (int j = 0; j < s.length(); j++)
		{
			if (c[j] == '-')
			{
				flag = false;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (flag)
			cout << count << endl;
		else
			cout << "IMPOSSIBLE" << endl;

	
}
	return 0;
}