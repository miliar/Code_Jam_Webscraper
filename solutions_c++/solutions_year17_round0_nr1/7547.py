// OversizedPancakeFlipper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream file("D:/Dev/GoogleJam/2017/OversizedPancakeFlipper/in.txt");

	//std::ostream& output = std::cout;
	std::ofstream outFile("D:/Dev/GoogleJam/2017/OversizedPancakeFlipper/out.txt");
	std::ostream& output = outFile;

	std::string in;
	std::getline(file, in);

	unsigned int count = 0;
	while (std::getline(file, in))
	{
		++count;

		std::string pattern = in.substr(0, in.find(' '));
		unsigned int k = std::stoul(in.substr(in.find(' ') + 1));

		unsigned int flip = 0;
		for (unsigned int i = 0; i <= pattern.size() - k; ++i)
		{
			if (pattern[i] == '-')
			{
				++flip;
				for (unsigned int j = i; j < i + k; ++j) {
					pattern[j] = (pattern[j] == '+' ? '-' : '+');
				}
			}
		}

		output << "Case #" << count << ": ";
		if (pattern.find_last_of('-') == std::string::npos) {
			output << flip << std::endl;
		}
		else {
			output << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}

