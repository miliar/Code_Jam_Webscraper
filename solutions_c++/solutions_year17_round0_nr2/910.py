// Google Code Jam 2017 - Qualifying Round
// B

#include <iostream>
#include <fstream>
using namespace std;

int t;
long long n;

bool is_tidy(long long k)
{
	int last_digit = 9;
	while (k > 0)
	{
		if (last_digit < k % 10) return false;
		last_digit = k % 10;
		k /= 10;
	}
	return true;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.txt");
	fin >> t;
	for (int h = 1; h <= t; h++)
	{
		fin >> n;
		long long ten = 1;
		while (!is_tidy(n))
		{
			int digit = (n / ten) % 10;
			n -= (digit + 1) * ten;
			ten *= 10;
		}
		fout << "Case #" << h << ": " << n << endl;
	}
	return 0;
}