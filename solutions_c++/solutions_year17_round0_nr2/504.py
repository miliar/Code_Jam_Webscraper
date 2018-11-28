#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

ifstream fin;
ofstream fout;

int firstDec(vector<int> dig)
{
	for (int i = 1; i < dig.size(); i++)
	{
		if (dig[i] < dig[i - 1])
			return i - 1;
	}

	return -1;
}

int firstSeq(vector<int> dig, int pos)
{
	for (int i = pos - 1; i > -1; i--)
	{
		if (dig[i] != dig[pos])
		{
			return i + 1;
		}
	}

	return 0;
}

void printNumber(vector<int> dig, int seq, int dec)
{
	if (dec == -1)
	{
		for (int i = 0; i < dig.size(); i++)
		{
			fout << dig[i];
		}

		return;
	}

	for (int i = 0; i < seq; i++)
	{
		fout << dig[i];
	}

	if(dig[seq] != 1)
		fout << dig[seq] - 1;

	for (int i = seq + 1; i < dig.size(); i++)
	{
		fout << "9";
	}
}

int main()
{
	fout.open("output.txt");
	fin.open("B-large.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		string s;
		fin >> s;
		vector<int> dig(s.size());
		for (int i = 0; i < s.size(); i++)
		{
			dig[i] = s[i] - '0';
		}
		
		int dec = firstDec(dig);
		int seq = firstSeq(dig, dec);
		fout << "Case #" << t + 1 << ": ";
		printNumber(dig, seq, dec);
		fout << endl;
	}

	return 0;
}