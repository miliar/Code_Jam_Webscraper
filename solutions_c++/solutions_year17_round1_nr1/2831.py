#include<bits/stdc++.h>
using namespace std;

int r, c, grid[25][25];
bool vis[25][25], pres[300], used[300];

bool __check(int i, int j)
{
	if(used[grid[i][j]])
		return false;
	int imax = i;
	while(imax+1<r && grid[imax+1][j]==grid[imax][j])
		++imax;
	int jmax = j;
	while(jmax+1<c && grid[i][jmax+1]==grid[i][jmax])
		++jmax;
	used[grid[i][j]] = true;
	bool __checkans = true;
	for(int iii=i; iii<=imax && __checkans; ++iii)
		for(int jjj=j; jjj<=jmax && __checkans; ++jjj) {
			__checkans = grid[i][j]==grid[iii][jjj];
			vis[iii][jjj] = true;
		}
	return __checkans;
}

bool check()
{
	memset(vis, 0, sizeof vis);
	memset(used, 0, sizeof used);

	bool checkans = true;
	for(int i=0; i<r && checkans; ++i)
		for(int j=0; j<c; ++j)
			if(!vis[i][j])
				checkans &= __check(i, j);
	return checkans;
}

bool recsolve(int i, int j)
{
	if(i>=r) return check();
	if(j>=c) return recsolve(i+1, 0);
	if(grid[i][j]!='?'-'A')	return recsolve(i, j+1);
	bool recans = false;
	for(int car='A'-'A'; car<='Z'-'A' && !recans; ++car) {
		if(!pres[car+'A'])
			continue;
		grid[i][j] = '?'-'A';
		if(i==0 || j==0) {
			grid[i][j] = car;
			recans = recsolve(i, j+1);
		}
		if(!recans && i>0 && grid[i-1][j]==car) {
			grid[i][j] = car;
			recans = recsolve(i, j+1);
		}
		if(!recans && j>0 && grid[i][j-1]==car) {
			grid[i][j] = car;
			recans = recsolve(i, j+1);
		}
	}

	if(!recans)
		grid[i][j] = '?'-'A';
	return recans;
}

void solve()
{
	recsolve(0, 0);
	for(int i=0; i<r; ++i) {
		for(int j=0; j<c; ++j)
			cout << ((char)(grid[i][j]+'A'));
		cout << "\n";
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	cin >> t;
	for(int caso=1; caso<=t; ++caso) {
		cin >> r >> c;
		for(int i=0; i<r; ++i)
			for(int j=0; j<c; ++j) {
				char car;
				cin >> car;
				grid[i][j] = car-'A';
				pres[(int)car] = true;
			}
		cout << "Case #" << caso << ":\n";
		solve();
		memset(pres, 0, sizeof pres);
	}

	return 0;
}
