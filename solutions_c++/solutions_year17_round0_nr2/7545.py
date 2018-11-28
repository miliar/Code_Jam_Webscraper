// TidyNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream file("in.txt");

	//std::ostream& output = std::cout;
	std::ofstream outFile("out.txt");
	std::ostream& output = outFile;

	std::string in;
	std::getline(file, in);

	unsigned int count = 0;
	while (std::getline(file, in))
	{
		++count;

		bool ok = false;
		while (!ok)
		{
			ok = true;
			for (unsigned int i = 1; i < in.length(); ++i)
			{
				if (in[i - 1] > in[i])
				{
					in[i - 1] = in[i - 1] - 1;
					for (; i < in.length(); ++i) {
						in[i] = '9';
					}
					ok = false;
					break;
				}
			}
		}

		auto zero = in.find_first_not_of('0');
		if (zero != std::string::npos) {
			in = in.substr(zero);
		}

		output << "Case #" << count << ": " << in << std::endl;
	}

	return 0;
}

