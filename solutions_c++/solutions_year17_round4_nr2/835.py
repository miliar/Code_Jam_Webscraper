#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;


void solve(int test)
{

	int n, c, m;
	cin >> n >> c >> m;
	vector<pair<int, int> > v(m);
	multiset<pair<int, int> > msAll;
	for (int i = 0; i < m; ++i)
	{
		cin >> v[i].first >> v[i].second;	//pos and buyer
		v[i].first--;
		msAll.insert(v[i]);
	}
	int cnt = 0;
	sort(v.begin(), v.end());
	vector<pair<int, int> > rest;
	rest = v;
	while (rest.size() != 0)
	{
		cnt++;
		int cursit = 0;
		int lastpos = 0;
		vector<pair<int, int> > nextRest;
		set<int> pass;
		for (int i = 0; i < rest.size(); ++i)
		{
			if (pass.find(rest[i].second) != pass.end())
			{
				nextRest.push_back(rest[i]);
				continue;
			}
			if (rest[i].first >= lastpos)
			{
				lastpos++;
				pass.insert(rest[i].second);
			}
			else
			{
				nextRest.push_back(rest[i]);
			}
		}
		rest = nextRest;
	}
	vector<vector<char> > roll(cnt, vector<char>(n, false));
	vector<int> ptr(cnt, 0);
	vector<set<int> > rollPass(cnt);
	int ansProm = 0;
	rest.clear();
	rest = v;
	
	map<int, int> ma;
	for (int i = 0; i < rest.size(); ++i)
	{
		ma[rest[i].first]++;
	}
	for (auto it = ma.begin(); it != ma.end(); ++it)
	{
		if (it->second > cnt)
		{
			ansProm += it->second - cnt;
		}
	}


	printf("Case #%d: %d %d\n", test, cnt, ansProm);
	
}


int main() {
#ifdef _CONSOLE
	freopen("B-small-attempt2 (1).in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int testNum;
	cin >> testNum;
	for (int test = 1; test <= testNum; ++test)
	{
		solve(test);
	}			

	return 0;
}