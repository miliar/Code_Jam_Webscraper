// 03_bathroom.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

struct slot_compare {
	bool operator() (const pair<int,int>& lhs, const pair<int,int>& rhs) const {
		if (lhs.second > rhs.second)
			return true;
		if (lhs.second < rhs.second)
			return false;
		if (lhs.first <= rhs.first)
			return true;
		return false;
	}
};

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N, K;
		cin >> N >> K;
		int Ls = 0;
		int Rs = 0;
	
		set <pair<int, int>, slot_compare> freeslots;
		freeslots.insert(make_pair(0, N));
		for (int j = 0; j < K; ++j)
		{
			auto itr = freeslots.begin();
			int beginS = itr->first;
			int lengthS = itr->second;
			int midS = beginS + (lengthS - 1) / 2;
			Ls = midS - beginS;
			Rs = beginS + lengthS - midS - 1;
			freeslots.erase(itr);
			if (Ls > 0)
				freeslots.insert(make_pair(beginS, Ls));
			if (Rs > 0)
				freeslots.insert(make_pair(midS + 1, Rs));

			if (Ls == 0 && Rs == 0)
				break;
		}
		cout << "case #" << i + 1 << ": " << max(Ls, Rs)<<" "<<min(Ls,Rs) << endl;
	}
	return 0;
}
