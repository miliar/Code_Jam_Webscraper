#include <iostream>
#include <string>
#include <Windows.h>
#include<fstream>

using namespace std;
int check(char *arr)
{
	int checknum = 0;
	for (int i = 0; i < strlen(arr); i++)
	{
		if (arr[i] == '-')
		{
			checknum++;
		}
	}
	return checknum;
}
void main()
{
	ifstream fin;
	ofstream fo;
	char arr[100][100];
	int flipper[100];
	fin.open("A-small-attempt0.in");
	fo.open("A-small-sou.out");
	if (!fin)
	{
		cout << "fail" << endl;
		exit(1);
	}
	else
	{
		for (int i = 0; i < 100; i++)
		{
			fin >> arr[i] >> flipper[i];
		}
	}
	
	char *arr2 = new char;
	//for (int z = 0; z < 100; z++)
	int z = 0;
	while (z < 100)
	{
		int r = 0;
		arr2 = arr[z];
		for (int s = 0; s < strlen(arr2) - flipper[z] + 1; s++)
		{			
			if (arr2[s] == '-')
			{
				for (int i = s; i < s + flipper[z]; i++)
				{
					if (arr2[i] == '-')
					{
						arr2[i] = '+';
					}
					else
					{
						arr2[i] = '-';
					}
				}
				r++;
			}
		}
	
		for (int e = strlen(arr2) - 1; e > flipper[z] - 1; e--)
		{
			if (arr2[e] == '-')
			{
				for (int i = e; i > e - flipper[z]; i--)
				{
					if (arr2[i] == '-')
					{
						arr2[i] = '+';
					}
					else if (arr2[i] == '+')
					{
						arr2[i] = '-';
					}
				}
				r++;
			}
		}
		if (check(arr2) == 0 && r<100)
		{
			cout << z << "   The number of reversals :" << r << endl;
			fo << "case #" << z + 1 << ": " << r << endl;
		}
		else
		{
			cout << z << "   IMPOSSIBLE" << endl;
			fo << "case #" << z + 1 << ": IMPOSSIBLE" <<endl;
		}
		z++;
	}

	if (fin.is_open() == true)
	{
	fin.close();
	}
}

