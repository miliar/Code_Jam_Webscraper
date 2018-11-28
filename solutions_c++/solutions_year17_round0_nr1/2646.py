#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cstdlib>
typedef long long int LL;
using namespace std;
#ifndef max
#define max(a,b) ((a) > (b) ? (a) : (b))
#endif
#ifndef min
#define min(a,b) ((a) > (b) ? (b) : (a))
#endif
long long int solve(string s, long long int N)
{
	bool *count = new bool[s.length()];
	for (int i = 0; i < s.length(); i++)
		count[i] = false;
	int len = s.length();
	int cnt = 0;
	for (int i = 0; i < len; i++)
	{
		if (s[i] == '-'&&count[i] == false)
		{
			cnt++;
			if (i + N > len)
				return -1;
			for (int j = i; j < i+N; j++)
				count[j] = !count[j];
		}
		else if (s[i] == '+'&&count[i] == true)
		{
			cnt++;
			if (i + N > len)
				return -1;
			for (int j = i; j < i+N; j++)
				count[j] = !count[j];
		}
	}
	return cnt;
}
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	long long int num_t, N,cnt;
	long long int result1 = 0;
	long long int result2 = 0;
	string s1,s2;
	fin >> num_t;
	cnt = 1;
	while (num_t--)
	{
		fin >> s1;
		fin >> N;
		result1 = solve(s1, N);
		std::reverse(s1.begin(), s1.end());
		result2 = solve(s1, N);
		if (result1 == -1 && result2 == -1)
			fout << "Case #" << cnt++ << ": " << "IMPOSSIBLE" << endl;
		else if (result1==-1 || result2 == -1)
			fout << "Case #" << cnt++ << ": " << max(result1, result2) << endl;
		else
			fout << "Case #" << cnt++ << ": " << min(result1, result2) << endl;

	}

}