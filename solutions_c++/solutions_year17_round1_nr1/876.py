#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef vector<int> vi;

#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d%d", &x, &y)
#define FOR(i,S,E) for(int i=S; i<E; i++)
#define fst first
#define snd second
#define mp make_pair

const int MAX = 25*25+20;
/*
struct Pos {
	pii leftTop, botRight;
	void clear () {
		leftTop=botRight=-1;
	}
};
*/

int xmov[] = {-1, 1, 0, 0}, ymov[] = {-0, 0, -1, 1};

int R, C;

bool val(int x, int y) {
	return (x >= 0 && y >=0 && x < R && y < C);
}

int main () {
	int T; cin >> T;
	FOR(t,1,T+1) {
		cin >> R >> C;
		
		//FOR(i,0,R*C+10) pos[i].clear();
		
		vector<string> grid;
		vector<vi> vis;
		vis.resize(R);
		grid.resize(R);
		
		FOR(i,0,R) {
			cin >> grid[i];
			vis[i].resize(C,0);
		}
		bool bad=0;
		int cnt=1, i=0;
		do {
			bad=0;
			FOR(r,0,R) {
				FOR(c,0,C) {
					if (grid[r][c] == '?') {
						bad=1;
						continue;
					}
					
					if (vis[r][c] == cnt) continue;
					int x = xmov[i]+r, y = ymov[i]+c;
					if (!val(x,y) || grid[x][y] != '?') continue;
					while( val(x,y) && grid[x][y] == '?') {
						//	printf("%d %d -> %d %d; %d\n", r, c, x, y, cnt);
						grid[x][y] = grid[r][c];
						vis[x][y] = cnt;
						if (!i) {
							x--;
						}
						else if (i==1) {
							x++;
						}
						else if (i==2) {
							y--;
						}
						else {
							y++;
						}
					}
				}
			}
			cnt++;
			i = (i+1)%4;
		} while(bad);

		cout << "Case #" << t << ":" << endl;
		FOR(i,0,R) {
			cout << grid[i] << endl;;
		}
	}
}
