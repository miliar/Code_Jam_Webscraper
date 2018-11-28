// c_jam_b.cpp : Defines the entry point for the console application.
//

#include <tchar.h>

#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <bitset>

#include <stdio.h>
#include <hash_map>
#include <hash_set>
#include <stack>
#include <list>
#include <deque>
#include <vector>
#include <map>

#define SMALL_CASE 0
#define USER_CASE 0

int _tmain(int argc, _TCHAR* argv[])
{
#if SMALL_CASE
	std::ifstream input("c:\\cdj\\A-small-attempt1.in", std::ifstream::in);
	FILE * f = fopen("c:\\cdj\\A_small.out", "a");
#elif USER_CASE
	std::ifstream input("c:\\cdj\\input.txt", std::ifstream::in);
	FILE * f = fopen("c:\\cdj\\output.txt", "a");
#else
	std::ifstream input("c:\\cdj\\A-large.in", std::ifstream::in);
	FILE * f = fopen("c:\\cdj\\A_large.out", "a");
#endif

	int T = 0;
	input >> T;
	for (int i = 0; i < T; ++i)
	{
		long long D = 0;
		input >> D;
		int N = 0; 
		input >> N;

		//std::vector<int> distance(N);
		//std::vector<int> speed(N);

		float max_time = 0;

		long long dist = 0;
		long long speed = 0;

		for (int j = 0; j < N; ++j)
		{
			int k = 0;
			int s = 0;

			input >> k;
			input >> s;


			float time = static_cast<float>(D - k) / s;

			if (time > max_time)
			{
				dist = D - k;
				speed = s;
				max_time = time;
			}
		}

		double result = static_cast<double>(D * speed) / dist;
		fprintf(f, "Case #%d: %.6f\n", i + 1, result);
	}

	fclose(f);
	return 0;
}


