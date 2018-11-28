/*
 * Program.cpp
 *
 *  Created on: Apr 5, 2017
 *      Author: meni
 */

#include <functional>
#include <queue>
#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include <list>
#include <cstring>

using namespace std;

int solve(int arr[], int n, int k)
{
	int counter = 0;

	for (int i=0;i<n;i++)
	{
		if (arr[i] == 0)
		{
			if (i+k > n)
			{
				return -1; // no solution
			}

			counter++;

			for (int j=i;j<i+k;j++)
			{
				if (arr[j] == 0)
				{
					arr[j] = 1;
				}
				else
				{
					arr[j] = 0;
				}
			}
		}
	}

	return counter;
}

int main()
{
    int ct, t;

    cin >> t;
    for (ct = 1; ct <= t; ct ++)
    {
    	string s;
    	int k;

        cin >> s >> k;

        int n = s.length();
        int* arr = new int[n];
        int sum =0;

        for (int i=0;i<n;i++)
        {
        	if (s[i] == '+')
        	{
        		arr[i] = 1;
        		sum++;
        	}
        	else
        	{
        		arr[i] = 0;
        	}
        }

        if (sum == n)
        {
        	cout << "Case #" << ct << ": " << "0" << endl;
        	continue;
        }

        int min = solve(arr,n, k);

        if (min == -1)
        {
        	cout << "Case #" << ct << ": " << "IMPOSSIBLE" << endl;
        }
        else
        {
        	cout << "Case #" << ct << ": " << min << endl;
        }
    }

    return 0;
}
