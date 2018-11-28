#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

#define FOR2(r, L, R, c, U, D) for (int r = L; r <= R; ++r) for(int c = U; c <= D; ++c)

bool submit = true;

// ---------------------------------------------------
// ---------------------------------------------------

struct RG
{
	int l = INT_MAX;
	int r = INT_MIN;
	int u = INT_MAX;
	int d = INT_MIN;
};

void printgrid(const vector<vector<char>>& grid)
{
	int R = grid.size(); 
	int C = grid[0].size();

	F0(r, R)
	{
		F0(c, C)
			printf("%c", grid[r][c]);
		printf("\n");
	}
}


void expand(vector<vector<char>>& grid, char cIn, RG rg)
{
	FOR2(r, rg.u, rg.d, c, rg.l, rg.r) grid[r][c] = cIn; // inital filling

	int R = grid.size(); 
	int C = grid[0].size();

	bool okay = true;
	while(okay && rg.l > 0)
	{
		rg.l--;	
		FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
		{
			if (grid[r][c] == '?' || grid[r][c] == cIn) 
				continue;
			else 
				okay = false;
		}

		if (okay) 
		{
			FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
				grid[r][c] = cIn;
		}
		else
			rg.l++;

	}

	okay = true;
	while(okay && rg.u > 0)
	{
		rg.u--;
		FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
		{
			if (grid[r][c] == '?' || grid[r][c] == cIn) 
				continue;
			else 
				okay = false;
		}

		if (okay)
		{
			FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
				grid[r][c] = cIn;
		}
		else
			rg.u++;
	}

	okay = true;
	while(okay && rg.r < C-1)
	{
		rg.r++;
		FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
		{
			if (grid[r][c] == '?' || grid[r][c] == cIn) 
				continue;
			else 
				okay = false;
		}

		if (okay) 
		{
			FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
			grid[r][c] = cIn;
		}
		else
			rg.r--;
	}

	okay = true;
	while(okay && rg.d < R-1)
	{
			rg.d++;
		FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
		{
			if (grid[r][c] == '?' || grid[r][c] == cIn) 
				continue;
			else 
				okay = false;
		}

		if (okay) 
		{
			FOR2(r, rg.u, rg.d, c, rg.l, rg.r)
				grid[r][c] = cIn;
 		}
 		else
 			rg.d--;
	}

}
void util(vector<vector<char>>& grid)
{
	int R = grid.size(); 
	int C = grid[0].size();

	map<char, int> mcnt;
	map<char, RG> mrg;

	F0(r, R) 
	F0(c, C) 
	{
		char c1 = grid[r][c];
		mcnt[c1]++;
		
		mrg[c1].l = min(mrg[c1].l, c);
		mrg[c1].r = max(mrg[c1].r, c);
		mrg[c1].u = min(mrg[c1].u, r);
		mrg[c1].d = max(mrg[c1].d, r);
	}

	if (mcnt.find('?') == mcnt.end()) return;

	// printf("--------\n");
	// for (auto m : mcnt) printf("%c : %d \n", m.first, m.second);
	// printf("--------\n");
	// for (auto m : mrg) printf("%c : l %d, r %d, u %d, d %d\n", m.first, m.second.l, m.second.r, m.second.u, m.second.d );

	for (auto m : mrg)
		if (m.first != '?')
			expand(grid, m.first, m.second);


	F0(r, R) 
	F0(c, C) 
	{
		char c1 = grid[r][c];
		mcnt[c1]++;
		
		mrg[c1].l = min(mrg[c1].l, c);
		mrg[c1].r = max(mrg[c1].r, c);
		mrg[c1].u = min(mrg[c1].u, r);
		mrg[c1].d = max(mrg[c1].d, r);
	}


	if (mcnt.find('?') == mcnt.end()) return;

	for (auto m : mrg)
		if (m.first != '?')
			expand(grid, m.first, m.second);

}

int main()
 {
	if (submit)
	{
		freopen("A-small-attempt1.in", "r", stdin);
		freopen("A-small-attempt1.out", "w", stdout);
		
		// freopen("A-large.in", "r", stdin);
		// freopen("A-large.out", "w", stdout);

		int tt, tn; // loop var and total test cases
		cin >> tn;

		int R, C;

		F1(tt,tn)
		{
			cin >> R; cin >> C;
			vector<vector<char>> grid(R, vector<char> (C, '?'));
			F0(r, R)
				F0(c, C)
					cin >> grid[r][c];

			if (tt == 22) {printf("Original grid\n"); printgrid(grid);}
			

			util(grid);

			printf("Case #%d:\n", tt);
			printgrid(grid);

		}
	}
	else // go dev
	{

	}

	return 0;
}
