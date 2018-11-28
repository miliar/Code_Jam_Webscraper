#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
using namespace std;
ofstream fout;
void fun(int, string,int);
void main()
{
	ifstream fin;
	fout.open("out.in");
	fin.open("A-large.in");
	int T,K;
	fin >> T;
	string S;
	for (int i = 0;i < T;i++)
	{
		fin >> S;
		fin >> K;
		fun(i, S, K);
	}
}

void fun(int T, string S, int K)
{
	int n = 0;
	for (int i = 0;i < S.length();i++)
	{
		if (S[i] != '+')
		{
			if (S.length() - i < K)
			{
				fout << "Case #" << T + 1 << ": IMPOSSIBLE" << endl;
				return;
			}
			for (int j=0;j < K;i++,j++)
			{
				if (S[i] == '-')
					S[i] = '+';
				else
					S[i] = '-';
			}
			n++;
			i -= K;
		}
	}
	fout << "Case #" << T + 1 << ": " << n << endl;
}