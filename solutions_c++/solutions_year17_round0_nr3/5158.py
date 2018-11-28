#include<iostream>
#include<string>
#include<vector>
#include <algorithm> 

using namespace std;



void solve1(long long n, long long k, long long& val_min, long long& val_max)
{

	vector<int> b(n + 2, false);
	b[0] = true;
	b[n + 1] = true;

	int s, ls = 0, rs = 0;
	val_min = 0; val_max = 0;


	for (int kk = 0; kk < k; ++kk)
	{
		val_min = -1;

		for (int i = 0; i < b.size(); ++i)
		{
			if (!b[i])
			{
				int lst = 0, rst = 0;
				for (int j = i - 1; !b[j]; --j, ++lst);
				for (int j = i + 1; !b[j]; ++j, ++rst);

				int cur_val_min = min(lst, rst);
				int cur_val_max = max(lst, rst);

				if ((cur_val_min > val_min) || (cur_val_min == val_min && cur_val_max > val_max))
				{
					ls = lst;
					rs = rst;
					s = i;
					val_min = cur_val_min;
					val_max = cur_val_max;
				}
			}
		}

		b[s] = true;
	}
}


vector< long long > vec;
void devide(long long size)
{
	if (size == 0)
	{
		return;
	}

	vec.push_back(size);

	devide((size - 1) / 2);
	devide((size - 1) / 2 + (size - 1) % 2);
}


void solve2(long long n, long long k, long long& val_min, long long& val_max)
{
	k--;

	vec.clear();
	devide(n);
	sort(vec.begin(), vec.end());
	reverse(vec.begin(), vec.end());


	long long size = (vec[k] - 1);

	val_min = size / 2;
	val_max = size / 2 + size % 2;

};




int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T = 3;

	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{

		int n, k;
		cin >> n >> k;



		long long  val_min = 0, val_max = 0;

		//solve1(n, k, val_min, val_max);
		//
		//long long  val_min2 = 0, val_max2 = 0;
		solve2(n, k, val_min, val_max);

		//if (val_min != val_min2 || val_max != val_max2)
		//{
		//	cout << "aaaa";
		//}


		printf("Case #%d: %lld %lld\n", t+1, val_max, val_min);

	}

	return 0;
}