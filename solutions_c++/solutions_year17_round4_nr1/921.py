
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
double eps = 1e-15;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N, P;
		cin >> N >> P;
		if (P == 2)
		{
			int count0 = 0, count1 = 0;
			for (int i = 0; i < N; i++)
			{
				int a;
				cin >> a;
				if (a % 2 == 0) count0++;
				else count1++;
			}
			cout << "Case #" << tc << ": ";
			cout << count0 + (count1+1)/2 << endl;
		}
		else if (P == 3)
		{
			int count0 = 0, count1 = 0, count2 = 0;
			for (int i = 0; i < N; i++)
			{
				int a;
				cin >> a;
				if (a % 3 == 0) count0++;
				else if (a % 3 == 1)
				{
					if (count2 > 0)
					{
						count2--;
						count0++;
					}
					else
					{
						count1++;
					}
				}
				else
				{
					if (count1 > 0)
					{
						count1--;
						count0++;
					}
					else
					{
						count2++;
					}
				}
			}
			cout << "Case #" << tc << ": ";
			cout << count0 + (count2+count1 + 2) / 3 << endl;
		}
		else
		{
			int count0 = 0, count1 = 0, count2 = 0, count3 = 0;
			for (int i = 0; i < N; i++)
			{
				int a;
				cin >> a;
				if (a % 4 == 0) count0++;
				else if (a % 4 == 1)
				{
					if (count3 > 0)
					{
						count3--;
						count0++;
					}
					else
					{
						count1++;
					}
				}
				else if (a % 4 == 2)
				{
					if (count2 > 0)
					{
						count2--;
						count0++;
					}
					else
					{
						count2++;
					}
				}
				else
				{
					if (count1 > 0)
					{
						count1--;
						count0++;
					}
					else
					{
						count3++;
					}
				}
			}
			count3 = count3 + count1;
			if (count2 > 0)
			{
				if (count3 >= 2)
				{
					count0++;
					count3 -= 2;
					count2--;
				}
			}
			if (count3 >= 4)
			{
				count0 += count3 / 4;
				count3 = count3 % 4;
			}
			if (count3 + count2 > 0)count0++;
			cout << "Case #" << tc << ": ";
			cout << count0 << endl;
		}
	}

}