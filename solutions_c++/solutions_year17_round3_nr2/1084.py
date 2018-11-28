#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
#include <climits>
#include <queue>
#include <numeric>
#include <thread>
#include <bitset>
#include<math.h>
using namespace std;
#define MAXN 1005
int N, K,Q;
struct Interval
{
	int s, e;
	int interv;
	int user;
	Interval(int a, int b, int c) :s(a), e(b), user(c) { interv = e - s; };
};

double f[MAXN][MAXN];
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	int Q, N, M,s,e;
	cin >> Q;
	vector<Interval> intervals;
	for (size_t q = 0; q < Q; q++)
	{
		cin >> N >> M;
		int remainA=720, remainB=720;
		int mins,mine;
		mins = INT_MAX;
		intervals.clear();
		for (size_t i = 0; i < N; i++)
		{
			cin >> s >> e;
			if (s < mins)
			{
				mins = s;
				mine = e;
			}
			intervals.emplace_back(Interval(s, e, 0));
			remainA -= e - s;
		}
		if (N) intervals.emplace_back(Interval(mins+1440, mine+1440, 0));
		mins = INT_MAX;
		for (size_t i = 0; i < M; i++)
		{
			cin >> s >> e;
			if (s < mins)
			{
				mins = s;
				mine = e;
			}
			intervals.emplace_back(Interval(s, e, 1));
			remainB -= e - s;
		}
		if (M) intervals.emplace_back(Interval(mins + 1440, mine + 1440, 1));
		sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b) {return a.s < b.s; });
		int time;
		bool find = false;
		int index,minTime;
		while (true)
		{
			find = false;
			minTime = INT_MAX;
			for (int i = 0; i < intervals.size()-1; i++)
			{
				if (intervals[i].user == intervals[i + 1].user)
				{
					time = intervals[i + 1].s - intervals[i].e;
					if (intervals[i].user)
					{
						if (time <= remainB)
						{
							if (time < minTime)
							{
								minTime = time;
								index = i;
							}
							find = true;
						}
					}
					else
					{
						if (time <= remainA)
						{
							if (time < minTime)
							{
								minTime = time;
								index = i;
							}
							find = true;
						}
					}
				}
			}
			if (!find) break;
			else
			{
				if (intervals[index].user)
					remainB -= minTime;
				else
					remainA -= minTime;
				intervals[index].e += minTime;
				intervals.erase(intervals.begin() + index);
			}
		}
		int ans = 0;
		int size = intervals.size();
		if (M)
			size--;
		if (N)
			size--;
		for (size_t i = 0; i <size; i++)
		{
			if (intervals[i].user != intervals[i + 1].user)
				ans += 1;
			else
				ans += 2;
		}
		cout << "Case #" << q + 1 << ": " << ans << endl;

	}
	return 0;
}
