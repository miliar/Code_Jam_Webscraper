#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <utility>
#include <iomanip> 
#include <queue>

using namespace std;

#define pb push_back

#define N 110

typedef long long ll;

int was[N][N][N], d[N][N][N], a[N], c[N];
int n, p, t;

int check(int c1, int c2, int c3)	{
	if ((c1 + 2*c2 + 3*c3) % p == 0)
		return 1;
	return 0;
}

int dp(int c1, int c2, int c3)	{
	if (was[c1][c2][c3])
		return d[c1][c2][c3];
	
	was[c1][c2][c3] = 1;
	if (c1)
		d[c1][c2][c3] = max(d[c1][c2][c3],dp(c1-1,c2,c3)+check(c1-1,c2,c3));
	if (c2)
		d[c1][c2][c3] = max(d[c1][c2][c3],dp(c1,c2-1,c3)+check(c1,c2-1,c3));
	if (c3)
		d[c1][c2][c3] = max(d[c1][c2][c3],dp(c1,c2,c3-1)+check(c1,c2,c3-1));

	return d[c1][c2][c3];
}

int main() {

	//freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);

	was[0][0][0] = 1;
	cin >> t;
	int testcase = 0;
	while (t--)	{
		int temp;
		cin >> n >> p;
		int cnt1 = 0, cnt2 = 0;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		
		
		c[0] = c[1] = c[2] = c[3] = 0;
		for (int i = 0; i < n; i++)
			c[a[i]%p]++;
		
		testcase++;
		cout << "Case #" << testcase << ": ";
		cout << c[0]+dp(c[1],c[2],c[3]) << endl;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				for (int l = 0; l < N; l++)
					d[i][j][l] = was[i][j][l] = 0;
		was[0][0][0] = 1;
	}

	return 0;
}