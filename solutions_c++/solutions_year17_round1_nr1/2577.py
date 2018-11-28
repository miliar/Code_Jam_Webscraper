#include<bits/stdc++.h>
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define tam size()
#define mp make_pair
#define ite iterator
#define prim first
#define sec second
using namespace::std;

const long double PI = acos(-1);
const long double golden = (1+sqrt(5))*0.5;

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<ll,ll> llll;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef set<int> si;
typedef set<ii> sii;
typedef set<iii> siii;

int t, n, m;
vs grid;

void fill(int r1, int r2, int c1, int c2, char ch){
	for(int r = min(r1, r2); r <= max(r1, r2); r++)
		for(int c = min(c1, c2); c <= max(c1, c2); c++)
			grid[r][c] = ch;
}

void solve(){
	for(int r1 = 0; r1 < n; r1++)
		for(int c1 = 0; c1 < m; c1++)
			if( grid[r1][c1] != '?' ){
				char ch = grid[r1][c1];
				for(int r2 = 0; r2 < n; r2++)
					for(int c2 = 0; c2 < m; c2++)
						if( grid[r2][c2] == ch )
							fill(r1, r2, c1, c2, ch);
			}
	for(int r1 = 0; r1 < n; r1++)
		for(int c1 = 0; c1 < m; c1++)
			if( grid[r1][c1] == '?' ){
				for(int c2 = c1 - 1; c2 >= 0; c2--)
					if( grid[r1][c2] != '?' )
						fill(r1, r1, c1, c2, grid[r1][c2]), c2 = -1;
				for(int c2 = c1 + 1; c2 < m; c2++)
					if( grid[r1][c2] != '?' )
						fill(r1, r1, c1, c2, grid[r1][c2]), c2 = m;
			}
	for(int r1 = 0; r1 < n; r1++)
		for(int c1 = 0; c1 < m; c1++)
			if( grid[r1][c1] == '?' ){
				for(int r2 = r1 - 1; r2 >= 0; r2--)
					if( grid[r2][c1] != '?' )
						fill(r1, r2, c1, c1, grid[r2][c1]), r2 = -1;
				for(int r2 = r1 + 1; r2 < n; r2++)
					if( grid[r2][c1] != '?' )
						fill(r1, r2, c1, c1, grid[r2][c1]), r2 = n;
			}
}

int main(){
	scanf("%d", &t);
	for(int caso= 1; caso <= t; caso++){
		printf("Case #%d:\n", caso);
		scanf("%d %d\n", &n, &m);
		grid.resize(n);
		for(int i = 0; i < n; i++){
			cin >> grid[i];
		}
		solve();
		for(int i=0; i<n; i++) cout << grid[i] << endl;
	}
	return 0;
}
