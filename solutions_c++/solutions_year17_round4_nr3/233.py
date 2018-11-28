#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <cstdio>
using namespace std;
#define V vector
#define tD typedef
tD long long ll;
tD V<int> vi;
tD V<vi> vii;
tD V<ll> vll;
tD V<string> vs;
tD V<double> vd;
tD long double ld;
tD pair<int, int> pii;
#define prr make_pair
#define fr(x,y) for(int x=0;x<(y); ++x)
#define fi(n) fr(i,n)
#define fj(n) fr(j,n)
#define fk(n) fr(k,n)
#define pb push_back
#define sz size()
#define DEBUG 0

// Case #68 has a problem

// 3,15 works with 1,15| or 3,14-

struct cell {
	int y, x;
	cell(int Y, int X) {
		y = Y; x = X;
	}
	bool operator==(const cell& c) const {
		return prr(y, x) == prr(c.y, c.x);
	}
	bool operator<(const cell& c) const {
		return prr(y, x) < prr(c.y, c.x);
	}
};

void backslash(int& dy, int& dx) {
	int newdx = dy;
	int newdy = dx;
	dy = newdy;
	dx = newdx;
}

void forwardslash(int& dy, int& dx) {
	int newdx = -dy;
	int newdy = -dx;
	dy = newdy;
	dx = newdx;
}

// If there's any laser whose direction can be determined, do that. Repeat.
bool SolidifyAllLasers(map<cell, vector<pair<cell, bool> > >& ctl, map<cell, bool>& laserdir) {
	bool change = false;
	map<cell, vector<cell> > laser_to_cells;
	for (auto it : ctl) {
		for (auto laser : it.second) {
			laser_to_cells[laser.first].pb(it.first);
		}
	}
	set<cell> to_visit;
	for (auto it : ctl) {
		to_visit.insert(it.first);
	}
	while (!to_visit.empty()) {
		cell ec = *to_visit.begin();
		to_visit.erase(to_visit.begin());
		if (ctl[ec].sz == 0) {
			if (DEBUG) cout << " That doesn't work for cell "<<ec.y<<","<<ec.x<<endl;
			return false;
		}
		if (ctl[ec].sz == 1 && !laserdir.count(ctl[ec][0].first)) {
			if (DEBUG) cout << " Visiting cell "<<ec.y<<","<<ec.x<< endl;
			cell fix = ctl[ec][0].first;
			bool fixvert = ctl[ec][0].second;
			laserdir[fix] = fixvert;
			if (DEBUG) cout << "  Fixing laser at " << fix.y << ","<<fix.x << " to " << (fixvert?'|':'-') << endl;
			for (auto it : ctl) {
				auto options = it.second;
				vector<pair<cell, bool> > new_options;
				bool fixed_found = false;
				fi(options.sz) {
					if (options[i].first == fix) {
						if (DEBUG) cout << "   Considering that laser's effect on " << it.first.y<<","<<it.first.x<<endl;
					}
					if (!(options[i].first == fix && options[i].second != fixvert)) {
					    new_options.pb(options[i]);
					} else {
						if (DEBUG) cout << "   Found the fixed one now can't help " << it.first.y<<","<<it.first.x<<endl;
					}
					if (options[i].first == fix && options[i].second == fixvert) {
						fixed_found = true;
						if (DEBUG) cout <<  "  Found the fixed one can help " << it.first.y << "," << it.first.x << endl;
					}
				}
				if (fixed_found) {
					new_options = vector<pair<cell, bool> >(1, prr(fix, fixvert));
				}
				if (new_options.sz == 0) return false;
				if (new_options != it.second) {
					ctl[it.first] = new_options;
					if (DEBUG) {
						cout << "   New options: ";
						for (auto opt : ctl[it.first]) cout << opt.first.y<<","<<opt.first.x<<(opt.second?'|':'-') << "  ";
						cout << endl;
					}
					to_visit.insert(it.first);
				}
			}
		}
	}
	return true;
}

