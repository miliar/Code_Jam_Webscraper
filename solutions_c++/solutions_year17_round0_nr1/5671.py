#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool flip(std::string& pstr,size_t start,size_t end)
{
	if (end > pstr.length())
	{
		return false;
	}
	for (size_t idx = start; idx < end; idx++)
		pstr[idx] == '-' ? pstr[idx] = '+' : pstr[idx] = '-';

	return true;
}

long solve(std::string& pstr, size_t K)
{
	size_t count = 0;
	size_t start = pstr.find_first_of("-");
	while (start < pstr.length())
	{
		bool res = false;
		res = flip(pstr, start, start + K);
		if (res)
			count++;
		else
			return -1;

		start = pstr.find_first_of("-");
	}
	return count;
}

void read_and_solve(std::string fpath)
{
	std::fstream infile;
	std::ofstream outfile;
	infile.open(fpath);
	outfile.open("../resources/res.out");

	if(infile.is_open() && outfile.is_open())
	{
		size_t T;
		std::string pcakestr;
		size_t K;
		infile >> T;
		for(size_t idx=0; idx < T; idx++)
		{
			long fcount = -1;
			infile >> pcakestr;
			infile >> K;
			fcount = solve(pcakestr, K);
			if (fcount == -1)
			{
				outfile << "Case #" << idx + 1 << ": " << "IMPOSSIBLE" << std::endl;
			}
			else
			{
				outfile << "Case #" << idx + 1 << ": " << fcount << std::endl;
			}
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
