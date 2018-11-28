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

const int MAXN = 55;
int n, p;
int rr[MAXN];
int q[MAXN][MAXN];
int l[MAXN][MAXN], r[MAXN][MAXN];

bool chk(int x, int y, int z)
{
	if(x * 10 > y * z * 11) return false;
	if(x * 10 < y * z * 9) return false;
	return true;
}

int main()
{
	int Test;
	cin >> Test;
	for(int t = 1; t <= Test; t++)
	{
		int ans = 0;
		cin >> n >> p;
		for(int i = 1; i <= n; i++)
			cin >> rr[i];
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= p; j++)
			{
				cin >> q[i][j];
				l[i][j] = 10000000;
				r[i][j] = 0;
				r[i][j] = q[i][j] * 10 / 9 / rr[i];
				l[i][j] = (q[i][j] * 10 - 1) / 11 / rr[i] + 1;
			}
		
		for(int c = 1; c <= 1000000; c++)
		{
			bool f = 1;
			for(int i = 1; i <= n; i++)
			{
				bool g = 0;
				for(int j = 1; j <= p; j++)
				{
					if(l[i][j] <= c && r[i][j] >= c)
					{
						g = 1;
						break;
					}
				}
				if(!g)
				{
					f = 0;
					break;
				}
			}
			if(f)
			{
				ans++;
				for(int i = 1; i <= n; i++)
				{
					int best = 0;
					for(int j = 1; j <= p; j++)
					{
						
						if(l[i][j] <= c && r[i][j] >= c)
						if(best == 0 || r[i][j] < r[i][best])
						best = j;
					}
					r[i][best] = 0;
				}
				c--;
			}
		}
		
		
		cout << "Case #" << t << ": " << ans << endl;
	}
	
	return 0;
}

