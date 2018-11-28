#include <bits/stdc++.h>

using namespace std;

#define ll long long

int n, m, ans;
string s;
vector<int> a;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	ll T;
	cin >> T;
	for(int TT = 1; TT <= T; TT++) {
		ll R, C;
		cin >> R >> C;

		char grid[R+5][C+5], gridCopy[R+5][C+5];
		vector<pair<ll,ll>> initialsPositions;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				cin >> grid[i][j];
				gridCopy[i][j]=grid[i][j];
				if(grid[i][j] != '?') {
					initialsPositions.push_back({i,j});
				}
			}
		}

		for(int i = 0; i < initialsPositions.size(); i++) {
			ll y = initialsPositions[i].first;
			ll x = initialsPositions[i].second;
			char cInitial = grid[y][x];

			ll t,b,l,r;
			t=b=y;
			l=r=x;

			for(; t>=0 && (grid[t][l]==cInitial || grid[t][l]=='?'); t--) {
				grid[t][l]=cInitial;
			}
			t++;
			for(; b<R && (grid[b][l]==cInitial || grid[b][l]=='?'); b++) {
				grid[b][l]=cInitial;
			}
			b--;
			for(; r+1<C;) {
				bool valid = 1;
				for(int i = t; i <= b; i++) {
					if(grid[i][r+1] != cInitial && grid[i][r+1] != '?') {
						valid=0;
						break;
					}
				}
				if(valid) {
					for(int i = t; i <= b; i++) {
						grid[i][r+1] = cInitial;
					}
					r++;
				} else {
					break;
				}
			}
			for(; l-1>=0;) {
				bool valid = 1;
				for(int i = t; i <= b; i++) {
					if(grid[i][l-1] != cInitial && grid[i][l-1] != '?') {
						valid=0;
						break;
					}
				}
				if(valid) {
					for(int i = t; i <= b; i++) {
						grid[i][l-1] = cInitial;
					}
					l--;
				} else {
					break;
				}
			}
		}

		bool isRight = 1;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(grid[i][j] == '?') {
					isRight=0;
					break;
				}
			}
		}
		if(!isRight) {
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					grid[i][j] = gridCopy[i][j];
				}
			}


			for(int i = 0; i < initialsPositions.size(); i++) {
				ll y = initialsPositions[i].first;
				ll x = initialsPositions[i].second;
				char cInitial = grid[y][x];

				ll t,b,l,r;
				t=b=y;
				l=r=x;

				for(; l>=0 && (grid[t][l]==cInitial || grid[t][l]=='?'); l--) {
					grid[t][l]=cInitial;
				}
				l++;
				for(; r<C && (grid[t][r]==cInitial || grid[t][r]=='?'); r++) {
					grid[b][l]=cInitial;
				}
				r--;

				for(; b+1<R;) {
					bool valid = 1;
					for(int i = l; i <= r; i++) {
						if(grid[b+1][i] != cInitial && grid[b+1][i] != '?') {
							valid=0;
							break;
						}
					}
					if(valid) {
						for(int i = l; i <= r; i++) {
							grid[b+1][i] = cInitial;
						}
						b++;
					} else {
						break;
					}
				}
				for(; t-1>=0;) {
					bool valid = 1;
					for(int i = l; i <= r; i++) {
						if(grid[t-1][i] != cInitial && grid[t-1][i] != '?') {
							valid=0;
							break;
						}
					}
					if(valid) {
						for(int i = l; i <= r; i++) {
							grid[t-1][i] = cInitial;
						}
						t--;
					} else {
						break;
					}
				}
			}


		}

		cout << "Case #" << TT << ":\n";

		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				cout << grid[i][j];
			}
			cout << endl;
		}
	}



}
