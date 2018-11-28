#include <bits/stdc++.h>

#define PB push_back

using namespace std;

#define sz(v) ((int)(v).size())
#define forn(i, n) for(in i = 0; i < (n); i++)
#define forv(i, v) forn(i, sz(v))
typedef long long in;
struct two_sat {
in N; // number of variables
	vector<in> val; // assignment of x is at val[2x] and -x at val[2x+1]
	vector<vector<in> > G; // graph of implications G[x][i] = y means (x -> y)

two_sat(in N) : N(N) { // create a formula over N variables (numbered 1 to N)
	val.resize(2*N);
	G.resize(2*N);
}

in to_ind(in x) { // converts a signed variable index to its position in val[] and G[]
	return 2*(abs(x)-1) + (x<0);
}

// Add the implication: a -> b
void add_implication(in a, in b) {
	G[to_ind(a)].push_back(to_ind(b));
}
// Add the or-clause: (a or b)
void add_or(in a, in b) {
	add_implication(-a,b);
	add_implication(-b,a);
}
// Add condition: x is true
void add_true(in x) {
	add_or(x,x);
}

bool dfs(in x) {
	if(val[x] != -1) return val[x];
	val[x] = 1;
	val[x^1] = 0;
	forv(i,G[x])
	if(!dfs(G[x][i]))
		return false;
	return true;
}

bool solve() {
	forv(i,val) val[i] = -1;
	vector<in> tmp(sz(val));
	for(int i=0; i<sz(val); i+=2) {
		if(val[i]==-1) {
			forv(j,val) tmp[j] = val[j];
			if(!dfs(i)) {
				forv(j,val) val[j] = tmp[j];
				if(!dfs(i+1)) return false;
			}
		}
	}
	return true;
}
};

char IN[55][55];

struct point{
	int i,j;
	
	point() {}
	point(int i, int j): i(i), j(j) {}
	
	
	point operator+(const point oth) const {
		return point(i+oth.i, j+oth.j);
	}
	
	bool valid(int R, int C) {
		return i >= 0 && j >= 0 && i < R && j < C;
	}
};

point dir[] = {point(-1,0),point(0,1),point(1,0),point(0,-1)};

int reflect(int d, char c) {
	if(c == '/') {
		switch(d) {
			case 0: return 1;
			case 1: return 0;
			case 2: return 3;
			case 3: return 2;
		}
	} else {
		switch(d) {
			case 0: return 3;
			case 1: return 2;
			case 2: return 1;
			case 3: return 0;
		}
	}
	return 0;
}

void printarr(int R, int C) {
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			printf("%c", IN[i][j]);
		}
		printf("\n");
	}
}

int main() {
	
	int T;
	scanf("%d ", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		
		int R,C;
		scanf("%d%d ", &R, &C);
		
		for(int i = 0; i < R; i++) {
			fgets(IN[i], 55, stdin);
		}
		
		vector<point> laser;
		bool has_empty = false;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(IN[i][j] == '|' || IN[i][j] == '-') laser.emplace_back(i,j);
				if(IN[i][j] == '.') has_empty = true;
			}
		}
		
		if(laser.empty()) {
			if(has_empty) printf("IMPOSSIBLE\n");
			else {
				printf("POSSIBLE\n");
				printarr(R,C);
			}
			
			
			continue;
		}
		
		vector<vector<vector<int> > > E(R,vector<vector<int> >(C));
		set<int> false_x;
		
		two_sat SAT(sz(laser));
		for(int k = 0; k < sz(laser); k++) {
			int x = k+1;
			for(int D = 0; D < 4; D++) {
				x = -x;
				point cur = laser[k];
				int d = D;
				while(true) {
					cur = cur + dir[d];
					if(!cur.valid(R,C)) break;
					char c = IN[cur.i][cur.j];
					if(c == '#') break;
					if(c == '|' || c == '-') {
						SAT.add_true(-x);
						false_x.insert(x);
						break;
					}
					if(c == '\\' || c == '/') {
						d = reflect(d,c);
						continue;
					}
					if(c == '.') {
						E[cur.i][cur.j].PB(x);
						continue;
					}
				}
			}
		}
		
		bool pos = true;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(IN[i][j] != '.') continue;
				if(E[i][j].empty()) {
					pos = false;
				}
				vector<int> vars;
				for(int v : E[i][j]) {
					if(false_x.find(v) == false_x.end()) vars.PB(v);
				}
				if(sz(vars) == 1) SAT.add_true(vars[0]);
				else if(sz(vars) == 2) SAT.add_or(vars[0],vars[1]);
				else {
					pos = false;
				}
			}
		}
		
		if(pos && SAT.solve()) {
			printf("POSSIBLE\n");
			for(int k = 0; k < sz(laser); k++) {
				if(SAT.val[SAT.to_ind(k+1)]) {
					IN[laser[k].i][laser[k].j] = '-';
				} else {
					IN[laser[k].i][laser[k].j] = '|';
				}
			}
			printarr(R,C);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	
	return 0;
}
