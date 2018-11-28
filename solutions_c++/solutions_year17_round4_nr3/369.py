#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cassert>
#include <queue>
#include <map>

using namespace std;



struct LaserData
{
	int r;
	int c;
	bool vertok;
	bool horizok;
	set<int> vert;
	set<int> horiz;
};

 bool shootLaser(char *grid, int R, int C, int i, int j, int dirx, int diry, set<int> &visited)
{
	while (true)
	{
		i += dirx;
		j += diry;
		//cout << i << " " << j << " " << grid[j*C + i] << endl;
		if (i < 0 || i >= C || j < 0 || j >= R)
			return true;
		if (grid[j*C + i] == '#')
			return true;
		if (grid[j*C + i] == '|' || grid[j*C + i] == '-')
			return false;
		if (grid[j*C + i] == '\\')
		{
			return shootLaser(grid, R, C, i, j, diry, dirx, visited);
		}
		if (grid[j*C + i] == '/')
		{
			return shootLaser(grid, R, C, i, j, -diry, -dirx, visited);
		}
		assert(grid[j*C + i] == '.');
		visited.insert(j*C + i);
	}
}

vector<LaserData> findLasers(char *grid, int R, int C)
{
	vector<LaserData> result;
	for (int i = 0; i<C; i++)
	{
		for (int j = 0; j < R; j++)
		{
			if (grid[j*C+i] == '|' || grid[j*C+i] == '-')
			{
				LaserData ld;
				ld.r = j;
				ld.c = i;
				// check horizontal laser
				ld.horizok = shootLaser(grid, R, C, i, j, 1, 0, ld.horiz);
				ld.horizok &= shootLaser(grid, R, C, i, j, -1, 0, ld.horiz);
				ld.vertok = shootLaser(grid, R, C, i, j, 0, 1, ld.vert);
				ld.vertok &= shootLaser(grid, R, C, i, j, 0, -1, ld.vert);
				result.push_back(ld);
			}
		}
	}	
	return result;
}

void doCase()
{
	int R, C;
	cin >> R >> C;
	char *grid = new char[R*C];

	set<int> open;
	for (int i = 0; i < R*C; i++)
	{
		cin >> grid[i];
		if (grid[i] == '.')
			open.insert(i);
	}
	vector<LaserData> lasers = findLasers(grid, R, C);
	int nlasers = lasers.size();
	set<int> forced;
	vector<char> orients;
	orients.resize(nlasers);

	vector<int> lasersleft;

	for (int i = 0; i < nlasers; i++)
	{
		LaserData &ld = lasers[i];
		if (!ld.horizok && !ld.vertok)
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		if (!ld.horizok)
		{
			forced.insert(ld.vert.begin(), ld.vert.end());
			orients[i] = '|';
		}
		else if (!ld.vertok)
		{
			forced.insert(ld.horiz.begin(), ld.horiz.end());
			orients[i] = '-';
		}
		else
			lasersleft.push_back(i);
	}

	vector<int> remaining;
	for (set<int>::iterator it = open.begin(); it != open.end(); ++it)
		if (forced.count(*it) == 0)
			remaining.push_back(*it);

	for (int brute = 0; brute < (1 << lasersleft.size()); brute++)
	{
		set<int> accum;
		int val = brute;
		for (int i = 0; i < lasersleft.size(); i++)
		{
			int bit = val % 2;
			if (bit == 0)
			{
				accum.insert(lasers[lasersleft[i]].horiz.begin(), lasers[lasersleft[i]].horiz.end());
			}
			else
			{
				accum.insert(lasers[lasersleft[i]].vert.begin(), lasers[lasersleft[i]].vert.end());
			}
			val /= 2;
		}
		bool ok = true;
		for (int i = 0; i < remaining.size(); i++)
		{
			if (accum.count(remaining[i]) == 0)
			{
				ok = false;
				break;
			}
		}
		if (!ok)
			continue;
		cout << "POSSIBLE" << endl;
		val = brute;
		for (int i = 0; i < lasersleft.size(); i++)
		{
			int bit = val % 2;
			if (bit == 0)
				orients[lasersleft[i]] = '-';
			else
				orients[lasersleft[i]] = '|';
			val /= 2;
		}
		for (int i = 0; i < lasers.size(); i++)
		{
			LaserData &ld = lasers[i];
			grid[ld.c + C*ld.r] = orients[i];
		}
		for (int j = 0; j < R; j++)
		{
			for (int i = 0; i < C; i++)
			{
				cout << grid[j*C + i];
			}
			cout << endl;
		}
		return;
	}
	
	cout << "IMPOSSIBLE" << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		doCase();
	}
}

