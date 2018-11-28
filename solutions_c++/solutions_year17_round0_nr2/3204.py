#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>


typedef unsigned __int64 bigint;


bool IsTidy(const std::string& N)
{
	char last = 0;
	for each(char c in N)
	{
		if (last > c)
			return false;
		last = c;
	}
	return true;
}


int main()
{
	std::ifstream in("input.in");
	std::ofstream out("output.txt");
	if (!in)
		return -1;

	unsigned int numCases = 0;
	in >> numCases;
	for (unsigned int i = 1; i <= numCases; i++)
	{
		out << "Case #" << i << ": ";

		std::string N;

		{
			bigint n;
			in >> n;
			std::stringstream c;
			c << n;
			c >> N;
		}

		size_t charCheck = N.size() - 1;
		while (!IsTidy(N))
		{
			char a = N[charCheck - 1], b = N[charCheck];

			if (a > b)
			{
				N[charCheck - 1]--;
				for (size_t i = charCheck; i < N.size(); i++)
				{
					N[i] = '9';
				}
			}

			charCheck--;
		}

		while (N.front() == '0')
			N = N.substr(1);

		out << N << std::endl;
	}

	return 0;
}


