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
		std::vector<std::pair<LL, LL>> ss;

		LL a, b;
		for (int i = 0; i < N; i++)
		{
			fin >> a >> b;
			LL aa = 2*a*b;
			ss.push_back(make_pair(aa,a));
		}

		std::sort(ss.rbegin(), ss.rend(), mycomparer);

		double result = 0;
		LL maxr = LLONG_MIN;
		for (int i = 0; i < K - 1; i++)
		{
			result += ss[i].first;
			if (maxr < ss[i].second)
				maxr = ss[i].second;
		}
		if (K == 1)
			maxr = 0;
		std::vector< LL> vv;
		for (int i = K - 1; i < N; i++)
		{
			LL s1, s2;
			s1 = ss[i].first;
			s2 = ss[i].second;
			LL areaincrease = 0;
			if (s2 <= maxr &&K!=1)
				areaincrease = s1 ;
			else
				 areaincrease = s1 + s2*s2 - maxr*maxr;
			vv.push_back(areaincrease);
		}
		std::sort(vv.rbegin(), vv.rend());
		result+= vv[0] + maxr*maxr;
		fout <<  std::fixed << std::setprecision(11)<< result*M_PI << endl;
	}
}