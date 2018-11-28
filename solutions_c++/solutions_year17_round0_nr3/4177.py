/*
 * Program.cpp
 *
 *  Created on: Apr 5, 2017
 *      Author: meni
 */

#include <functional>
#include <queue>
#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include <list>

using namespace std;

typedef long long ull;

void solve1(int ct, unsigned long long  n, unsigned long long  k)
{
	bool* arr = new bool[n];

	for (ull j=0;j<n;j++)
	{
		arr[j] = false;
	}

	ull y,z;
	bool multi_max=false;
	bool multi_min=false;
	ull min_index = 0;
	ull max_index = 0;
	ull left_most_index = n;

	for (ull i=0;i<k;i++)
	{
		list< pair<ull,ull> > q;
		y = -1;
		z= 1000000;

		for (ull j=0;j<n;j++)
		{
			if (arr[j])
			{
				continue;
			}

			ull ls = j, rs = n-1-j;
			for (ull x=j;x>=0;x--)
			{
				if (arr[x])
				{
					ls = j-x-1;
					break;
				}
			}

			for (ull x=j;x<=n;x++)
			{
				if (arr[x])
				{
					rs = x-j-1;
					break;
				}
			}

			/*
			if (y == max(ls,rs))
			{
				multi_max = true;
			}

			if (y < max(ls,rs))
			{
				y = max(ls,rs);
				multi_max = false;
				max_index = j;
				if (left_most_index > j)
				{
					left_most_index = j;
				}
			}
			*/

			if (z == min(ls,rs))
			{
				pair<ull,ull> pr = q.front();
				if (pr.second < max(ls,rs))
				{
					q.pop_front();
					q.push_back(make_pair(j, max(ls,rs)));
				}
			}

			if (z < min(ls,rs) || z == 1000000)
			{
				z = min(ls,rs);
				q.clear();
				q.push_back(make_pair(j, max(ls,rs)));
			}
		}

		while (!q.empty())
		{
			pair<ull,ull> pr = q.front();
			q.pop_front();

			if (y < pr.second)
			{
				y = pr.second;
				min_index = pr.first;
			}
			else
			{
				break;
			}
		}

		arr[min_index] = true;
	}

	cout << "Case #" << ct << ": " << y << " " << z << endl;
}

void solve(int ct, ull n, ull k)
{
	auto cmp = [] (pair<ull,ull> left, pair<ull,ull> right)
		{
			if (left.second - left.first == right.second - right.first)
			{
				return left.first < right.first;
			}

			return left.second - left.first < right.second - right.first;
		};

	priority_queue< pair<ull,ull> , vector< pair<ull, ull> > , decltype(cmp)> q(cmp);
	pair<ull, ull> head = make_pair(0, n-1);
	q.push(head);
	ull y,z;

	for (ull i=0;i<k;i++)
	{
		pair<ull,ull> node = q.top();
		q.pop();

		if (node.second - node.first == 0) // 1 stall
		{
			y = z = 0;
			break; // maybe continue to be a saint
		}

		ull mid = node.first + ((node.second - node.first) / 2);

		if ((node.second - node.first) % 2 != 0)
		{
			ull mid1 = node.first + ((node.second - node.first) / 2);
			ull mid2 = mid1+1;

			ull ls1 = mid1 - node.first;
			ull rs1 = node.second - mid1;

			ull ls2 = mid2 - node.first;
			ull rs2 = node.second - mid2;

			if (min(ls1,rs1) < min(ls2,rs2))
			{
				mid = mid1;
			}
			else if (min(ls1,rs1) == min(ls2,rs2))
			{
				if (max(ls1,rs1) <= max(ls2,rs2))
				{
					mid = mid1;
				}
				else
				{
					mid = mid2;
				}
			}
			else
			{
				mid = mid2;
			}
		}

		//ull mid = node.first + ((node.second - node.first) / 2);
		ull ls = mid - node.first;
		ull rs = node.second - mid;

		y = max(ls,rs);
		z = min(ls,rs);

		if (mid - node.first >= node.second - mid)
		{
			q.push(make_pair(node.first,mid-1));
			q.push(make_pair(mid+1,node.second));
		}
		else
		{
			q.push(make_pair(mid+1,node.second));
			q.push(make_pair(node.first,mid-1));
		}
	}

	cout << "Case #" << ct << ": " << y << " " << z << endl;

}

int main()
{
    int ct, t;

    cin >> t;
    for (ct = 1; ct <= t; ct ++)
    {
    	ull n,k;

        cin >> n >> k;
        if (n == k)
        {
        	cout << "Case #" << ct << ": " << "0 0" << endl;
        }
        else
        {
        	solve(ct, n,k);
        	//cout << "Case #" << ct << ": " << solve(n,k) << endl;
        }
    }

    return 0;
}
