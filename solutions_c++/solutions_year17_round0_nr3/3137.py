#include <iostream>

using namespace std;

void print(long long Max)
{
	if (Max % 2 == 1)
		cout << Max / 2 << ' ' << Max / 2 << endl;
	else
		cout << Max / 2 << ' ' << Max / 2 - 1 << endl;
	return;
}

void solve(int number)
{
	long long n, k;
	cin >> n >> k;
	k--;
	cout << "Case #" << number << ": ";
	bool equal = true;
	long long Min = n;
	long long Num_min = 1;
	long long Max = n;
	long long Num_max = 1;
	long long T = 1;
	while (true)
	{
		if (k == 0)
		{
			print(Max);
			return;
		}
		if (T <= k)
		{
			k -= T;
			if (equal)
			{
				if (Min % 2 == 1)
				{
					Min /= 2;
					Max /= 2;
					Num_min *= 2;
					Num_max *= 2;
				}
				else
				{
					equal = false;
					Min = Min / 2 - 1;
					Max = Max / 2;
				}
			}
			else
			{
				if (Max % 2 == 1)
				{
					Num_max *= 2;
					Num_max += Num_min;
					Max = Max / 2;
					Min = Min / 2 - 1;
				}
				else
				{
					Num_min *= 2;
					Num_min += Num_max;
					Max = Max / 2;
					Min = Min / 2;
				}
			}
		}
		else
		{
			if (k < Num_max)
			{
				print(Max);
			}
			else
			{
				print(Min);
			}
			return;
		}
		T *= 2;
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}