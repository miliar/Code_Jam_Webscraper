#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cstdlib>
#include <algorithm>
typedef long long int LL;
using namespace std;
#ifndef max
#define max(a,b) ((a) > (b) ? (a) : (b))
#endif
#ifndef min
#define min(a,b) ((a) > (b) ? (b) : (a))
#endif
ifstream fin("in.txt");
ofstream fout("out.txt");
LL z22;
bool isequal(std::pair<LL, LL> i1)
{
	if (i1.first == z22)
		return true;
	else
		return false;
}
long long int solve(long long int N, long long int K)
{
	std::vector<std::pair<LL, LL>> v1;
	v1.push_back(make_pair(N, 1));

	long long int s = N - 1;
	while (K)
	{
		std::sort(v1.begin(), v1.end());
		long long int s = v1.back().first-1;
		LL n1 = v1.back().second;
		v1.pop_back();
		LL s1 = s / 2;
		LL s2 = s - s1;
		if (K <= n1)
		{
			fout << s2 << " " << s1; return -1;
		}
		z22 = s1;
		auto it = std::find_if(v1.begin(), v1.end(), isequal);
		if (it != v1.end())
			(*it).second += n1;
		else
			v1.push_back(make_pair ( s1, n1));
		z22 = s2;
		auto it1 = std::find_if(v1.begin(), v1.end(), isequal);
		if (it1 != v1.end())
			(*it1).second += n1;
		else
			v1.push_back(make_pair(s2, n1));

		K -= n1;
	}
	return -1;
}
int main()
{
	long long int num_t, N,cnt,K;
	long long int result1 = 0;
	long long int result2 = 0;
	string s1,s2;
	fin >> num_t;
	cnt = 1;
	while (num_t--)
	{
		fin >> N;
		fin >> K;
		fout << "Case #" << cnt++ << ": ";
		solve(N, K);
		fout<< endl;

	}

}