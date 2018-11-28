#include <bits/stdc++.h>
using namespace std;
const int mxn = 1010;

int n, c, m;
vector < pair <int, int> > bil;
int ile_wolnych[mxn], ile_za_duzo[mxn];

vector < pair <int, int> > usun_vec(vector < pair <int, int> > a, vector < pair <int, int> > b)
{
	vector < pair <int, int> > ret;
	
	sort(a.begin(), a.end());
	
	sort(b.begin(), b.end());
	reverse(b.begin(), b.end());
	
	for(auto p : a)
	{
		if(b.size() > 0 && p == b.back())
			b.pop_back();
		else
			ret.push_back(p);
	}
	return ret;
}

int rozw()
{
	int ret = 0;
	int ile_ludzi = 0;
	int ile_w_miejscu[mxn];
	bool wziety[mxn];
	
	for(int i = 1 ; i <= c ; i++)
		wziety[i] = false;
		
	for(int i = 1 ; i <= n ; i++)
		ile_w_miejscu[i] = 0;
		
	vector < pair <int, int> > usun;
	
	for(auto p : bil)
	{
		if(ile_ludzi == p.first)
			continue;
			
		if(wziety[p.second] == true)
			continue;
			
		usun.push_back(p);
		ile_ludzi++;
		wziety[p.second] = true;
		ile_w_miejscu[p.first]++;
	}
	
	bil = usun_vec(bil, usun);
	
	
	for(int i = 1 ; i <= n ; i++)
	{
		ile_za_duzo[i] += max(0, ile_w_miejscu[i] - 1);
		
		if(ile_w_miejscu[i] == 0)
			ile_wolnych[i]++;
			 
		ret += max(0, ile_w_miejscu[i] - 1);
	}
	return ret;
}

pair <int, int> solve()
{
	scanf("%d%d%d", &n, &c, &m);
	for(int i = 1 ; i <= n ; i++)
	{
		ile_wolnych[i] = 0;
		ile_za_duzo[i] = 0;
	}
	bil.clear();
	for(int i = 0 ; i < m ; i++)
	{	
		int a, b;
		scanf("%d%d", &a, &b);
		bil.push_back({a, b});
	}
	sort(bil.begin(), bil.end());
	int ile_razy = 0, ile_przeniesien = 0;
	while(bil.size() > 0)
	{
		ile_razy++;
		ile_przeniesien += rozw();
	}
	for(int i = 1 ; i <= n ; i++)
		ile_przeniesien -= min(ile_wolnych[i], ile_za_duzo[i]);
	return {ile_razy, ile_przeniesien};
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1 ; i <= t ; i++)
	{
		printf("Case #%d: ", i);
		auto v = solve();
		printf("%d %d\n", v.first, v.second);
	}
}
