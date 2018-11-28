#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("a.out");

const int MAXN = 1005;
int a[MAXN];
int ma;
int n, m, c;
int stc[MAXN];
int ans1 = 0;

bool chk(int mid)
{
	int r = 0;
	for(int i = n; i >= 1; i--)
	{
		r += a[i];
		r -= mid;
		if(r < 0) r = 0;
	}
	if(r == 0) return true;
	return false;
	
}

int work()
{
	memset(a, 0, sizeof(a));
	memset(stc, 0, sizeof(stc));
	
	cin >> n >> c >> m;
	
	for(int i = 1; i <= m; i++)
	{
		int p, q;
		cin >> q >> p;
		stc[p]++;
		a[q]++;
	}
	ma = 0;
	for(int i = 1; i <= c; i++)
	if(stc[i] > ma) ma = stc[i];
	
	int l = ma;
	int r = m;
	while(l < r)
	{
		int mid = (l + r) / 2;
		if(chk(mid)) r = mid;
		else l = mid + 1;
	}
	ans1 = l;
	
	int ans = 0;
	for(int i = 1; i <= n; i++)
	{
		if(a[i] > l)
			ans += a[i] - l;
	}
	//cout << a[1] << ' ' << a[2] << "::" <<endl;
	return ans;
}

int main()
{
	int Test;
	cin >> Test;
	for(int test = 1; test <= Test; test++)
	{
		int ans = 0;
		
		ans = work();
		
		cout << "Case #" << test << ": " << ans1 << ' ' << ans << endl;
	}
	
	return 0;
}
/*
5
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1
*/

