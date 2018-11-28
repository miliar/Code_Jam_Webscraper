/*
ID: meet2dinesh
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>

char a[10][16];
int N;
using namespace std;

int findId(char *str)
{
	for (int i = 0; i<N; i++)
	{
		if (strncmp(str, a[i], 14) == 0)
			return i;
	}
	return -1;
}

int main() {
	//ofstream fout("outp.txt");
	//ifstream fin("gift1.in");
	//ifstream fin("input.txt");
	int T;// N, Nn;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		char str[1001] = { 0, };
		int K,M=0, flip=0;
		//int d[10] = { 0, }, t, m = 1;
		cin >> str;
		cin >> K;
		M = strlen(str);
		for (int t = 0; t <= M-K ; t++)
		{
			if (str[t] == '-' )
			{
				flip++;
				//now flip k elements
				for (int l = t; l < K+t; l++)
				{
					if (str[l] == '-')
						str[l] = '+';
					else
						str[l] = '-';
				}
			}
		}
		for (int t = M-K; t < M ; t++)
		{
			if (str[t] == '-')
			{
				flip = -1;
			}
		}
		if (flip < 0)
		{
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << i + 1 << ": " << flip << endl;
		}
	}
	return 0;
}