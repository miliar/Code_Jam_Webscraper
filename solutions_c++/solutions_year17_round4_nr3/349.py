#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn = 1010;
char a[maxn][maxn];
int hit[maxn][maxn][4];
int n, m;
const int pie[4]={1,0,3,2};
const int na[4]={3,2,1,0};
const int dx[4]={-1,0,1,0};
const int dy[4]={0,1,0,-1};

bool check(int x, int y)
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			//cout << i << "," << j << endl;
			if (a[i][j] == '.'||a[i][j]=='/'||a[i][j]=='\\')
			{
				int flag = 0;
				for (int k = 0; k < 4; ++k)
					if (hit[i][j][k] != -1)
					{
						int row = hit[i][j][k];
						int type = row%2;row/=2;
						int col=row%m;row/=m;
						if (x*m+y <= row*m+col)
						{
							flag = -1;
							continue;
						}
						//cout << "!" << row << " " << col << " " << type << endl;
						if ((a[row][col]=='-')==(type==0))
							flag = 1;
					}
				if (flag==0) return false;
			}
			if (a[i][j] == '-' || a[i][j] == '|')
			{
				int flag = 0;
				for (int k = 0; k < 4; ++k)
					if (hit[i][j][k] != -1)
					{
						int row = hit[i][j][k];
						int type = row%2;row/=2;
						int col=row%m;row/=m;
						if (x*m+y <= row*m+col)
							continue;
						if ((a[row][col]=='-')==(type==0))
							flag = 1;
					}
				if (flag) return false;
			}
		}
	return true;
}

int travel(int x, int y, int dir)
{
	while (1)
	{
		x += dx[dir];
		y += dy[dir];
		if (x<0||x>=n||y<0||y>=m) return -1;
		switch (a[x][y])
		{
			case '.':break;
			case '#':return -1;break;
			case '/':dir=pie[dir];break;
			case '\\':dir=na[dir];break;
			case '-':
			case '|':return (x*m+y)*2+(dir%2==0);break;
		}
	}
}

bool search(int x, int y)
{
	//cout << x << " " << y << endl;
	if (!check(x, y))
		return false;
	while (1)
	{
		if (y >= m)
		{
			y -= m;
			++x;
			if (x >= n)
				return true;
		}
		if (a[x][y] == '-' || a[x][y] == '|') break;
		++y;
	}
	a[x][y] = '-';
	if (search(x,y+1)) return true;
	a[x][y] = '|';
	if (search(x,y+1)) return true;
	return false;
}

void solve()
{
	memset(a, 0, sizeof(a));
	cin >> n >> m;
	vector<vector<int> > status;
	for (int i = 0; i < n; ++i)
	{
		vector<int> tmp;
		for (int j = 0; j < m; ++j)
		{
			cin >> a[i][j];
			tmp.push_back(a[i][j] == '#' || a[i][j]=='-'||a[i][j]=='|');
		}
		status.push_back(tmp);
	}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (a[i][j] != '#')
			{
				for (int k = 0; k < 4; ++k)
					hit[i][j][k] = travel(i, j, k);
			}
	if (search(0, 0))
	{
		cout << "POSSIBLE" << endl;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
				cout << a[i][j];
			cout << endl;
		}
	}
	else
		cout << "IMPOSSIBLE" << endl;
}

int main()
{
	int times;
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}