int main() {
    int T; cin >> T;
    for (int qw = 1 ; qw <= T; qw++) {
		int R, C; cin >> R >> C;
		R = R + 2;
		C = C + 2;
		vector<string> grid(R, string(C, '#'));
		for (int i = 1; i < R - 1; i++) { cin >> grid[i]; grid[i] = "#" + grid[i] + "#"; }
		if (DEBUG) fi(R) cout << grid[i] << endl;
		set<pair<cell, bool> > laser_no_point;
		map<cell, vector<pair<cell, bool> > > cell_to_laser;
		map<cell, bool> laserdir;
		
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (grid[r][c] == '|' || grid[r][c] == '-') {
					// Laser. Follow it.
					for (int vertical = 0; vertical < 2; vertical++) {
						for (int reverse = 0; reverse < 2; reverse++) {
							int dy = vertical ? 1 : 0;
							int dx = vertical ? 0 : 1;
							if (reverse) { dy *= -1; dx *= -1; }
							int y = r, x = c;
							while(true) {
								y += dy; x += dx;
								if (grid[y][x] == '#') break;
								if (grid[y][x] == '|' || grid[y][x] == '-') {
									laser_no_point.insert(prr(cell(r,c), (bool)vertical));
									laserdir[cell(r,c)] = !(bool)vertical;
									break;
								}
								if (grid[y][x] == '\\') {
									backslash(dy, dx);
								}
								if (grid[y][x] == '/') {
									forwardslash(dy, dx);
								}
								if (grid[y][x] == '.') {
									//if (DEBUG) cout << "Cell at " << y<<","<<x<<" works for laser at " << r<<","<<c<<(vertical?'|':'-')<< endl;
									cell_to_laser[cell(y,x)].pb(prr(cell(r, c), vertical));
								}
							}
						}
					}
				}
			}
		}

		// Check which lasers can cover which cells.
		bool fail = false;
		fi(R) fj(C) {
			if (grid[i][j] == '.') {
				vector<pair<cell, bool> > ctl = cell_to_laser[cell(i, j)];
				vector<pair<cell, bool> > newctl;
				fk(ctl.sz) {
					if (!laser_no_point.count(ctl[k])) newctl.pb(ctl[k]);
				}
				cell_to_laser[cell(i, j)] = newctl;
				if (newctl.empty()) {
					fail = true;
				}
				if (DEBUG) {
					cout << "[" << i <<","<<j<<"]: ";
					fk(newctl.sz) {
						cout << newctl[k].first.y <<","<<newctl[k].first.x<<(newctl[k].second ? '|' : '-') << "  ";
					} cout << endl;
				}
			}
		}
		if (DEBUG) cout << "After checking whether cells are theoretically coverable, fail is " << fail << endl;

		// Check whether any lasers can't point any direction.
		fi(R) fj(C) {
			if (grid[i][j] == '-' || grid[i][j] == '|') {
				if (laser_no_point.count(prr(cell(i,j), false)) && laser_no_point.count(prr(cell(i,j), true))) fail = true;
			}
		}
		if (DEBUG) cout << "After checking whether all lasers have somewhere to point, fail is " << fail << endl;

		if (!SolidifyAllLasers(cell_to_laser, laserdir)) {
			fail = true;
		}
		if (DEBUG) cout << "After fixing all lasers we can fix, fail is " << fail << endl;

		bool change = false;
		do {
			change = false;
			for (auto it : cell_to_laser) {
				if (it.second.sz != 2) continue;
				for (int i = 0; i < 2; i++) {
					if (DEBUG) cout << it.first.y << "," << it.first.x << " needs to be resolved. Trying the laser at " << it.second[i].first.y <<"," << it.second[i].first.x << (it.second[i].second ? '|':'-') << endl;
					map<cell, vector<pair<cell, bool> > > new_ctl = cell_to_laser;
					new_ctl[it.first] = vector<pair<cell, bool> >(1, it.second[i]);
					map<cell, bool> new_laserdir = laserdir;
					if (SolidifyAllLasers(new_ctl, new_laserdir)) {
						if (DEBUG) cout << "It worked!" << endl;
						cell_to_laser = new_ctl;
						laserdir = new_laserdir;
						change = true;
						break;
					}
				}
				if (!change) {
					fail = true;
				}
				break;
			}
		} while (change && !fail);

		if (fail) {
			cout << "Case #" << qw << ": IMPOSSIBLE" << endl;
			continue;
		}
		cout << "Case #" << qw << ": POSSIBLE" << endl;
		fi(R) {
			if (i == 0 || i == R - 1) continue;
			fj(C) {
				if (j == 0 || j == C - 1) continue;
				if (grid[i][j] != '-' && grid[i][j] != '|') {
					cout << grid[i][j];
					continue;
				}
				if (laserdir.count(cell(i,j))) { cout << (laserdir[cell(i,j)] ? '|' : '-'); }
				else cout << '-';  // Direction doesn't matter.
			}
			cout << endl;
		}
    }
}
