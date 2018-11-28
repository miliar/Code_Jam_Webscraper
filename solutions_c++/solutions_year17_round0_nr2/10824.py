// TidyN.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	std::ifstream infile("G:\\sample.txt");
	//int n;
	int temp, r1, r2;
	int T;
	//std::cin >> T;
	string str;
	int t = 0;
	getline(infile, str);
	T = stoi(str);
	vector<int> n(T);

	while (t!=T)
	{
		getline(infile, str);
		n[t] =stoi(str);
		t++;
	}
	
	for (int t = 0; t < T; t++)
	{
		for (int i = n[t]; i > 0; i--)
		{
			temp = i;
			while (temp != 0)
			{
				r1 = temp % 10;
				temp = temp / 10;
				r2 = temp % 10;
				if (r2 < r1)
				{
					continue;
				}
				else if (r1 < r2)
				{
					break;
				}
			}
			if (temp == 0)
			{
				std::cout << "Case #" << t + 1 << ": " << i << std::endl;
				break;
			}
		}
	}
    return 0;
}

