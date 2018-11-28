#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>
#include <cmath>
#include <stack>
#include <iomanip>
#define int long long
#define CONTAINS(v,n) (find((v).begin(), (v).end(), (n)) != (v).end())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define ARY_SORT(a, size) sort((a), (a)+(size))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;


struct St
{
	int start;
	int end;
	bool is_c;

	bool operator < (const St &st) const
	{
		return (start < st.start);
	}
};

int AC, AJ;
St st[4];

const int HALF = 720;
int check(int n, bool flg[4], bool is_first_c)
{
	bool is_c = is_first_c;

	int change = 0;
	int sum_c = 0;
	int sum_j = 0;
	int cur_t = 0;
	int cnt = 0;
	while(cnt < n)
	{
		int index = cnt / 2;
		if (cnt % 2 == 0)
		{
			int start_len = st[index].start - cur_t;

			int *p_sum = is_c ? &sum_c : &sum_j;
			if (start_len + *p_sum >= HALF)
			{
				cur_t += HALF - *p_sum;
				*p_sum = HALF;
				is_c = !is_c;
				change++;
			}
			else
			{
				if (flg[cnt])
				{
					*p_sum += st[index].start - cur_t;
					cur_t = st[index].start;
					if (*p_sum > HALF)
					{
						return INT_MAX;
					}
					is_c = !is_c;
					change++;
					p_sum = is_c ? &sum_c : &sum_j;
				}
				if (st[index].is_c == is_c)
				{
					return INT_MAX;
				}
				else
				{
					*p_sum += st[index].end - cur_t;
					cur_t = st[index].end;
					cnt++;
					if (*p_sum > HALF)
					{
						return INT_MAX;
					}
				}
			}
		}
		else
		{
			if (flg[cnt])
			{
				is_c = !is_c;
				change++;
			}
			cnt++;
		}
	}

	int *p_sum1 = is_c ? &sum_c : &sum_j;
	
	int end_len = (HALF * 2) - cur_t;
	if (end_len + *p_sum1 > HALF)
	{
		cur_t += HALF - *p_sum1;
		*p_sum1 = HALF;
		is_c = !is_c;
		change++;
	}

	int *p_sum2 = is_c ? &sum_c : &sum_j;
	*p_sum2 += (HALF * 2) - cur_t;
	if (*p_sum2 > HALF)
	{
		return INT_MAX;
	}

	if (is_first_c != is_c) change++;

	return change;
}


signed main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> AC >> AJ;
		int cnt = 0;
		int min_start = INT_MAX;
		for (int i = 0; i < AC; i++)
		{
			cin >> st[cnt].start >> st[cnt].end;
			st[cnt].is_c = true;
			min_start = MIN(st[cnt].start, min_start);
			cnt++;
		}
		for (int i = 0; i < AJ; i++)
		{
			cin >> st[cnt].start >> st[cnt].end;
			st[cnt].is_c = false;
			min_start = MIN(st[cnt].start, min_start);
			cnt++;
		}

		for (int i = 0; i < cnt; i++)
		{
			st[i].start -= min_start;
			st[i].end -= min_start;
		}

		ARY_SORT(st, cnt);

		int d = AC + AJ;
		bool flg[4];
		int min_change = INT_MAX;
		if (d == 1)
		{
			for (int i = 0; i < 4; i++)
			{
				flg[0] = ((i & 1) > 0);
				flg[1] = ((i & 2) > 0);
				min_change = MIN(check(2, flg, true), min_change);
				min_change = MIN(check(2, flg, false), min_change);
			}
		}
		else
		{
			for (int i = 0; i < 16; i++)
			{
				flg[0] = ((i & 1) > 0);
				flg[1] = ((i & 2) > 0);
				flg[2] = ((i & 4) > 0);
				flg[3] = ((i & 8) > 0);
				min_change = MIN(check(4, flg, true), min_change);
				min_change = MIN(check(4, flg, false), min_change);
			}
		}

	/*	flg[0] = true;
		flg[1] = true;
		flg[2] = true;
		flg[3] = true;
		min_change = MIN(check(4, flg, true), min_change);*/

		cout << "Case #" << (t + 1) << ": " << min_change << endl;
	}
}
