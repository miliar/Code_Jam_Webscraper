// c_jam_b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream input("c.txt", std::ifstream::in);
	
	FILE * f = fopen("c_out.txt", "a");

	int T = 0;
	input >> T;

	std::vector<long long> heap;

	 for (int i = 0; i < T; ++i)
	 {
		 long long N = 0;
		 long long K = 0;
		 input >> N;
		 input >> K;

		long long min_v = N;

		 if (N == K)
		 {
			fprintf(f, "Case #%i: %i %i\n", i + 1, 0, 0);
		 }
		 else
		 {
			 heap.push_back(N);
				long long l = 0;
				long long r = 0;
			 for (int j = 0; j < K; ++j)
			 {
				 long long v = heap.front();
				 std::pop_heap(heap.begin(), heap.end());
				 heap.pop_back();

				 r = v / 2;
				 l = r - !(v & 1);

				 heap.push_back(r);
				 std::push_heap(heap.begin(), heap.end());

				 heap.push_back(l);
				 std::push_heap(heap.begin(), heap.end());

				 min_v = std::min(min_v, l);
			 }

			 fprintf(f, "Case #%i: %I64d %I64d\n", i + 1, r, min_v);
			 heap.clear();
		 }

		 //output >> std::string("Case #") >> i + 1 >> std::string(": ") >> result >> std::endl;
	 }

	 fclose(f);

	return 0;
}


