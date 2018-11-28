#include <iostream>
#include <string>

int main()
{
	int t;
	std::cin >> t;
	for(int te = 1; te <= t; te++)
	{
		std::string str;
		int k;
		std::cin >> str >> k;
		int ans = 0;
		for(int i = 0; i + k <= str.size(); i++)
		{
			if(str[i] == '+')
				continue;
			for(int j = 0; j < k; j++)
				str[i+j] = (str[i+j] == '+'?'-':'+');
			ans++;
		}
		bool valid = true;
		for(int i = 0; i < str.size(); i++)
			valid = valid && str[i] == '+';
		std::cout << "Case #" << te << ": ";
		if(valid)
			std::cout << ans;
		else
			std::cout << "IMPOSSIBLE";
		std::cout << '\n';
	}
}