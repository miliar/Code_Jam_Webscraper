//// ConsoleApplication99.cpp : Defines the entry podouble for the console application.
////
//

#include "stdafx.h"
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		double res = 0.0;

		double D, N;
		cin >> D >> N;

		double* pos = (double*)malloc(N * sizeof(double));
		double* speed = (double*)malloc(N * sizeof(double));

		for (int i = 0; i < N; i++)
		{
			cin >> pos[i] >> speed[i];
		}

		if (N == 0)
		{
			res = 0;
		}
		else if (N == 1)
		{
			double time = (double)(D - pos[0]) / speed[0];
			res = (double)D/time;
		}
		else
		{
			if (pos[0] > pos[1])
			{
				double temp = pos[0];
				pos[0] = pos[1];
				pos[1] = temp;

				temp = speed[0];
				speed[0] = speed[1];
				speed[1] = temp;
			}
			
			if (speed[0] <= speed[1])
			{
				double time = (double)(D - pos[0]) / speed[0];
				res = (double)D / time;
			}
			else if (pos[0] == pos[1])
			{
				double s = std::min(speed[0], speed[1]);
				double time = (double)(D - pos[0]) / s;
				res = (double)D / time;
			}
			else
			{
				double meet = ((double)(speed[0] * pos[1]) - (double)(speed[1] * pos[0])) / (speed[0] - speed[1]);

				if ((double)meet >= D)
				{
					// dont meet
					double time = (double)(D - pos[0]) / speed[0];
					res = (double)D / time;
				}
				else
				{
					double time1 = (meet - pos[0]) / speed[0];
					double time2 = (D - meet) / speed[1];

					double time = time1 + time2;

					res = D / time;
				}
			}
		}
		std::cout << std::setprecision(6) << std::fixed;
		cout << "Case #" << tc << ": " << res << std::endl;
	}

	return 0;
}

