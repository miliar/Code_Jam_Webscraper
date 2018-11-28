/*
 * Program.cpp
 *
 *  Created on: Apr 5, 2017
 *      Author: meni
 */

#include <iostream>
#include <cmath>

using namespace std;

unsigned long long solve(unsigned long long  n)
{
	unsigned long long orig = n;
	int arr[18] = {0};
	int idx = 17;
	int num_of_digits = 0;

	while (n)
	{
		num_of_digits++;
		int lsb = n % 10;
		arr[idx--] = lsb;
		n /= 10;
	}

	bool is_tidy = true;

	for (int i=18-num_of_digits;i<17;i++)
	{
		if (arr[i] > arr[i+1]) // bad - fix
		{
			is_tidy = false;
			arr[i]--;
			for (int j=i+1;j<18;j++)
			{
				arr[j] = 9;
			}

			break;
		}
	}

	if (is_tidy)
	{
		return orig;
	}

	unsigned long long resolve = 0;

	for (int i=0;i<18;i++)
	{
		resolve = resolve*10 + arr[i];
	}

	return solve(resolve);
}

int main()
{
    int ct, t;

    cin >> t;
    for (ct = 1; ct <= t; ct ++)
    {
        unsigned long long n;

        cin >> n;
        if (n < 10)
        {
        	cout << "Case #" << ct << ": " << n << endl;
        }
        else
        {
        	cout << "Case #" << ct << ": " << solve(n) << endl;
        }
    }

    return 0;
}
