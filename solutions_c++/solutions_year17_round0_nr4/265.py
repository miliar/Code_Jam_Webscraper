#include <bits/stdc++.h>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

bool can_place(int x, int y, vector<vector<bool> >& occupied, int *dX, int *dY)
{
	for(int dir = 0; dir<4; dir++)
	{
		int cx = x, cy = y;
		while(cy >= 0 && cy < occupied.size() && cx >= 0 && cx < occupied[cy].size())
		{
			if(occupied[cy][cx])return 0;
			cx += dX[dir];
			cy += dY[dir];
		}
	}
	return 1;
}

int dX_bishop[4] = {1, 1, -1, -1}, dY_bishop[4] = {-1, 1, 1, -1};
int dX_rook[4] = {0, 1, 0, -1}, dY_rook[4] = {-1, 0, 1, 0};

bool can_place_rook(int x, int y, vector<vector<bool> >& occupied)
{
	return can_place(x, y, occupied, dX_rook, dY_rook);
}

bool can_place_bishop(int x, int y, vector<vector<bool> >& occupied)
{
	return can_place(x, y, occupied, dX_bishop, dY_bishop);
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int test=0; test<t; test++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		vector<vector<bool> > bishop(n, vector<bool> (n, 0)), rook(n, vector<bool> (n, 0));
		int style = 0;
		for(int i=0; i<m; i++)
		{
			int r, c;
			char type;
			scanf(" %c %d %d", &type, &r, &c);
			r--;
			c--;
			if(type == 'o' || type == '+')
			{
				bishop[r][c] = 1;
				style++;
			}
			if(type == 'o' || type == 'x')
			{
				rook[r][c] = 1;
				style++;
			}
		}
		int sx = 0, sy = n-1;
		set<pii > modified;
		while(1)
		{
			for(int x=sx, y=sy; x < n && y < n; x++, y++)
			{
				if(can_place_rook(x, y, rook))
				{
					rook[y][x] = 1;
					modified.insert(pii(x,y));
					style++;
				}
				if(can_place_bishop(x, y, bishop))
				{
					bishop[y][x] = 1;
					modified.insert(pii(x, y));
					style++;
				}
			}
			if(sx == 0 && sy == 0)break;
			swap(sx, sy);
			if(sx == 0)sy--;
		}
		printf("Case #%d: %d %d\n", test+1, style, (int)modified.size());
		for(set<pii >::iterator it = modified.begin(); it != modified.end(); it++)
		{
			int x = (*it).first, y = (*it).second;
			char type;
			if(bishop[y][x] && rook[y][x])type = 'o';
			else if(bishop[y][x])type = '+';
			else if(rook[y][x])type = 'x';
			printf("%c %d %d\n", type, y+1, x+1);
		}
	}
	return 0;
}