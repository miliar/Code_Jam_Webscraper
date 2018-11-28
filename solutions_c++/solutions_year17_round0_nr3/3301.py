#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <list>
#include <set>
#include <bitset>


typedef size_t bigint;
typedef long long bigsint;


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

		bigint N;
		std::string K;

		in >> N;

		{
			bigint k;
			in >> k;
			std::bitset<8 * sizeof(k)> b(k);
			K = b.to_string();
		}

		while (K.front() == '0')
			K = K.substr(1);

		K = K.substr(1);
		std::reverse(K.begin(), K.end());

		bigint runningVal = N;
		for (bigint j = 0; j < K.size(); j++)
		{
			switch (K[j])
			{
			case '1':
				runningVal = (runningVal - 1) / 2;
				break;
			case '0':
				runningVal /= 2;
				break;
			}
		}
		bigint a = (runningVal - 1) / 2,
			b = runningVal / 2;
		if (runningVal == 0)
			a = 0;

		out << b << ' ' << a << std::endl;
	}

	return 0;
}


