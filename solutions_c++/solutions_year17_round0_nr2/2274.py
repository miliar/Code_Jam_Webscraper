#include <iostream>
#include <string>

std::string find_last_tidy(std::string n)
{
	if (n.length() == 1)
	{
		return n;
	}
	
	for (int i = 0; i < n.length() - 1; i++)
	{
		if (n[i] > n[i + 1])
		{
			for (int j = i + 1; j < n.length(); j++)
			{
				n[j] = '9';
			}
			n[i]--;
			//if (n[i] == 0) n.erase(i, 1);
			i = -1;
		}
	}
	if (n[0] == '0') n = n.erase(0, 1);
	return n;
}

int main()
{
	int testCases = 0;
	std::cin >> testCases;
	std::string n;
	for (int i = 0; i < testCases; i++)
	{
		std::cin >> n;
		std::cout << "Case #" << i + 1 << ": " << find_last_tidy(n) << std::endl;
	}
}