// Google Code Jam 2017 - Qualifying Round
// C

#include <iostream>
#include <fstream>
using namespace std;

int t;
long long n;
long long k;

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.txt");
	fin >> t;
	for (int h = 1; h <= t; h++)
	{
		fin >> n >> k;
		long long two = 1;
		while (2 * two <= k) two *= 2;
		long long small_val = (n - two + 1) / two;
		long long large_val = small_val + 1;
		long long large_num = (n - two + 1) - small_val * two;
		long long small_num = two - large_num;
		fout << "Case #" << h << ": ";
		if (k - two + 1 <= large_num)
		{
			fout << large_val / 2 << " " << (large_val - 1) / 2 << endl;
		}
		else
		{
			fout << small_val / 2 << " " << (small_val - 1) / 2 << endl;
		}
	}
	return 0;
}