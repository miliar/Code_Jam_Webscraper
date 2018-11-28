#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>
#include <set>

using namespace std;

#define mp(a, b) make_pair(a,b)

int e(int n, int k)
{
	if (k == 1)
		return n;
	int st = 0;
	int k0 = k;
	int mod = k % 2;
	while (k>1)
	{
		mod += k % 2;
		k /= 2;
		st++;

	}
	if (mod>0)
	{
		mod = 1;
	}
	k = k0;

	for (int i = 0;i < st-1;i++)
	{
		n--;
		n /= 2;
	}
	
	n /= 2;
	return n;
}

void f()
{
	int n,m;
	cin >> n >> m;
	vector<int> ing(n);
	for (int i = 0;i < n;i++)
	{
		cin >> ing[i];
	}
	vector<vector<int> > a(n, vector<int>(m));
	for (int i = 0;i < n;i++)
	{
		for (int j = 0;j < m;j++)
		{
			cin >> a[i][j];
		}
		sort(a[i].begin(), a[i].end());
	}
	vector<vector<pair<int,int> > > b(n);
	for (int i = 0;i < n;i++)
	{
		for (int j = 0;j < m;j++)
		{
			int mi = (a[i][j] *10) / (ing[i] * 11);
			int x = (a[i][j] * 10);
			int y = (ing[i] * 11);
			int z = (ing[i] * 9);
			if ((a[i][j] * 10) % (ing[i] * 11) != 0)
				mi++;
			int ma = (a[i][j] * 10) / (ing[i] * 9);
			
			if (mi<=ma)
			{
				b[i].push_back(mp(mi, ma));
			}

		}
	}
	vector<int > u(n);
	for (int i = 0;i < n;i++)
	{
		if (b[i].empty())
		{
			cout << 0;
			return;
		}
		u[i] = 0;
	}
	
	int cnt = 0;
	int out = false;
	while (true)
	{
		
		if (out) {
			break;
		}
		
		int maf = -1e9;
		int fir_i = -1;
		int mis = 1e9;
		int sec_i = -1;
		for (int i = 0;i < n;i++)
		{
			if (b[i][u[i]].first > maf)
			{
				maf = b[i][u[i]].first;
				fir_i = i;
			}
			if (b[i][u[i]].second < mis)
			{
				mis = b[i][u[i]].second;
				sec_i = i;
			}
			
		}
		while (maf>mis) 
		{
			u[sec_i]++;
			if (u[sec_i] >= b[sec_i].size())
			{
				out = true;
				break;
			}
			maf = -1e9;
			fir_i = -1;
			mis = 1e9;
			sec_i = -1;
			for (int i = 0;i < n;i++)
			{
				if (b[i][u[i]].first > maf)
				{
					maf = b[i][u[i]].first;
					fir_i = i;
				}
				if (b[i][u[i]].second < mis)
				{
					mis = b[i][u[i]].second;
					sec_i = i;
				}
			}
		}
		if (out) {
			break;
		}
		else
		{
			cnt++;
			vector<int> tmp(m);
			for (int i = 0;i < n;i++)
			{
				u[i]++;
				if (u[i] >= b[i].size())
				{
					out = true;
					break;
				}
			}
		}
	}
	cout << cnt;
}


int main() {
	int n;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> n;
	for (int i = 0;i < n;i++)
	{
		cout << "Case #" << i + 1 << ": ";
		f();
		cout << endl;
	}

	return 0;
}