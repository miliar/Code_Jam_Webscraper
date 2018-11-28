#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

std::string solve(size_t N)
{
	std::string s = std::to_string(N);
	size_t start = 0;
	size_t end = 0;
	for (size_t idx = 0; idx < (s.length() - 1); idx++)
	{
		if (s[idx] - '0' < s[idx + 1] - '0')
		{
			start = idx + 1;
		}
		else if (s[idx] - '0' > s[idx + 1] - '0')
		{
			end = idx + 1;
			break;
		}
	}
	if (end == 0)
	{
		return s;
	}
	std::stringstream ss;
	for (size_t idx = 0; idx < s.length(); idx++)
	{
		if (idx < start)
		{
			ss << s[idx];
		}
		else if (idx == start)
		{
			char digit = ((s[idx] - '0') - 1) + '0';
			if (idx == 0 && digit == '0')
				continue;
			ss << digit;
		}
		else
		{
			ss << '9';
		}
	}
	std::string tidy_str;
	ss >> tidy_str;

	return tidy_str;
}

void read_and_solve(std::string fpath)
{
	std::fstream infile;
	std::ofstream outfile;
	infile.open(fpath);
	outfile.open("../resources/res2.out");

	if (infile.is_open() && outfile.is_open())
	{
		size_t T;
		size_t N;
		infile >> T;
		for (size_t idx = 0; idx < T; idx++)
		{
			std::string tnum;
			infile >> N;
			tnum = solve(N);

			outfile << "Case #" << idx + 1 << ": " << tnum << std::endl;
		}
		infile.close();
		outfile.close();
	}
	else
	{
		std::cout << "FILE ERROR" << std::endl;
	}
}

int main(int argc, char* argv[])
{
	read_and_solve(argv[1]);
	std::cout << "FINISHED" << std::endl;
	getchar();
	return 0;
}
