
//https://open.kattis.com/users/joseph-scott


#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <sstream>
#include <cstdint>
#include <cmath>
#include <vector>

using namespace std;

pair<long long, long long> sim(long long n, long long k)
{
	set<int> is_open;
	is_open.insert(0);
	is_open.insert(n + 1);
	pair<long long, long long> ret = make_pair(long long(0), long long(0));
	int last_left = 0;

	while (k)
	{
//		ret = ret = make_pair(long long(0), long long(0));
		vector<pair<pair<int ,int>,int>> best;
		int best_val = -1;
		for (int i = 0; i < n; i++)
		{
			if (is_open.count(i+1)==0)
			{
				auto ls_ptr = (is_open.lower_bound(i + 1));
				ls_ptr --;
				int ls = i - *ls_ptr ;
				auto rs = (*is_open.upper_bound(i + 1)) - i -2 ;
				if (min(ls, rs) == best_val)
				{
					best.push_back(make_pair(make_pair(ls, rs),i));
				}
				if (min(ls, rs) > best_val)
				{
					best.clear();
					best.push_back(make_pair(make_pair(ls, rs),i));
					best_val = min(ls, rs);
				}
			}
			else
			{
				continue;
			}
		}
		int tie_break = -1;
		int select = -1;
		for (int i = 0; i < best.size(); i++)
		{
			if (max(best[i].first.first, best[i].first.second) > tie_break)
			{
				select = i;
				tie_break = max(best[i].first.first, best[i].first.second);
			}
		}
		ret = make_pair(best[select].first.first, best[select].first.second);
		is_open.insert(best[select].second + 1);
		k--;
	}
	return ret;
}


pair<long long, long long> split(long long n)
{
	if (n == 1)
	{
		return make_pair(0, 0);
	}
	if (n == 2)
	{
		return make_pair(1, 0);
	}
	n--;
	pair<long long, long long> p(0, n / 2);
	if (n / 2 + n / 2 == n)
	{
		p.first = n / 2;
	}
	else
	{
		p.first = n / 2 + 1;
	}
	return p;
}

pair<long long, long long> try2_ans(long long n)
{
	if (n == 0)
	{
		return make_pair(0, 0);
	}
	if (n == 1)
	{
		return make_pair(1, 0);
	}
}

pair<long long, long long> try2(long long n, long long k)
{
	map<long long, long long> nums;
	pair<long long, long long> p;
	nums.insert(make_pair(n, 1));
	while (k)
	{
		int highest = nums.rbegin()->first;
		nums[highest]--;
		if (nums[highest] == 0)
		{
			nums.erase(highest);
		}
		p = split(highest);
		if (nums.count(p.first) == 0)
		{
			nums.insert(make_pair(p.first, 0));
		}
		nums[p.first]++;

		if (nums.count(p.second) == 0)
		{
			nums.insert(make_pair(p.second, 0));
		}
		nums[p.second]++;
		k--;
	}
	return p;
}

pair<long long, long long> try3(long long n, long long k)
{

	if (n == k)
	{
		return make_pair(0, 0);
	}
	if (2 * k > n)
	{
	//	return make_pair(1, 0);
	}


	map<long long, long long> nums;
	pair<long long, long long> p;
	nums.insert(make_pair(n, 1));
	while (1)
	{
		long long highest = nums.rbegin()->first;
		p = split(highest);
		if (k <= nums[highest]) return p;
		if (nums.count(p.first) == 0)
		{
			nums.insert(make_pair(p.first, 0));
		}
		nums[p.first]+= nums[highest];

		if (nums.count(p.second) == 0)
		{
			nums.insert(make_pair(p.second, 0));
		}
		nums[p.second]+= nums[highest];
		k-= nums[highest];
		nums.erase(highest);
	}
}



int main()
{
#if 1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int ncase; cin >> ncase;
	for (int icase = 1; icase <= ncase; icase++)
	{
		cerr << icase << " / " << ncase << endl;
		long long n, k; cin >> n >> k;
		//auto ans = sim(n, k);
//		auto ans2 = try2(n, k);

		auto ans3 = try3(n, k);
		//cout << "Case #" << icase << ": " << ans.second << " " << ans.first<<"\t"<< ans2.first<<" "<<ans2.second<< endl;
		//cout << "Case #" << icase << ": " << ans2.first<<" "<<ans2.second<< "\t"<<ans3.first << " " << ans3.second<<endl;
		cout << "Case #" << icase << ": " << ans3.first << " " << ans3.second << endl;
		//if (ans2 != ans3)
	}
}
