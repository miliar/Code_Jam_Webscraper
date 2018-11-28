#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		long long N, K;
		cin >> N >> K;
		long long big_part;
		long long small_part;
		long long number_big, number_small;
		big_part = N;
		small_part = 0;
		number_big = 1;
		number_small = 0;
		while (number_big + number_small < K)
		{
			//cout << number_big << ":" << big_part << " " << number_small << ":" << small_part << endl;
			K -= number_big + number_small;
			long long new_big = 0, new_small = 0, new_big_number = 0, new_small_number = 0;
			if ((big_part - 1) % 2 == 0)
			{
				new_big = (big_part - 1) / 2;
				new_big_number = number_big * 2 + number_small;
				if (number_small > 0)
				{
					new_small = (small_part - 1) / 2;
					new_small_number = number_small;
				}
			}
			else
			{
				new_big = (big_part - 1) / 2 + 1;
				new_big_number = number_big;
				new_small = (big_part - 1) / 2;
				new_small_number = number_big + number_small * 2;
			}
			big_part = new_big;
			number_big = new_big_number;
			small_part = new_small;
			number_small = new_small_number;
		}
		long long size = small_part;
		if (K <= number_big)
			size = big_part;
		long long mini = (size - 1) / 2;
		long long maxi = mini + (size - 1) % 2;
		cout << "Case #" << t << ": " << maxi << " "<< mini << endl;
	}
	return 0;
}