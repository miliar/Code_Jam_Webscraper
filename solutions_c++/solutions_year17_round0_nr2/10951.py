#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include<algorithm>
#include<math.h>
#include <time.h>
#include<fstream>
#include <ctime>
#include "windows.h" 
#include <map>
#include <cstdlib>
#include <random>

using namespace std;

bool Non_Decreasing_Order(int x)
{
	string y;
	y = to_string(x);
	int r[10];
	for (int i = 0; i < y.size()-1; i++)
	{
		r[i] = y[i] - '0';
		r[i + 1] = y[i + 1] - '0';
		if (r[i]>r[i + 1])
		{
			return false;
		}
	}
	return true;
}
int Last_Tidy_Number(int x)
{
	int t[100];
	int a;
	for (int j = x; j > 0; j--)
	{
		if (Non_Decreasing_Order(j))
		{
			return j;
		}

	}
}
int main()
{
		int a;
		int i = 0;
		int Container;
		int T;
		
		
		ifstream myReadFile;
		ofstream Write_File;
		myReadFile.open("B-small-attempt10.in");
		Write_File.open("Results_For_Code_Jam.txt");
		char output[100];
		if (myReadFile.is_open())
		{
			while (!myReadFile.eof())
			{
				for (i; i < 101; i++)
				{
					myReadFile >> Container;
					if (Container == 100)
					{
						continue;
					}
					else
					{
						Write_File << "Case " <<  "#"<< i << ": "<<Last_Tidy_Number(Container) << endl;
					}
				}
				
			}
	
		}
		myReadFile.close();
		Write_File.close();
		cin >> a;
	
}