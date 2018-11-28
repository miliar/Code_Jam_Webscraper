// q3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"
using namespace std;


int main()
{
	int T;
	cin >> T;

	for (int Tl = 1; Tl <= T; ++Tl) {
		unsigned long long S, C;

		cin >> S >> C;

		unsigned long long Round = 0;
		for (unsigned long long x = C; x; x>>=1 , Round++);

		// will alwsys be even for a full round - just how many small and large groups


		unsigned long long SizeLarge, SizeSmall;

		unsigned long long CountLarge, CountSmall;
		unsigned long long NewSizeLarge, NewSizeSmall;
		unsigned long long LastRound, SeatsLeft, AlreadySeated;

		SizeLarge = S >> (Round-1);
		// Howmany size large?

		// In the last round - alraedy seated
		AlreadySeated = ((1 << (Round - 1)) - 1);
		
		// Hommany in last round
		LastRound = C - AlreadySeated;
		

		// each round splits the spaces in half, odd will split into an even and odd, even will split into 2 odd
		// so if even is n, I have a mix of n and n-1 or n and n+1

		SeatsLeft = S - AlreadySeated;
		CountLarge = SeatsLeft - (SizeLarge - 1) * (AlreadySeated + 1);

		SizeLarge = S >> (Round - 1);
		//SizeSmall = SizeLarge - 1;

		//CountSmall = AlreadySeated + 1 - CountLarge;
		
		if (CountLarge < LastRound)
			SizeLarge--;



		// Or I just say I have a group of size n and a group of n-1 but even/odd may be either.
		// New large size is always int( old large size -1/2


		 

		cout << "Case #" << Tl << ": ";
		cout << (SizeLarge >> 1) << ' ' << (( SizeLarge & 1  ) ? (SizeLarge >> 1) : ((SizeLarge >> 1)-1) );
		cout << endl;
	}
	return 0;
}

