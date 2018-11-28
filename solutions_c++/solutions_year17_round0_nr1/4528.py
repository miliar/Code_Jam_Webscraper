// OversizedPancakeFlipper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>

using namespace std;

inline void flip(bool* pancakes, int K)
{
	for(int iK = 0; iK < K; ++iK)
		pancakes[iK] = !pancakes[iK];
}

inline bool check(bool* pancakes, int N)
{
	for(int i = 0; i < N; ++i)
		if (!pancakes[i])
			return false;
	return true;
}

inline void printState(bool* pancakes, int N)
{
	for (int i = 0; i < N; ++i)
		cout << (pancakes[i] ? '+' : '-');
	cout << endl;
}

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		// raw input string
		string sInput;
		// size of flipper
		int K;
		// get the input
		cin >> sInput >> K;
		// number of pancakes
		int N = sInput.length();

		// convert the string to a bool array
		bool* pancakes = new bool[N];
		for(int i = 0; i < N; ++i)
		{
			pancakes[i] = sInput[i] == '+';
		}

		int nFlips = 0;

		int nUpper = N - K;
		// loop through the pancakes and flip the first one that is 
		for(int i = 0; i <= nUpper; ++i)
		{
			if (!pancakes[i])
			{
				flip(pancakes + i, K);
				//printState(pancakes, N);
				++nFlips;
			}
		}


		if (check(pancakes + nUpper, K))
			cout << "Case #" << t << ": " << nFlips << endl;
		else
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;

		delete[] pancakes;
	}
	getchar();
    return 0;
}

