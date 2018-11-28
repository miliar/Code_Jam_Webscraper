#include<iostream>
#include<string>
#include<string.h>
#include<vector>

using namespace std;

int main()
{
	freopen("G:\\PDF\\Electronics\\6th sem Electronics\\Digital Communication\\A-large.in", "r", stdin);
	freopen("G:\\PDF\\Electronics\\6th sem Electronics\\Digital Communication\\output_file_name1.out", "w", stdout);
	int t;
	cin >> t;
	int cont = 0;
	while (t--)
	{
		cont++;
		string str;
		int n;
		cin >> str >> n;
		int ans = 0;
		int len = str.length();
		for (int i = 0; i < len - n; i++)
		{
			if (str[i] == '-')
			{
				for (int j = i; j < i + n; j++)
				{
					if (str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
				ans++;
			}
		}
		bool temp = false;
		//cout << ans << endl;
		//cout << str << endl;
		for (int i = len - n+1; i < len; i++)
		{
			if (str[i] != str[len - n])
			{
				temp = true;
			}
		}
		//cout << temp << endl;
		if (temp == true)
		{
			cout <<"Case #"<<cont<<": "<< "IMPOSSIBLE" << endl;
		}
		else {
			if (str[len - n] == '-')
				ans++;
			cout << "Case #" << cont << ": " << ans << endl;
		}
	}
	
	return 0;
}