#include <iostream>
#include <string> 
using namespace std;

int main(int argc, char const *argv[])
{
	int num = 0;
	int count = 0;
	cin >> num;
	for (int i = 0; i < num; ++i)
	{
		string str;
		int len = 0;
		int ans = 0;
		bool flag = true;

		count++;

		cin >> str >> len;
		for (int i = 0; i < str.size() - len + 1; ++i)
		{
			if (str[i]  == '-')
			{
				ans++;
				for (int j = 0; j < len; ++j)
				{
					if (str[i + j] == '-')
					{
						str[i + j] = '+';
					}
					else
						str[i + j] = '-';
				}
			}
		}
		for (int i = 1; i <= len - 1; ++i)
		{
			if (str[str.size() - i] == '-')
			{
				flag = false;
			}
		}
		if (flag == true)
		{
			cout << "Case #" << count << ": " << ans << "\n";
		}
		else
			cout << "Case #" << count << ": IMPOSSIBLE" << "\n";
	}
	return 0;
}