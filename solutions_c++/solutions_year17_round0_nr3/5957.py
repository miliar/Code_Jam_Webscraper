#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
typedef long long int ll;
using namespace std;

vector <ll> stall_start, stall_end;
//vector <int> next_start, next_end;
//leftmost = 0, rightmost = n+1 = (n+2)-1

class Stall
{
public:
	ll stall_start, stall_end;
	ll diff;

	void calc ()
	{
		diff = stall_end-stall_start;
	}
};

bool comp (Stall a, Stall b)
{
	if (a.diff > b.diff) return true;
	else if (a.diff < b.diff) return false;
	else
	{
		if (a.stall_start < b.stall_start) return true;
		else return false;
	}
}

int mysort ()
{
	vector <Stall> stall;
	stall.resize(stall_start.size());

	for (ll i=0; i<stall_start.size(); i++)
	{
		stall[i].stall_start = stall_start[i];
		stall[i].stall_end = stall_end[i];
		stall[i].calc();
	}

	sort(stall.begin(), stall.end(), comp);

	for (ll i=0; i<stall_start.size(); i++)
	{
		stall_start[i] = stall[i].stall_start;
		stall_end[i] = stall[i].stall_end;
	}

}

int main (void)
{
	int t;
	ll k, n, steps, limit;
	ll curr_diff;
	ll l, r, mid;
	ll minlr, maxlr;

	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cin >> n >> k;

		steps = 0;
		limit = 0;
		stall_start.push_back(0);
		stall_end.push_back(n+1);
		l = stall_start[0];
		r = stall_end[0];
		mid = (l+r)/2;

		while (steps < k)
		{
			steps++;

			l = stall_start[0];
			r = stall_end[0];
			curr_diff = r-l-1;
			mid = (l+r)/2;
			//cout << "step #" << steps << endl;
			//printf("l: %lld\nr: %lld\nmid: %lld\n", l, r, mid);
			//cout << "curr_diff: " << curr_diff << endl << endl;

			if (curr_diff == 0) //no space in between
			{
				stall_start.erase(stall_start.begin());
				stall_end.erase(stall_end.begin());
				continue;
			}
			if (steps <= limit)
			{
				//cout << "here\n";
				stall_start.erase(stall_start.begin());
				stall_end.erase(stall_end.begin());
				continue;
			}
			if (curr_diff % 2 == 1) //there is a midpoint
			{
				stall_start.push_back(l);
				stall_end.push_back(mid);

				stall_start.push_back(mid);
				stall_end.push_back(r);

				mysort();
				/*
				if ((mid-l-1) % 2 == 0) //if the space that is split is even
				{
					ll midl = (mid+l)/2;
					ll midr = (r+mid)/2;

					stall_start.push_back(midl);
					stall_end.push_back(mid);

					stall_start.push_back(midr);
					stall_end.push_back(r);

					stall_start.push_back(l);
					stall_end.push_back(midl);

					stall_start.push_back(mid);
					stall_end.push_back(midr);

					limit = steps+2;
				}
				*/
			}
			else //even, no midpoint
			{
				stall_start.push_back(mid);
				stall_end.push_back(r);

				stall_start.push_back(l);
				stall_end.push_back(mid);

				mysort();
			}

			stall_start.erase(stall_start.begin());
			stall_end.erase(stall_end.begin());
		}

		//at this point, steps = k
		//mid, l, r should be the same
		//printf("l: %lld\nr: %lld\nmid: %lld\n\n", l, r, mid);
		maxlr = max(mid-l-1, r-mid-1);
		minlr = min(mid-l-1, r-mid-1);

		stall_start.clear();
		stall_end.clear();
		printf("Case #%d: %lld %lld\n", i, maxlr, minlr);
	}
}