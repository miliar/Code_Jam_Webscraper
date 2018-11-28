#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <list>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <sstream>
using namespace std;
typedef signed long long int lli;
typedef vector<int> vi;
#define FOR(i, p, n) for(int i(p); i < n; i++)
#define FORR(i,p) for( i(p); i>=0; i--)
#define ALL(a) (a.begin()),(a.end())
#define sqr(x) ((x)*(x))
#define sqrt(x) sqrt(1.0*(x))
#define pow(x,n) pow(1.0*(x),n)
#define FORI(n) for(int i=0;i<n;i++)
#define sz(V) (int)V.size()
#define pb push_back
#define UN(x) (x).resize(unique(ALL((x))) - (x).begin());
#define mp make_pair
const int INF = 1000000000;
const int N = 1000000;
int t[N * 4];
int sum(int v, int tl, int tr, int l, int r)
{
	if (l>r) return 0;
	if (tl == l && tr == r)
	{
		return t[v];
	}
	else
	{
		int tm = (tl + tr) / 2;
		return max(sum(v * 2, tl, tm, l, min(r, tm)), sum(v * 2 + 1, tm + 1, tr, max(tl + 1, l), r));
	}
}
void update(int v, int tl, int tr, int pos, int val)
{
	if (tl == tr)
	{
		t[v] = val;
	}
	else
	{
		int tm = (tl + tr) / 2;
		if (tm <= pos)
			update(v * 2, tl, tm, pos, val);
		else update(v * 2 + 1, tm + 1, tr, pos, val);
		t[v] = max(t[v * 2], t[v * 2 + 1]);
	}
}
bool solve()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i(0); i < t; i++)
	{
		int n, k;
		cin >> n >> k;
		multiset < int >a;
		a.insert(n);
		int L(0), R(0);
		for (int j(0); j < k; j++)
		{
			multiset<int>::iterator it = a.end();
			it--;
			int tmp = *it;
			a.erase(it);
			a.insert(tmp / 2);
			if (tmp & 1)
			{
				if (tmp / 2) a.insert(tmp / 2);
				L = tmp / 2;  R = tmp / 2;
			}
			else  {
				if(tmp/2-1>0) a.insert(tmp / 2 - 1);
					L = tmp / 2 - 1;  R = tmp / 2;
			}
			L = max(L, 0);
			R = max(R, 0);
		}
		cout << "Case #" << i + 1 << ": " << max(L, R) << " "<<min(L, R) << endl;
	}
	return 1;
}
int main()
{
	solve();
	//while (solve());
	return 0;
}