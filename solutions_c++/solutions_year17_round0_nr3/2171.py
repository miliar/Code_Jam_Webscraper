// Code Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <queue>
#include <unordered_map>

using namespace std;



int main()
{
	ifstream in("C-large.in");
	ofstream out;
	out.open("out.txt");

	int T;

	in >> T;

	for (int i = 1; i <= T; i++)
	{
		out << "Case #" << i << ": ";

		long long N, K;

		in >> N >> K;

		if (N == K && false)
		{
			out << 0 << " " << 0 << "\n";
			continue;
		}

		unordered_map<long long, long long> occs;
		priority_queue<long long> Q;

		occs[N] = 1;
		Q.push(N);

		while (!Q.empty())
		{
			long long t = Q.top();
			Q.pop();

			long long occ = occs[t];
			K -= occ;

			
			
			long long ls = (t - 1) / 2, rs = (t - 1) / 2 + (t - 1) % 2;

			if (K <= 0)
			{
				out << rs << " " << ls << "\n";
				break;
			}

			std::unordered_map<long long, long long>::iterator left = occs.find(ls);

			if (left != occs.end())
				left->second += occ;
			else
			{
				occs[ls] = occ;
				Q.push(ls);
			}

			std::unordered_map<long long, long long>::iterator right = occs.find(rs);

			if (right != occs.end())
				right->second += occ;
			else
			{
				occs[rs] = occ;
				Q.push(rs);
			}
		}
	}
	in.close();
	out.close();

    return 0;
}

