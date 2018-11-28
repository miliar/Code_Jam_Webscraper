// c-stalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <iostream>
#include <vector>

#define LL unsigned long long

using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	try
	{
		for (int i = 0; i < numCases; i++)
		{
			// input
			LL stalls = 0;
			LL people = 0;

			cin >> stalls;
			cin >> people;

			LL left = 0;
			LL right = 0;

			LL arraySizeA = 1;
			LL arraySizeB = 2;

			LL *arrayA = new LL[arraySizeA];
			arrayA[0] = stalls;
			LL *arrayB = new LL[arraySizeB];
			arrayB[0] = arrayB[1] = 0;
			LL bFilled = 0;

			// calc
			if (stalls != people)
			{
				for (LL person = 0; person < people; person++)
				{
					// reset
					if (bFilled == arraySizeB)
					{
						arraySizeA = arraySizeB;
						arraySizeB = arraySizeB * 2;
						bFilled = 0;

						delete arrayA;
						arrayA = arrayB;
						arrayB = new LL[arraySizeB];
					}

					// choose
					LL value = 0;
					LL index = 0;

					for (LL j = 0; j < arraySizeA; j++)
					{
						if (arrayA[j] > value)
						{
							index = j;
							value = arrayA[j];
						}
					}

					arrayA[index] = 0;

					// split
					if (value % 2 == 0)
					{
						right = value / 2;
						if (right > 0)
						{
							left = right - 1;
						}
						else
						{
							left = right;
						}
					}
					else
					{
						right = left = value / 2;
					}

					arrayB[index * 2] = left;
					arrayB[(index * 2) + 1] = right;

					bFilled += 2;
				}
			}

			delete arrayA;
			delete arrayB;

			// output
			cout << "Case #" << i + 1 << ": ";
			if (left > right)
			{
				cout << left << " " << right;
			}
			else
			{
				cout << right << " " << left;
			}
			cout << endl;
		}
	}
	catch (std::exception &ex)
	{
		cout << ex.what();
	}

    return 0;
}

