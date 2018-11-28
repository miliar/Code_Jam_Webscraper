#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <string>

using namespace std;

void solve()
{
	int n;
	int r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	std::string out;
	int rt = r + o + v;
	int yt = y + o + g;
	int bt = b + g + v;
	if(rt >n/2 || yt > n/2 || bt >n/2 || o > b || g > r || v > y)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	
	for(int i =0 ;i < o;++i)
	{
		out.push_back('O');
		out.push_back('b');
	}
	b -=o;
	for(int i =0 ;i < g;++i)
	{
		out.push_back('G');
		out.push_back('R');
	}
	r -=g;
	for(int i =0 ;i < v;++i)
	{
		out.push_back('V');
		out.push_back('Y');
	}
	y =y-v;
	multimap<int, char> m;
	m.insert(make_pair(r, 'R'));
	m.insert(make_pair(y, 'Y'));
	m.insert(make_pair(b, 'B'));
	
	
	auto it = m.rbegin();
	auto it1 = it++;
	auto it2 = it++;
	auto it3 = it++;
	for(int i =0; i < (it2->first + it3->first - it1->first);++i)
	{
		out.push_back(it1->second);
		out.push_back(it2->second);
		out.push_back(it3->second);
	}

	for(int i =0; i< (it1->first - it3->first);++i)
	{
		out.push_back(it1->second);
		out.push_back(it2->second);
	}

	for(int i=0; i < (it1->first - it2->first);++i)
	{
		out.push_back(it1->second);
		out.push_back(it3->second);
	}
	printf("%s\n", out.c_str());
}


int main()
{
	int t;
	std::cin >> t;
	for(int i =1; i <=t;++i)
	{
		printf("Case #%d: " , i);
		solve();
	}
	return 0;
}

