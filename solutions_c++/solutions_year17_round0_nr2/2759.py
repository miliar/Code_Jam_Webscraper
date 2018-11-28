#include <iostream>
#include <string>

int main()
{
	int t;
	std::cin >> t;
	for(int te = 1; te <= t; te++)
	{
		std::string str;
		std::cin >> str;
		std::string ans;
		int first = 0;
		for(int i = 1; i < str.size(); i++)
		{
			if(str[i] == str[i - 1])
				continue;
			else if(str[i] > str[i - 1])
			{
				first = i;
				continue;
			}
			else
			{
				for(int j = first + 1; j < str.size(); j++)
					str[j] = '9';
				str[first]--;
				break;
			}
		}
		bool got = false;
		for(int i = 0; i < str.size(); i++)
		{
			if(str[i] != '0')
				got = true;
			if(got)
				ans += str[i];
		}
		if(!got)
			ans += '0';
		std::cout << "Case #" << te << ": " << ans << '\n';
	}
}