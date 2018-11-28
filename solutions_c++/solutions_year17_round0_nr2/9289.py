#include <fstream>
#include <string>
#include <iostream>
#include <sstream>

bool IsNewMaxtidy(std::string currentNumStr, int& digit)
{
	if(currentNumStr.size() == 1)
	{
		return true;
	}
	for (digit; digit < currentNumStr.size() - 1; ++digit)
	{
		if (currentNumStr.at(digit) > currentNumStr.at(digit + 1))
		{
			return false;
		}
		if (digit == currentNumStr.size() - 2)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	std::ifstream infile("D:\\Projects\\input2_17.txt");
	std::ofstream outfile("D:\\Projects\\output2_17.txt");

	std::string line;
	std::getline(infile, line);
	int testCaseNum = std::stoi(line);

	for (int n = 0; n < testCaseNum; n++)
	{
		std::getline(infile, line);
		long long currentNum = stoll(line);
		
		std::string maxTidy = "1";
		for (long long i = currentNum; i >= 1; --i)
		{
			std::string currentNumStr = std::to_string(i);
			int digit = 0;
			if (IsNewMaxtidy(currentNumStr, digit))
			{
				maxTidy = currentNumStr;
				break;
			}
			else
			{
				for (int digitToNull = digit + 2; digitToNull < currentNumStr.size(); ++digitToNull)
				{
					currentNumStr.at(digitToNull) = '0';
				}
				i = stoll(currentNumStr);
			}
		}
		std::cout << "Case #" << n + 1 << ": " << maxTidy << std::endl;
		outfile << "Case #" << n + 1 << ": " << maxTidy << std::endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

