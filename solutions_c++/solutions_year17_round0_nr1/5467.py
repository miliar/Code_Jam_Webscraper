// 01_pancake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

bool flip(string &S, int I, int K)
{
	if (S.length() < I + K)
		return false;

	for (int i = I; i < I + K; ++i)
	{
		if (S[i] == '+') S[i] = '-';
		else S[i] = '+';
	}
}

int check(string &S, int I)
{
	int i = I;
	for (; i < S.length(); ++i)
	{
		if (S[i] == '-') break;
	}
	return i;
}
int main()
{
	int T;
	cin >> T;
	string S;
	int K;
	for (int i = 0; i < T; i++)
	{
		cin >> S;
		cin >> K;

		int flips = 0;
		int j = check(S,0);
		while (j < S.length())
		{
			if (flip(S, j, K)) {
				++flips;
				j = check(S, j);
			}
			else {
				break;
			}
		}
		
		if (j < S.length()) {
			cout << "case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			cout << "case #" << i+1 << ": " << flips << endl;
		}
	}
    return 0;
}

