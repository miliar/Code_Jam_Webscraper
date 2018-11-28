#include<fstream>

using namespace std;

void swap(long long& i1, long long& i2)
{
	long long buffer = i1;
	i1 = i2;
	i2 = buffer;
}


int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;

	for (int test_case = 0; test_case < T; test_case++)
	{
		long long n, k, step = 2, min, max, num_max = 0, num_min = 2;

		cin >> n >> k;
		k--;

		max = n / 2;
		min = n / 2;

		if (n % 2 == 0)
		{
			min--;
			num_max++;
			num_min--;
		}
	
		while (k > step)
		{
			long long temp1 = (min - 1) / 2, temp2, n_t1 = 0, n_t2 = 0;

			k -= step;
			step *= 2;

			if (min == max)
			{
				if (min % 2 == 0)
				{
					temp2 = temp1 + 1;
					n_t1 = (num_min + num_max);
					n_t2 = n_t1;
				}
				else
				{
					n_t1 = (num_min + num_max) * 2;
					temp2 = temp1;
				}
			}
			else
			{
				temp2 = temp1 + 1;
				if (min % 2 == 0)
				{
					n_t1 = num_min;
					n_t2 = num_min + num_max * 2;
				}
				else
				{
					n_t1 = num_min * 2 + num_max;
					n_t2 = num_max;
				}
			}
			
			if (temp1 < temp2)
			{
				min = temp1;
				num_min = n_t1;
				max = temp2;
				num_max = n_t2;
			}
			else if (temp1 > temp2)
			{
				max = temp1;
				num_max = n_t1;
				min = temp2;
				num_min = n_t2;
			}
			else
			{
				min = temp1;
				max = min;
				num_min = n_t1 + n_t2;
				num_max = 0;
			}
		}		

		if (k != 0)
		{
			if (k <= num_max)
			{
				if (max % 2)
				{
					max = (max - 1) / 2;
					min = max;
				}
				else
				{
					min = (max - 1) / 2;
					max = min + 1;
				}
			}
			else
			{
				if (min % 2)
				{
					max = (min - 1) / 2;
					min = max;
				}
				else
				{
					min = (min - 1) / 2;
					max = min + 1;
				}
			}
		}

		cout << "Case #" << test_case + 1 << ": " << max << " " << min << endl;
	}

	return 0;
}