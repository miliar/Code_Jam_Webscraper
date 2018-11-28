// bath.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int _DBG_LOG_ = 0;

void calc(long long, long long, long long &, long long &);

int main(int argc, char* argv[])
{
	// inputs
	int T;
	vector<long long> N;
	vector<long long> K;

	string inFileName = "D:\\DEV\\VS2012\\GoogleCodeJam\\201704\\03\\bath\\input.txt";

	ifstream inFile(inFileName);
	inFile >> T;

	for(int i = 0; i < T; i++)
	{
		long long n;
		long long k;
		
		inFile >> n >> k;
		
		N.push_back(n);
		K.push_back(k);
	}

	for(int i = 0; i < T; i++)
	{
		if(_DBG_LOG_ == 1)
		{
			cout << K[i] << " customers / " << N[i] << " stalls" << endl;
		}

		long long maxP = 0, minP = 0;
		calc(N[i], K[i], maxP, minP);

		cout << "Case #" << i + 1 << ": " << maxP << " " << minP << endl;
	}
}

void calc(long long N, long long K, long long &maxP, long long &minP)
{
	long long *LS = new long long[N];
	long long *RS = new long long[N];
	long long *occ = new long long[N];

	for(long long i = 0; i < N; i++)
	{
		LS[i] = i;
		RS[i] = N - i - 1;
		occ[i] = 0;
	}

	for(long long i = 0; i < K; i++)
	{
		long long maximal_min = -1;
		vector<long long> maximal_min_ind;
		long long maximal_min_cand;

		long long maximal_max = -1;
		vector<long long> maximal_max_ind;
		long long maximal_max_cand;

		long long occ_ind;

		// calculate min LS/RS & max LS/RS
		for(long long j = 0; j < N; j++)
		{
			if(occ[j] == 1)
				continue;

			maximal_min_cand = min(LS[j], RS[j]);
			if(maximal_min < maximal_min_cand)
			{
				maximal_min = maximal_min_cand;
				maximal_min_ind.clear();
				maximal_min_ind.push_back(j);
			}
			else if(maximal_min == maximal_min_cand)
			{
				maximal_min_ind.push_back(j);
			}
		}

		if(maximal_min_ind.size() == 1)
		{
			occ_ind = maximal_min_ind[0];
		}
		else
		{
			for(vector<long long>::iterator it = maximal_min_ind.begin(); it != maximal_min_ind.end(); ++it) {
				maximal_max_cand = max(LS[*it], RS[*it]);
				if(maximal_max < maximal_max_cand)
				{
					maximal_max = maximal_max_cand;
					maximal_max_ind.clear();
					maximal_max_ind.push_back(*it);
				}
				else if(maximal_max == maximal_max_cand)
				{
					maximal_max_ind.push_back(*it);
				}
			}

			// either max or leftmost
			occ_ind = maximal_max_ind[0];
		}

		minP = min(LS[occ_ind], RS[occ_ind]);
		maxP = max(LS[occ_ind], RS[occ_ind]);

		// set occ
		occ[occ_ind] = 1;

		if(_DBG_LOG_ == 1)
		{
			cout << "Customer " << i << " occupies stall " << occ_ind << endl;
		}

		// update LS RS
		for(long long k = 0; k < N; k++)
		{
			if(occ_ind < k)
			{
				if(k - occ_ind - 1 < LS[k])
					LS[k] = k - occ_ind - 1;
			}

			if(occ_ind > k)
			{
				if(occ_ind - k - 1 < RS[k])
					RS[k] = occ_ind - k - 1;
			}
		}
	}

	return;
}
