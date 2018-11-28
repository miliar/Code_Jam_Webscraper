#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <vector>

#include <string>


bool convertStep( std::string& s)
{
	int lastVal = 0;

	std::string new_string = "";
	for (unsigned si = 0; si < s.size(); ++si)
	{
		int currVal = (int)(s[si] - '0');

		if (currVal < lastVal)
		{
			for (unsigned sii = 0; sii < si - 1; ++sii)
			{
				new_string += s[sii];
			}
			new_string += '0' + ((10 + lastVal - 1) % 10);
			for (unsigned sii = si; sii < s.size(); ++sii)
			{
				new_string += '9';
			}

			s = new_string;
			return false;
		}

		lastVal = currVal;
	}

	return true;
}

void tidy_numbers()
{
	int t;

	unsigned long long n;

	std::cin >> t;

	for (unsigned i = 0; i < t; ++i)
	{
		std::cin >> n;

		std::string s = std::to_string(n);

		while (!convertStep(s))
		{

		}

		n = std::stoll(s);

		s = std::to_string(n);

		std::cout << "Case #" << i + 1 << ": " << s << std::endl;

	}

}

int main()
{
	tidy_numbers();

	char inputEnd = getchar();
	inputEnd = getchar();

	return 0;
}

