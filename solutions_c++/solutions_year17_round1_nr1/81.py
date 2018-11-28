#include "bits/stdc++.h"
using namespace std;
const int maxn = 50;
#define mp make_pair
#define pb push_back
char grid[maxn][maxn];
typedef pair<int, int> ii;
vector<ii> orr[maxn*maxn];
int main(){
	int r, c;
	int cases; cin>>cases; 
	for(int cs = 1; cs <= cases; cs++){
		cout << "Case #" << cs << ":\n";
		for(int e = 0; e < maxn*maxn; e++)
			orr[e].clear();
		cin >> r >> c;
		for(int e = 0; e < r; e++)
			for(int f = 0; f < c; f++)
				cin >> grid[e][f], orr[grid[e][f]].pb(mp(e, f));
		for(int e = 'A'; e <= 'Z'; e++){
			if(orr[e].size()){
				int mx = orr[e][0].first;
				int my = orr[e][0].second;
				int mmx = mx;
				int mmy = my;
				for(auto &it:orr[e]){
					mx = min(mx, it.first);
					my = min(my, it.second);
					mmx = max(mmx, it.first);
					mmy = max(mmy, it.second);
				}
				for(int f = mx; f <= mmx; f++)
					for(int g = my; g <= mmy; g++)
						grid[f][g] = e;
			}
		}
					
		for(int e = 0; e < r; e++)
			for(int f = 0; f < c; f++)
				if(e+1 < r){
					if(grid[e+1][f] == '?')
						grid[e+1][f] = grid[e][f];
				}
		for(int e = r-1; e > -1; e--)
			for(int f = 0; f < c; f++)
				if(e-1 > -1){
					if(grid[e-1][f] == '?')
						grid[e-1][f] = grid[e][f];
				}
		for(int e = 0; e < r; e++)
			for(int f = 0; f < c; f++)
				if(f+1 < c){
					if(grid[e][f+1] == '?')
						grid[e][f+1] = grid[e][f];
				}
		for(int e = 0; e < r; e++)
			for(int f = c-1; f > 0; f--)
				if(grid[e][f-1] == '?')
					grid[e][f-1] = grid[e][f];	
		for(int e = 0; e < r; e++){
			for(int f = 0; f < c; f++)
				cout << grid[e][f];
			cout << endl;
		}
	}
	return 0;
}

