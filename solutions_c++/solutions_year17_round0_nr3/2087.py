// 2017_Qualification_C_BathroomStalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <cstdint>

std::ifstream input("C-large.in");
std::ofstream output("Result-large.txt");

int64_t findL(int64_t K, int &L, int64_t &Kbelow)
{
	int64_t Cl = 0, Clnew = 0;
	int i = 0;
	int64_t nrOnLevel = 1;

	while (Clnew < K)
	{
		Cl = Clnew;
		Clnew += nrOnLevel;
		nrOnLevel *= 2;
		i++;
	}
	L = i;
	Kbelow = Cl;
	return nrOnLevel;
}

void solve(int64_t &Sl, int64_t &Sr)
{
	int64_t K, N;
	input >> N >> K;
	int L;
	int64_t Kbelow, nrOnLevel;
	nrOnLevel = findL(K, L, Kbelow);
	int64_t toHelpOnLevel = K - Kbelow - 1;
	int64_t largeGap = N / (nrOnLevel /2);
	int64_t smallGap = largeGap - 1;
	int64_t nrLargeGaps = (N % (nrOnLevel / 2)) + 1;
	int64_t sizeGapToUse;
	if (toHelpOnLevel < nrLargeGaps)
		sizeGapToUse = largeGap;
	else
		sizeGapToUse = smallGap;

	if (sizeGapToUse % 2 == 0)
	{
		Sl = sizeGapToUse / 2;
		Sr = Sl - 1;
	}
	else
		Sl = Sr = sizeGapToUse / 2;
	
}

int main()
{
	int T;
	input >> T;
	for (int cas = 1; cas <= T; cas++)
	{
		int64_t Sl, Sr;
		solve(Sl, Sr);
		std::cout << "Case #" << cas << ": " << Sl << " " << Sr << "\n";
		output << "Case #" << cas << ": " << Sl << " " << Sr << "\n";
	}
}


