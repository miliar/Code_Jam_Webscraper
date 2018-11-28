#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
using namespace std;
ofstream fout;
void fun(int, string);
void main()
{
	ifstream fin;
	fout.open("out.in");
	fin.open("B-large.in");
	int T;
	fin >> T;
	string N;
	for (int i = 0;i < T;i++)
	{
		fin >> N;
		fun(i,N);
	}
}

void fun(int T,string n)
{
	if (n.length() == 1)
		fout << "Case #" << T + 1 << ": " << n << endl;
	for (int j = 0;j < n.length()-1;j++)
		if (n[j]>n[j + 1])
		{
			n[j] = n[j] - 1;
			for (int i = j + 1;i<n.length();i++)
				n[i] = '9';
			j = -1;
		}
		else if (j == n.length() - 2)
		{
			fout << "Case #" << T + 1 << ": " << stoll(n) << endl;
			return;
		}
}