// OversizedPancakes.cpp : main project file.

// RevengePanCakes.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
using namespace System;

using namespace std;

int main(void)
{
	//  Console::WriteLine(L"Hello World");
	int Test = 0;
	cin >> Test;
	vector<int> Answers;
	vector<bool> Possible;
	vector<string> PanCake;
	
	vector<int> FlipperSize;
	
	Answers.resize(Test);
	Possible.resize(Test);
	PanCake.resize(Test);
	FlipperSize.resize(Test);
	
	for (int i = 0; i < Test; i++)
	{
		PanCake[i] = "";
		cin >> PanCake[i];
		FlipperSize[i] = 0;
		cin >> FlipperSize[i];

	}
	for (int i = 0; i < Test; i++)
	{
		vector <bool> bPancake;
		int Length = PanCake[i].length();
		bPancake.resize(Length);
		int count = 0;
		Possible[i] = true;
		for(int j=0;j<Length;j++)
		{
			if (PanCake[i][j] == '+')
			{
				bPancake[j] = true;
			}
			else
				bPancake[j] = false;
		}
		for (int j = 0; j<Length; j++)
		{
			if (!bPancake[j])
			{
				int maxLength = j + FlipperSize[i];
				if (maxLength <= Length)
				{
					count++;
					for (int k = j; k <maxLength; k++)
					{
						//cout << "Before Pos " << k << "=" << bPancake[k] << endl;
						bPancake[k]= !bPancake[k];
					//	cout << "After Pos " << k << "=" << bPancake[k] << endl;
					}
				}
				else
				{
					Possible[i] = false;
					break;
				}
			}
		}

		Answers[i] = count;
	}

	for (int i = 0; i < Test; i++)
	{
		cout << "case #" << i + 1 << ": ";
		if (Possible[i])
			cout << Answers[i] << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
//	Console::ReadKey();
	return 0;
}
