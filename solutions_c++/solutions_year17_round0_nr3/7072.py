// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream> 
#include <climits>
#include <algorithm>

using namespace std;
int findL(int* Stalls, int place)
{
	int ret = 0;
	for (int i = 0; i < place; i++)
	{
		if (Stalls[i] == 0)
			ret++;
		else
			ret = 0;
	}

	return ret;
}

int findR(int* Stalls, int place, int length)
{
	int ret = 0;
	for (int i = length-1; i > place; i--)
	{
		if (Stalls[i] == 0)
			ret++;
		else
			ret = 0;
	}

	return ret;
}

void printStalls(int* Stalls, int length)
{
	for (int i = 0; i < length; i++)
	{
		if (Stalls[i] == 0) cout << ".";
		else cout << "O";
	}
	cout << endl;
}

void main() {
	int t, n, m;
	cin >> t;  
	for (int i = 1; i <= t; ++i) {
		cin >> n >> m;  // read n and then m.
		int* Stalls = new int[n];
		for (int j = 0; j < n; j++)
		{
			Stalls[j] = 0;
		}
		/*int* L = new int[n];
		int* R = new int[n];*/
		
		for (int j = 0; j < m; j++)
		{
			//printStalls(Stalls, n);
			int* minLR = new int[n];
			int* maxLR = new int[n];
			int max_minLR = INT_MIN;
			int max_maxLR = INT_MIN;

			for (int k = 0; k < n; k++)
			{
				if (Stalls[k] == 0)
				{
					int L = findL(Stalls, k);
					int R = findR(Stalls, k, n);
					minLR[k] = std::min(L, R);
					maxLR[k] = std::max(L, R);
					max_minLR = std::max(max_minLR, minLR[k]);
				}
			}

			int count_minLR = 0;
			int place_minLR = -1;
			for (int k = 0; k < n; k++)
			{
				if (Stalls[k] == 0)
				{
					if (minLR[k] == max_minLR)
					{
						count_minLR++;
						if (count_minLR == 1)
							place_minLR = k;

						max_maxLR = std::max(max_maxLR, maxLR[k]);
					}
				}
			}
			int count_maxLR = 0;
			int place_maxLR = -1;
			for (int k = 0; k < n; k++)
			{
				if (Stalls[k] == 0)
				{
					if (maxLR[k] == max_maxLR && minLR[k] == max_minLR)
					{
						count_maxLR++;
						if (count_maxLR == 1)
							place_maxLR = k;
					}
				}
			}

			int main_place = -1;
			if (count_minLR == 1)
			{
				main_place = place_minLR;
			}
			else if (count_maxLR == 1)
			{
				main_place = place_maxLR;
			}
			else
			{
				main_place = place_maxLR;
			}

			Stalls[main_place] = 1;

			//printStalls(Stalls, n);

			if (j == m - 1)
			{
				cout << "Case #" << i << /*"(" << n << " " << m << ")" <<*/ ": " << maxLR[main_place] << " " << minLR[main_place] << endl;
			}
		}
		//cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
	}
}
