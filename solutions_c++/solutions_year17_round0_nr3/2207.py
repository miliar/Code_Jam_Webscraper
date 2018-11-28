// Google2017Q-C.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <string>
#include <set>
#include <map>
#include <fstream>

using namespace std;

typedef long long int64;

void add(map<int64, int64>& M, int64 pos, int64 val)
{
	if (M.find(pos) == M.end())
		M[pos] = val;
	else
		M[pos] += val;
}


int main()
{
	ifstream input;
	ofstream output;
	input.open("C-large.in", std::ios_base::in);
	output.open("C-large-output.txt");

	int64 T;
	input >> T;
	for (int64 g = 0; g < T; g++)
	{
		int64 n, k;
		input >> n >> k;

		set<int64> Q;
		map<int64, int64> Mp;

		Q.insert(n);
		Mp[n] = 1;

		auto p = Q.begin();

		int64 j = k;
		int64 m = n;

		while (j > 0)
		{			
			m = *p;
			int64 q = Mp[m];

			Q.insert(m / 2);
			Q.insert((m - 1) / 2);

			add(Mp, m / 2, q);
			add(Mp, (m - 1) / 2,  q);

			p--;
			j -= q;
		}

		output << "Case #" << g + 1 << ": ";
		output << m / 2 << " " << (m - 1) / 2 << "\n";
	}

	input.close();
	output.close();

	return 0;
}




