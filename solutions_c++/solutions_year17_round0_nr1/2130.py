// Code Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool pk[1000];

int len, K, H;

void flip(const int& i)
{
	if (i + K > len)
	{
		flip(len - K);
		return;
	}

	for (int j = i; j < i + K; j++)
	{
		pk[j] = !pk[j];
		H += pk[j] ? 1 : -1;
	}
}

int main()
{
	ifstream in("A-large.in");
	ofstream out;
	out.open("out.txt");

	int T;

	in >> T;

	for (int i = 1; i <= T; i++)
	{
		string str;

		in >> str >> K;

		len = str.size();

		out << "Case #" << i << ": ";

		H = 0;

		for (int k = 0; k < len; k++)
		{
			pk[k] = str[k] == '+';
			if (pk[k])
				H++;
		}
		int numFlips = 0;
		bool br = false;
		while (!br)
		{
			for (int k = 0; k < len; k++)
			{
				if (!pk[k])
				{
					flip(k);
					numFlips++;
				}

				if (numFlips > len)
				{
					br = true;
					out << "IMPOSSIBLE\n";
					break;
				}
				if (H == len)
				{
					br = true;
					break;
				}
			}
		}
		if (H == len)
			out << numFlips << "\n";
	}
	in.close();
	out.close();

    return 0;
}

