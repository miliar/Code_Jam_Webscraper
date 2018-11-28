#include <string>
#include <fstream>
#include <vector>
#include <algorithm>


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

		int N, K;
		double U;
		in >> N >> K >> U;

		std::vector<double> P;

		for (int i = 0; i < N; i++)
		{
			double x;
			in >> x;
			P.push_back(x);
		}


		//What is the smallest probability, and what is the next smallest, and how many are there that are smallest?
		{
			proc:
			{
				std::sort(P.begin(), P.end());
				double smallest = P.front(), nextSmallest = 1.0f;
				int num = 0;
				for each(double x in P)
				{
					if (x - smallest < 0.0000001)
					{
						num++;
					}
					else
					{
						nextSmallest = x;
						break;
					}
				}
				double maxIncrease = (nextSmallest - smallest) * (double)num;

				double totalIncrease = std::min(maxIncrease, U);
				U -= totalIncrease;
				double coreIncrease = totalIncrease / (double)num;

				for (int i = 0; i < num; i++)
				{
					P[i] += coreIncrease;
				}

				if (U > 0.000001)
					goto proc;
			}
		}

		double product = 1.0;
		for each(double x in P)
			product *= x;

		out << product << std::endl;
	}

	return 0;
}


