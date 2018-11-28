#define TEST

#ifdef TEST 
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <iostream>
#include <vector>
#include <algorithm>



int row0[1005];
int row1[1005];
int numOfSeats;


bool remove(int from, int type)
{
	bool removed = false;

	for (int i = from; i < numOfSeats; ++i)
	{
		if (type == 0 && row0[i] > 0)
		{
			row0[i]--;
			removed = true;
			break;
		}
		else if (type == 1 && row1[i] > 0)
		{
			row1[i]--;
			removed = true;
			break;
		}
	}

	return removed;
}




int main()
{
#ifdef TEST
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "wb", stdout);
#endif

	int numOfTestcases;
	std::cin >> numOfTestcases;

	for (int t = 0; t < numOfTestcases; ++t)
	{
		std::cout << "Case #" << (t + 1) << ": ";

		for (int i = 0; i < 1005; ++i)
		{
			row0[i] = 0;
			row1[i] = 0;
		}

		int numOfCustomers, numOfTickets;
		std::cin >> numOfSeats >> numOfCustomers >> numOfTickets;

		int numOf0s = 0;
		int numOf1s = 0;
		int numOfRides = 0;
		int numOfReplaces = 0;

		for (int k = 0; k < numOfTickets; ++k)
		{
			int pos, buyer;
			std::cin >> pos >> buyer;
			if (buyer == 1)
			{
				row0[pos - 1]++;
				numOf0s++;
			}
			else
			{
				row1[pos - 1]++;
				numOf1s++;
			}
		}
		
		
		// start from left to right, try to pair up/cancel the customers by id
		for (int i = 0; i < numOfSeats; ++i)
		{
			bool removed = true;
			while (row0[i] > 0 && removed)
			{
				removed = remove(i + 1, 1);
				if (removed)
				{
					row0[i]--;
					numOf0s--;
					numOf1s--;
					numOfRides++;
				}
			}
		}

		for (int i = 0; i < numOfSeats; ++i)
		{
			bool removed = true;
			while (row1[i] > 0 && removed)
			{
				removed = remove(i + 1, 0);
				if (removed)
				{
					row1[i]--;
					numOf0s--;
					numOf1s--;
					numOfRides++;
				}
			}
		}

		// only 1s remaining
		if (numOf0s == 0)
		{
			numOfRides += numOf1s;
			numOfReplaces = 0;
		}
		
		// only 0s remaining
		if (numOf1s == 0)
		{
			numOfRides += numOf0s;
			numOfReplaces = 0;
		}

		// 1 column remaining
		if (numOf0s > 0 && numOf1s > 0)
		{
			// if its the first column the ride is the sum
			if (row0[0] > 0)
			{
				numOfRides += numOf0s + numOf1s;
				numOfReplaces = 0;
			}
			else
			{
				numOfRides += std::max(numOf0s, numOf1s);
				numOfReplaces = std::min(numOf0s, numOf1s);
			}
		}
		
		std::cout << numOfRides << " " << numOfReplaces << std::endl;
	}
}