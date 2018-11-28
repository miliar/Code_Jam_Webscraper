#include<iostream>
#include<string>
#include<math.h>
#include<algorithm>

using namespace std;


int main()
{
	int T;
	long long max, min;
	long long n, k;
	long long ans;

	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		cin >> n >> k;
		pair<long long, long long> max_min[10000];
		pair<int, int> d[10000];
		long long sum = 1;
		int H = 1;
		max_min[1].first = n;
		max_min[1].second = -1;
		d[1].first = 1;
		d[1].second = 0;

		while (sum < k)
		{
			if (max_min[H].first % 2 == 1)//max°¡ È¦¼ö
			{
				d[H + 1].first = d[H].first * 2;
			}
			else//max°¡ Â¦¼ö
			{
				d[H + 1].first = d[H].first;
				d[H + 1].second = d[H].first;
			}
			if (max_min[H].second != -1)//minÀÌ ÀÖÀ¸¸é
			{
				if (max_min[H].second % 2 == 1)//minÀÌ È¦¼ö
				{
					d[H + 1].second += d[H].second * 2;
				}
				else//minÀÌ Â¦¼ö
				{
					d[H + 1].first += d[H].second;
					d[H + 1].second += d[H].second;
				}
			}
			max_min[H + 1].second = -1;
			max_min[H + 1].first = max_min[H].first / 2;
			if (max_min[H].first % 2 == 0)//Â¦¼ö¸é
			{
				max_min[H + 1].second = max_min[H].first / 2 - 1;
			}
			if (max_min[H].second != -1)
			{
				if (max_min[H].second % 2 == 0)
					max_min[H + 1].second = max_min[H].second / 2 - 1;
				else
					max_min[H + 1].second = max_min[H].second / 2;
			}
			sum += pow(2, H);
			H++;
		}
		H--;
		sum -= pow(2, H);
		if (k > sum + d[H + 1].first)
			ans = max_min[H + 1].second;
		else
			ans = max_min[H + 1].first;

		max = ans / 2;
		if (ans % 2 != 0)//È¦¼ö¸é
			min = max;
		else
			min = max - 1;
		if (min < 0)
			min = 0;
		printf("Case #%d: ", i);
		cout << max << " " << min << endl;
	}
	return 0;
}