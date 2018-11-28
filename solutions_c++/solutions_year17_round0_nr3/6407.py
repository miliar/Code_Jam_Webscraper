#include <iostream>
#include <sstream>

struct result
{
	unsigned long long max;
	unsigned long long min;
};

result getResult(unsigned long long n, unsigned long long k)
{
	result r; r.max = -1; r.min = -1;

	if (k == 1)
	{
		if (n % 2 == 0)
		{
			r.max = n / 2;
			r.min = r.max - 1;
		}
		else
		{
			r.max = n / 2;
			r.min = n / 2;
		}
		return r;
	}
	else
	{
		unsigned long long newN = -1;
		unsigned long long newK = -1;
		if (n % 2 == 0)
		{
			if (k % 2 == 0)
				newN = n / 2;
			else
				newN = n / 2 - 1;
			newK = k / 2;
		}
		else
		{
			newN = n / 2;
			newK = k / 2;
		}
		return getResult(newN, newK);
	}

	return r;
}

int main(int argc, char* argv[])
{
	unsigned long long numCases;
	std::cin >> numCases;
	for (unsigned long long i = 0; i<numCases; i++)
	{
		unsigned long long N, K;
		std::cin >> N >> K;

		result r = getResult(N, K);

		std::cout << "Case #" << (i + 1) << ": " << r.max << " " << r.min << std::endl;

	}
	return 0;
}
