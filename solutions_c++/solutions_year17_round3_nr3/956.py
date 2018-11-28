#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <string>
#include <iomanip>
#include <algorithm>
#include <cfloat>
#include <limits>
typedef long long int LL;
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");
#define M_PI 3.14159265358979323846

bool mycomparer(std::pair<LL, LL> lhs, std::pair<LL, LL> rhs) {
	if (lhs.first < rhs.first) {
		return true;
	}
	else if (lhs.first == rhs.first && lhs.second > rhs.second) {
		return true;
	}
	else {
		return false;
	}
}
int main()
{

	long long int num_t, N,cnt,R,C;
	fin >> num_t;
	cnt = 1;
	while (num_t--)
	{

		fout << "Case #" << cnt++ << ": ";
		LL N, K;
		fin >> N >> K;
		double U;
		fin >> U;
		std::vector<double> zz;
		double tt;
		for (int i = 0; i < N; i++)
		{
			fin >> tt;
			zz.push_back(tt);
		}
		sort(zz.begin(), zz.end());
		int i = 1;
		while (1)
		{
			double tt;
			if (i == N)
				tt = 1;
			else
				tt= zz[i];
			double qq = zz[0];
			double n1 = U / i;
			double interv = tt - qq;
			if (n1 < tt - qq)
				interv = n1;
			for (int j = 0; j < i; j++)
				zz[j] = zz[j] + interv;
			U = U - (interv)*i;
			if (U < 0.000001)
				break;
			i++;
		}
		double result = 1;
		for (int i = 0; i < K; i++)
			result = result*zz[i];
		fout <<  std::fixed << std::setprecision(11)<< result << endl;
	}
}