#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <string>
#include <iomanip>
#include <algorithm>
typedef long long int LL;
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{

	long long int num_t, N,cnt,R,C;
	fin >> num_t;
	cnt = 1;
	while (num_t--)
	{
		double N, D;
		std::vector<double> hold_values;
		fin >> D >> N;
		double jj,kk;
		for (int i = 0; i < N; i++)
		{
			fin >> kk >> jj;
			hold_values.push_back(((D-kk)/jj));
		}
		std::sort(hold_values.rbegin(),hold_values.rend());
		double val1 = hold_values[0];
		std::cout << std::fixed;
		
		fout << "Case #" << cnt++ << ": " << std::fixed <<std::setprecision(6) << D / val1 << endl;
	}
}