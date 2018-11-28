#include <iostream>
#include <fstream>
using namespace std;

typedef long long unsigned int uint64_t;

void main()
{
	fstream fin, fout;
	fin.open("in.txt", ios::binary | ios::in);
	fout.open("out.txt", ios::trunc | ios::out);

	uint64_t T = 1, N = 111111111111111110;

	fin >> T;

	uint64_t n, l, r, place = 0;

	for (uint64_t t = 1; t <= T; t++)
	{
		fin >> N;
		n = N;
		place = 0;

		while (N >= 10)
		{
			l = N % 10;
			N = N / 10;

			r = N % 10;
			

			place++;

			if (l < r)
			{
				uint64_t mul = pow(10, place);
				n = (n / mul);
				n = n*mul;
				n--;
				
				N = n;
				place = 0;
			}
		}
		
		fout << "Case #" << t << ": " << n << endl;
	}

	fin.close();
	fout.close();

}