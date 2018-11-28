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

#define N 720

typedef long long ll;

const int inf = 1e8;
int d[2*N+1][N+1][2];
int n, m, t;

void cover_interval(int from, int to, int last, int val)	{
	for (int i = from; i <= to; i++)
		for (int l = 0; l <= N; l++) 
			d[i][l][last] = val;
}

int main() {

	//freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);

	cin >> t;
	int testcase = 0, ab, ae;
	while (t--)	{
		cin >> n >> m;
		
		cover_interval(0,2*N,0,inf/2);
		cover_interval(0,2*N,1,inf/2);
		
		for (int i = 0; i < n; i++)
		{	
			cin >> ab >> ae;
			cover_interval(ab+1,ae,0,inf);
		}
		for (int i = 0; i < m; i++)
		{
			cin >> ab >> ae;
			cover_interval(ab+1,ae,1,inf);
		}
	
		d[0][0][0] = d[0][0][1] = 0;
		for (int i = 1; i <= 2*N; i++)
			for (int j = 0; j <= min(i,N); j++)
			{	
				if (j == 0)
				{
					d[i][j][0] = inf;
					if (d[i][j][1] < inf)
						d[i][j][1] = d[i-1][j][1];
					continue;
				}
				
				if (d[i][j][0] < inf)
					d[i][j][0] = min(d[i-1][j-1][0],d[i-1][j-1][1]+1);
					
				if (d[i][j][1] < inf)
					d[i][j][1] = min(d[i-1][j][0]+1,d[i-1][j][1]);
			
			}
			
		/*for (int i = 0; i <= 2*N; i++)
		{
			for (int j = 0; j <= N; j++)
				cout << d[i][j][1] << ' ';
			cout << endl;
		}*/
		testcase++;
		cout << "Case #" << testcase << ": ";
		int ans = min(d[2*N][N][0],d[2*N][N][1]);
		ans += (ans%2);
		cout << ans << endl;
		
		cover_interval(0,2*N,0,0);
		cover_interval(0,2*N,1,0);
	}

	return 0;
}