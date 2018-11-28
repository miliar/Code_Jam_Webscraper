#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <fstream>
using namespace std;

vector<long long> index, Ls, Rs;
long long overallMinimal, minimalIndex;

long long findMin(long long x, long long y)
{
	if (x < y)
		return x;
	else
		return y;
}

long long findMax(long long x, long long y)
{
	if (x > y)
		return x;
	else
		return y;
}

void Initialize(long long size)
{
	for (long long i = 0; i<size; i++)
	{
		Ls[i] = i;
		Rs[i] = size - i-1;
	}
}

void compute(long long size)
{
	for (long long i = 0; i<size; i++)
	{
		if (i == 0)
			Ls[i] = 0;
		else
		{
			if (index[i - 1] != 1)
				Ls[i] = Ls[i - 1] + 1;
			else
				Ls[i] = 0;
		}
	}

	for (long long i = size - 1; i >= 0; i--)
	{
		if (i == (size - 1))
			Rs[i] = 0;
		else
		{
			if (index[i + 1] != 1)
				Rs[i] = Rs[i + 1] + 1;
			else
				Rs[i] = 0;
		}
	}
}

void findMinMax(long long size)
{
	overallMinimal = -999999999;
	long long currentMinimal;
	for (long long i = 0; i<size; i++)
	{
	    if (index[i] != 1)
		{
    		currentMinimal = findMin(Ls[i], Rs[i]);
    		if (currentMinimal >= overallMinimal)
    		{
    			if (currentMinimal == overallMinimal)
    			{
    				if (Rs[i] > Rs[minimalIndex])
    				{
    					minimalIndex = i;
    				}
    			}
    			else
    			{
    				overallMinimal = currentMinimal;
    				minimalIndex = i;
    			}
    		}
		}
	}
}

int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("output_file_name.out","w",stdout);

	int t, count;
	scanf("%d ", &t);
	count = t;
	while (t--)
	{
		cout << "Case #" << count - t << ": ";
		long long n, k, placeIndex;
		scanf("%lld %lld ", &n, &k);
		index.assign(n, 0);
		Ls.assign(n, 0);
		Rs.assign(n, 0);
		Initialize(n);
		for (long long i = 0; i<k; i++)
		{
			findMinMax(n);
			placeIndex = minimalIndex;
			index[placeIndex] = 1;
			compute(n);
		}
		cout << findMax(Ls[placeIndex], Rs[placeIndex]) << " " << findMin(Ls[placeIndex], Rs[placeIndex]) << "\n";
	}
}

