#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
typedef long long int LL;
using namespace std;

long long int solve(long long int N)
{
	LL res = 0;
	int flag = 0;
	int cnt = 0;
	std::vector<int> s1;
	while (N > 0 )
	{
			s1.push_back(N%10);
			N = N / 10;
	}
	int len = s1.size();

	int state = 0;
	for (int i = len - 1; i > 0; i--)
	{
		if (s1[i] > s1[i-1] )
		{
			if (s1[i] == 0)
			{
				int k = i + 1;
				while (s1[k] == 0)
					k++;
				s1[k]--;
				for (int j = k-1; j >= 0; j--)
					s1[j] = 9;
			}
			else
			{
				s1[i]--;
				for (int j = i-1; j >= 0; j--)
					s1[j] = 9;
			}
		}
	}
	for (int i = len-1; i>=0; i--)
		res = res * 10 + s1[i];
	return res;
}
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	long long int num_t, N,cnt;
	fin >> num_t;
	cnt = 1;
	while (num_t--)
	{
		fin >> N;
		LL k1 = N;
		LL k2 = 0;
		while (k2 != k1)
		{
			k2 = solve(k1);
			std::swap(k2, k1);
		}
		fout << "Case #" << cnt++ << ": " << k2<<endl;
	}

}