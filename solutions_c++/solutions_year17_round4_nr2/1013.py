#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#define MAX_N 1001
using namespace std;
int n,m,c;
int tab[MAX_N][MAX_N];
void clear()
{
	for (int i = 0; i < MAX_N; ++i)
		for (int j = 0; j < MAX_N; ++j)
			tab[i][j] = 0;
}

int check(int m) {
	vector<int> sie(MAX_N);
	int sum = 0;
	int res = 0;
	for (int i = 1; i <= c; ++i)
	{
		
		for (int j = n; j >= 1; --j)
		{
			int tmp = tab[i][j];
			int t = m - sie[j]-tmp;
			if (t < 0)
			{
				sum += -t;
				sie[j] = m;
			}
			else
			{
				sie[j] += tmp;
			}

			t = m - sie[j] - sum;
			int nsum = 0;
			if (t < 0)
			{
				nsum = -t;
				sie[j] = m;
			}
			else
			{
				sie[j] += sum;
			}
			res += sum - nsum;
			sum = nsum;
		}
		if (sum != 0)return -1;
		sum = 0;
	}
	return res;
}
pair<int,int> binSearch(int p, int k)
{
	
	int sr = (k + p) / 2;
	
	int z = check(sr);	
	if (p == k)return make_pair(p, z);
	if (sr == p && z!=-1)return make_pair(sr,z);
	
	if (z != -1)return binSearch(p, sr);
	if (sr == k - 1 && z==-1)return make_pair(k, check(k));
	
	return binSearch(p, sr);
}
void solve()
{
	int ma = 0;
	int s = 0;
	for (int i = 1; i <= c; ++i)
	{
		s = 0;
		for (int j = 1; j <= n; ++j)
			s += tab[i][j];
		ma = max(ma, s);
	}
	auto res = binSearch(ma, m);
	cout << res.first << " " << res.second<<"\n";
}
void input()
{
	cin >> n >> c >> m;
	for (int i = 0; i < m; ++i)
	{
		int a, b;
		cin >> a >> b;
		tab[b][a]++;
	}
}
int main()
{
	int t, m, n;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		clear();
		input();
		printf("Case #%d: ", k);
		solve();
	}
}