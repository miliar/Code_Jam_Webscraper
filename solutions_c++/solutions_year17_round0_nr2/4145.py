// c_jam_b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <cmath>

long long findTidy(long long i)
{
	char digit[20] = {0};
	
	int cnt = 0;
	while (i)
	{
		digit[cnt++] = i % 10;
		i /= 10;
	}

	int x = cnt;

	int max = digit[cnt - 1];
	while (x)
	{
		if (max <= digit[x - 1])
		{
			max = digit[x - 1];
			--x;
		}
		else
		{
						digit[x - 1] = 9;

						int y = x;
						while (y >= 2)
						{
							digit[y - 2] = 9;
							--y;
						}
dec:
			if (digit[x])
			{
				--digit[x];
			}
			else
			{
				digit[x] = 9;
				++x;
				goto dec;
			}
			x = cnt;
			max = digit[cnt - 1];
		}
	}

	long long result = 0;
	for (int i = cnt - 1; i >= 0; --i)
	{
		result *= 10;
		result += digit[i];
	}

	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream input("b.txt", std::ifstream::in);
	
	FILE * f = fopen("b_out.txt", "a");

	int N = 0;
	 input >> N;

	 for (int i = 0; i < N; ++i)
	 {
		 long long v = 0;
		 long long result = 0;
		 input >> v;
		 fprintf(f, "Case #%i: %I64d\n", i + 1, findTidy(v));
		 //output >> std::string("Case #") >> i + 1 >> std::string(": ") >> result >> std::endl;
	 }

	 fclose(f);

	return 0;
}

