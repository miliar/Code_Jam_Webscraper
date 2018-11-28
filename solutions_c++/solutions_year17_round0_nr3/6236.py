#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <deque>
#include <algorithm>


using namespace std;

int main(int argc, char* argv[])
{

	fstream inputFile(argv[1], ios_base::in);
	fstream outputFile(argv[2], ios_base::out);
	int t;
	inputFile >> t;

	int n, k, Ls, Rs, counter, tempMax, bingo, secondCounter;
	deque<int> splits, temp;

	for (int i = 1; i <= t; i++)
	{
		inputFile >> n >> k;
		//cout << i << " " << n << endl;
		
		splits.push_back(n);
		counter = static_cast<int>(splits.size());
		tempMax = splits.back();
		while (counter < k)
		{
			tempMax = 0;
			for (int j = 0; j < static_cast<int>(splits.size()); j++)
			{
				temp.push_back(static_cast<int>(floor((splits[j] - 1.0) / 2.0)));
				//cout << temp.back() << " ";
				tempMax = temp.back() > tempMax ? temp.back() : tempMax;
				temp.push_back(static_cast<int>(ceil((splits[j] - 1.0) / 2.0)));
				//cout << temp.back() << " ";
				tempMax = temp.back() > tempMax ? temp.back() : tempMax;
			}
			//cout << "tempMax " << tempMax << endl;
			splits = temp;
			temp.clear();
			counter += static_cast<int>(splits.size());
		}

		secondCounter = 0;
		
		counter -= static_cast<int>(splits.size());
		
		if (counter > n/2)
		{
			Ls = 0;
			Rs = 0;
		}
		else
		{
			for (int j = 0; j < static_cast<int>(splits.size()); j++)
			{
				if (splits[j] == tempMax)
				{
					secondCounter++;
					if (counter + secondCounter >= k)
					{
						bingo = tempMax;
						break;
					}
				}
			}
			if (counter + secondCounter >= k)
			{
				bingo = tempMax;
			}
			else 
			{
				bingo = tempMax - 1;
			}

			//while (counter < k)
			//{
			//	int found = 0;
			//	for (int j = 0; j < static_cast<int>(splits.size()); j++)
			//	{
			//		if (splits[j] == tempMax)
			//		{
			//			bingo = splits[j];
			//			counter++;
			//			splits[j] = -999;
			//			found = 1;
			//			break;
			//		}
			//	}
			//	if (found == 0)
			//	{
			//		tempMax--;
			//		bingo = tempMax;
			//		counter = k;
			//	}
			//}
			//cout << "Bingo " << bingo << endl;
			Ls = static_cast<int>(floor((bingo - 1.0) / 2.0));
			Rs = static_cast<int>(ceil((bingo - 1.0) / 2.0));
		}
		outputFile << "Case #" << i << ": " << max(Ls, Rs) << " " << min(Ls, Rs) << endl;
		splits.clear();
	}

	return 0;
}

