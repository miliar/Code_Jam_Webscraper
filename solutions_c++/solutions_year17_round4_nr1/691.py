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

const int MAXN = 105;
int a[MAXN];
int n, p;
int ans;
int best2[MAXN][MAXN];
int best3[MAXN][MAXN][MAXN];

void sv2()
{
	int c = 0;
	for(int i = 1; i <= n; i++)
		if(a[i] == 0)
			c++;
	ans = c + (n - c + 1) / 2;
}

void sv3()
{
	int c = 0, c1 = 0, c2 = 0;
	for(int i = 1; i <= n; i++)
	{
		if(a[i] == 0)
			c++;
		if(a[i] == 1)
			c1++;
		if(a[i] == 2)
			c2++;
	}
	ans = c;
	best2[0][0] = 0;
	best2[1][0] = 1;
	best2[0][1] = 1;
	for(int i = 0; i <= c1; i++)
		for(int j = 0; j <= c2; j++)
		{
			if(i >= 1)
				best2[i][j] = max(best2[i][j], best2[i - 1][j]);
			if(j >= 1)
				best2[i][j] = max(best2[i][j], best2[i][j - 1]);
			if(i >= 3)
				best2[i][j] = max(best2[i][j], best2[i - 3][j] + 1);
			if(j >= 3)
				best2[i][j] = max(best2[i][j], best2[i][j - 3] + 1);
			if(i >= 1 && j >= 1)
				best2[i][j] = max(best2[i][j], best2[i - 1][j - 1] + 1);
		}
	ans += best2[c1][c2];
}

void sv4()
{
	int c = 0, c1 = 0, c2 = 0, c3 = 0;
	for(int i = 1; i <= n; i++)
	{
		if(a[i] == 0)
			c++;
		if(a[i] == 1)
			c1++;
		if(a[i] == 2)
			c2++;
		if(a[i] == 3)
			c3++;
	}
	ans = c;
	best3[0][0][0] = 0;
	best3[1][0][0] = 1;
	best3[0][1][0] = 1;
	best3[0][0][1] = 1;
	for(int i = 0; i <= c1; i++)
		for(int j = 0; j <= c2; j++)
			for(int k = 0; k <= c3; k++)
			{
				if(i >= 1)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 1][j][k]);
				if(j >= 1)
					best3[i][j][k] = max(best3[i][j][k], best3[i][j - 1][k]);
				if(k >= 1)
					best3[i][j][k] = max(best3[i][j][k], best3[i][j][k - 1]);
				
				if(i >= 4)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 4][j][k]);
				if(i >= 3 && k >= 1)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 3][j][k - 1]);
				if(i >= 2 && k >= 2)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 2][j][k - 2]);
				if(i >= 1 && k >= 3)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 1][j][k - 3]);
				if(k >= 4)
					best3[i][j][k] = max(best3[i][j][k], best3[i][j][k - 4]);
				if(j >= 2)
					best3[i][j][k] = max(best3[i][j][k], best3[i][j - 2][k]);
				if(j >= 1 && i >= 2)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 2][j - 1][k]);
				if(j >= 1 && i >= 1 && k >= 1)
					best3[i][j][k] = max(best3[i][j][k], best3[i - 1][j - 1][k - 1]);
				if(j >= 1 && k >= 2)
					best3[i][j][k] = max(best3[i][j][k], best3[i][j - 1][k - 2]);
							
					
			}
	ans += best3[c1][c2][c3];
	
}

int work()
{
	ans = 0;
	cin >> n >> p;
	for(int i = 1; i <= n; i++)
		cin>>a[i];
	for(int i = 1; i <= n; i++)
		a[i] %= p;
	if(p == 2)
		sv2();
	if(p == 3)
		sv3();
	if(p == 4)
		sv4();
	
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
		
		cout << "Case #" << test << ": " << ans << endl;
	}
	
	return 0;
}
/*
3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
*/

