#include <bits/stdc++.h>
#define VERTICAL 1
#define HORISONTAL 2
#define DOWN 0
#define UP 1
#define RIGHT 2
#define LEFT 3
using namespace std;

#define rep(i, f, t) for (int i = f; i < int(t); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define trav(x,a) for (auto& x : a)
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string f[55];
int R, C;
vector<pair<pair<int, int>, int> > cover[55][55];
vector<vector<int> > direction;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

vector<pair<int, int> > trace(int sx, int sy, int D){
	bool ok = 1;
	vector<pair<int, int> > ret;
	int sxstart = sx;
	int systart = sy;
	rep(i,0,2){
		int d = 2*(D-1)+i;
		sx = sxstart;
		sy = systart;
		while(true){
			sx += dx[d];
			sy += dy[d];
			if(sx < 0 || sy < 0 || sx >= R || sy >= C)
				break;
			//cerr << f[sx][sy] << endl;
			if(f[sx][sy] == '#')
				break;
			if(f[sx][sy] == '-'){
				ok = 0;
				break;
			}
			if(f[sx][sy] == '/'){
				if(d == DOWN)
					d = LEFT;
				else if(d == UP)
					d = RIGHT;
				else if(d == LEFT)
					d = DOWN;
				else if(d == RIGHT)
					d = UP;
			}
			else if(f[sx][sy] == '\\'){
				if(d == DOWN)
					d = RIGHT;
				else if(d == UP)
					d = LEFT;
				else if(d == LEFT)
					d = UP;
				else if(d == RIGHT)
					d = DOWN;
			}
			else{
				ret.emplace_back(sx, sy);
			}
		}
	}
	if(!ok){
		ret.clear();
		ret.emplace_back(-1, -1);
	}
	return ret;
}

bool changed;
bool contradiction = false;

void computeCover(){
	rep(i,0,R)
		rep(j,0,C){
			cover[i][j].clear();
		}
	rep(i,0,R)
		rep(j,0,C){
			if(f[i][j] != '-')
				continue;
			rep(d,1,3){
				if(!(direction[i][j]&d))
					continue;
				auto points = trace(i, j, d);
				if(!points.empty() && points[0].first == -1){
					direction[i][j] ^= d;
					changed = true;
					if(!direction[i][j])
						contradiction = true;
					continue;
				}
				for(auto point : points){
					int x = point.first;
					int y = point.second;
					cover[x][y].emplace_back(make_pair(i, j), d);
				}
			}
		}
}

void solve(){
	cin >> R >> C;
	rep(i,0,R)
		rep(j,0,C){
			cover[i][j].clear();
		}
	direction = vector<vector<int> >(R, vector<int>(C, 3));
	rep(i,0,R)
		rep(j,0,C){
			cover[i][j].clear();
			direction[i][j] = 3;
		}
	rep(i,0,R){
		cin >> f[i];
		rep(j,0,C)
			if(f[i][j] == '|')
				f[i][j] = '-';
	}
	rep(i,0,R)
		rep(j,0,C){
			if(f[i][j] != '-')
				continue;
			if(direction[i][j] != 3)
				continue;
			auto directionSaved = direction;
			direction[i][j] = VERTICAL;
			changed = false;
			contradiction = false;
			bool isOk;
			while(!contradiction){
				changed = false;
				computeCover();
				isOk = true;
				rep(x,0,R)
					rep(y,0,C){
						if(f[x][y] != '.')
							continue;
						if(cover[x][y].empty()){
							isOk = false;
						}
						else if(cover[x][y].size() == 1){
							int x0 = cover[x][y][0].first.first;
							int y0 = cover[x][y][0].first.second;
							int d0 = cover[x][y][0].second;
							if(direction[x0][y0] == 3){
								direction[x0][y0] = d0;
								changed = true;
							}
						}
					}
				if(!changed)
					break;
				if(!isOk)
					break;
			}
			if(!isOk || contradiction){
				if(!(directionSaved[i][j] & HORISONTAL)){
					cout << "IMPOSSIBLE" << endl;
					return;
				}
				direction = directionSaved;
				direction[i][j] = HORISONTAL;
			}
		}
	computeCover();
	rep(x,0,R)
		rep(y,0,C){
			if(f[x][y] == '-' && !direction[x][y]){
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			if(f[x][y] != '.')
				continue;
			if(cover[x][y].empty()){
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}
	cout << "POSSIBLE" << endl;
	rep(i,0,R){
		rep(j,0,C){
			if(f[i][j] == '-'){
				if(direction[i][j] == HORISONTAL)
					cout << '-';
				else if(direction[i][j] == VERTICAL)
					cout << '|';
				else
					assert(0);
			}
			else
				cout << f[i][j];
		}
		cout << endl;
	}
}

int main(){
	int N;
	cin >> N;
	rep(t,1,N+1){
		cerr << t << endl;
		cout << "Case #" << t << ": ";
		solve();
	}
}
