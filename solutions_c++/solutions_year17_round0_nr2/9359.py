// tidy numbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

long long int mypow(int base, int index)
{
	if (index == 0)return 1;
	else if (index == 1)return base;
	else return base*mypow(base, index - 1);
}

int main()
{
	int t, min, size = 0, violate = -1;
	long long int num, statnum;
	int arr[20];
	cin >> t;
	for (int i = 0;i < t;i++)
	{
		cin >> num;
		statnum = num;
		do
		{
			num = statnum;
			size = 0;
			violate = -1;
			memset(arr, 0, sizeof(arr));
			for (int j = 0;num > 0;j++)
			{
				arr[j] = num % 10;
				num = num / 10;
				size++;
			}
			min = arr[size-1];
			for (int j = size-1;j>=0;j--)
			{
				if (min <= arr[j])min = arr[j];
				else {
					violate = j;
					break;
				}
			}
			if (violate != -1)
				statnum = ((statnum / mypow(10, violate)) * mypow(10, violate)) - 1;
		} while (violate != -1);
		cout << "Case #" << i + 1 << ": " << statnum << endl;
	}
    return 0;
}

