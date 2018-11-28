#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <vector>

#include <string>

#define uint64 unsigned long long


uint64 nearest_pow2(uint64 k)
{
	uint64 last_pow = 1;
	uint64 curr_pow = 1;
	while (k >= curr_pow)
	{

		last_pow = curr_pow;
		curr_pow = last_pow << 1;

	}

	return curr_pow;
}


uint64 last_pow2(uint64 k)
{
	uint64 last_pow = 1;
	uint64 curr_pow = 1;
	while (k >= curr_pow)
	{

		last_pow = curr_pow;
		curr_pow = last_pow << 1;

	}

	return last_pow;
}


void bathroom_stalls()
{
	int t;

	uint64 n, k;

	std::cin >> t;

	for (unsigned tt = 0; tt < t; ++tt)
	{
		std::cin >> n >> k;

		uint64 pow = nearest_pow2(k);

		uint64 v = n / pow;


		std::cout << v << std::endl;
	}
}

uint64 getValue(uint64 origVal, uint64 n, bool rightSide)
{
	if (n == 0)
	{
		return origVal;
	}

	uint64 lastVal;
	uint64 lastPow2 = last_pow2(n);
	bool lastSide = false;

	if (lastPow2 == 1)
	{
		lastVal = 0;
	}
	else
	{
		uint64 div = lastPow2 / 2;

		lastVal = (n - lastPow2) % div;
		lastSide = (n - lastPow2) / div;

		lastVal = div + lastVal;
	}


	uint64 v = getValue(origVal, lastVal, lastSide);
	if (rightSide)
	{
		if (v == 0)
		{
			return 0;
		}
		return (v - 1) / 2;
	}
	else
	{
		return (v / 2);
	}
}

void bathroom_stalls2()
{
	int t;

	uint64 n, k;

	std::cin >> t;

	for (unsigned tt = 0; tt < t; ++tt)
	{
		std::cin >> n >> k;

		uint64 v = getValue(n, k, 0);
		uint64 y = getValue(n, k, 1);

		std::cout << "Case #" << tt + 1 << ": " << v << " " << y << std::endl;
	}
}


int main()
{
	bathroom_stalls2();

	char inputEnd = getchar();
	inputEnd = getchar();

	return 0;
}

