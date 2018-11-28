#include <iostream>
#include <cstdlib>
#include <cmath>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <random>

using namespace std;

bool N[1000];

void solve(long long n, long long k, long long &mn, long long  &mx)
{
	long long l = floor(log2(k)) + 1;
	long long t = 1;
	long long s = 0;
	for (int i = 0; i < l - 1; i++)
	{
		s += t;
		t *= 2;
	}
	long long m = 1;
	for (int i = 1; i < l; i++)
	{
		m *= 2;
	}
	long long j = max(1ll, (long long) ceil((n - k + 1) / (double)m));
	if (j % 2 == 0) {
		mx = j / 2;
		mn = (j / 2) - 1;
		//cout << (j / 2) << " " << (j / 2) - 1;
	}
	else {
		mx = j / 2;
		mn = j / 2;
		//cout << (j / 2) << " " << (j / 2);
	}
}
int countLeft(int p, int n)
{
	int count = 0;
	for (int i = p - 1; i >= 0; i--)
	{
		if (N[i])
			break;
		count++;
	}
	return count;
}
int countRight(int p, int n)
{
	int count = 0;
	for (int i = p + 1; i < n; i++)
	{
		if (N[i])
			break;
		count++;
	}
	return count;
}
void brute(int n, int k, int &mn, int &mx)
{
	int pos;
	for (int i = 0; i < k; i++)
	{
		mn = -1;
		mx = -1;
		for (int j = 0; j < n; j++)
		{
			if (N[j])
				continue;
			int l = countLeft(j, n);
			int r = countRight(j, n);

			int tmn = min(l, r);
			int tmx = max(l, r);

			if (mn < tmn)
			{
				mn = tmn;
				mx = tmx;
				pos = j;
			}
			else if (mn == tmn)
			{
				if (mx < tmx)
				{
					mx = tmx;
					pos = j;
				}
			}
		}
		N[pos] = 1;
	}
}
void test()
{
	random_device rd, rd2;
	mt19937 gen(rd()), gen2(rd2());
	uniform_int_distribution<int> dis(1, 100);
	vector<pair<int, int>> tests;
	tests.push_back(make_pair(4, 2));
	tests.push_back(make_pair(5, 2));
	tests.push_back(make_pair(6, 2));
	tests.push_back(make_pair(1000, 1000));
	tests.push_back(make_pair(1000, 1));
	for (int i = 0; i < 1000; i++)
	{
		int n = dis(gen);
		uniform_int_distribution<int> dis2(1, n);

		int k = dis2(gen2);
		tests.push_back(make_pair(n, k));
	}
	for(int i=0;i<tests.size();i++)
	{
		memset(N, 0, sizeof(N));
		
		int n = tests[i].first;
		int k = tests[i].second;

		int bmn, bmx;
		long long smn, smx;

		brute(n, k, bmn, bmx);
		solve(n, k, smn, smx);

		cout << n << " " << k << " " << bmx << " " << bmn << " " << smx << " " << smn << " " << (bmn == smn && bmx == smx?"PASS":"FAIL") << "\n";
	}
}
int main()
{
	/*test();
	return 0;*/
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		memset(N, 0, sizeof(N));
		cout << "Case #" << c << ": ";
		long long n, k;
		cin >> n >> k;
		long long mn, mx;
		solve(n, k, mn, mx);
		cout << mx << " " << mn;
		cout << "\n";
	}
	return 0;
}