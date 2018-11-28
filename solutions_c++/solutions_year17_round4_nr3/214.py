#include <bits/stdc++.h> 

using namespace std;
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define fst first
#define snd second
#define sz(x) (int) ((x).size()) 
#define forn(i, n) for (int i = 0; (i) < (n); ++i)
#define fornr(i, n) for (int i = (n) - 1; (i) >= 0; --i)
#define forab(i, a, b) for (int i = (a); (i) < (b); ++i)
#define forba(i, a, b) for (int i = (b) - 1; (i) >= (a); --i)
#define forit(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(), (c).end() 

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) static_cast<void>(0)   
#endif

#ifdef _WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef vector <int> vi;
typedef pair <int, int> pii;

#define FNAME ""

const int MAX_N = 105;
const int TURN[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};

char s[MAX_N][MAX_N], used[MAX_N][MAX_N];
map<pii, vector<pii>> g;
map<pii, int> usedDfs;
vector<pii> path, path1, path2;
int h, w;

void go(int r, int c, int dir) {
 	if (s[r][c] == '#' || r < 0 || c < 0 || r >= h || c >= w)
 		return;
	path.pb(mp(r, c));
 	if (s[r][c] == '/') {
 	 	if (dir == 0) 
 	 		go(r - 1, c, 1);
 	 	if (dir == 1)
 	 		go(r, c + 1, 0);
 	 	if (dir == 2)
 	 		go(r + 1, c, 3);
 	 	if (dir == 3) 
 	 		go(r, c - 1, 2);
 		return;
 	}
 	if (s[r][c] == '/') {
 	 	if (dir == 0) 
 	 		go(r - 1, c, 1);
 	 	if (dir == 1)
 	 		go(r, c + 1, 0);
 	 	if (dir == 2)
 	 		go(r + 1, c, 3);
 	 	if (dir == 3) 
 	 		go(r, c - 1, 2);
 		return;
 	}
	go(r + TURN[dir][0], c + TURN[dir][1], dir);
}

bool isShoot(int r, int c) {
 	return s[r][c] == '-' || s[r][c] == '|' || s[r][c] == '?';
}

bool isOkPath(const vector<pii> &path) {
	for (auto np : path)
		if (isShoot(np.fs, np.sc))
			return 0;
	return 1;
}

char get(int dr, int dc) {
 	if (dr == 0)
 		return '-';
 	return '|';
}

void dfs(int r, int c, char symb, bool &possible) {
	usedDfs[mp(r, c)] = 1;
	s[r][c] = symb;
 	for (auto np : g[mp(r, c)]) {
 	 	if (s[np.fs][np.sc] != '?' && s[np.fs][np.sc] != symb)
 	 		possible = 0;
 	 	s[np.fs][np.sc] = symb;
 	 	if (!usedDfs[np])
 	 		dfs(np.fs, np.sc, symb, possible);
 	}
}

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    

	int t;
	scanf("%d", &t);
	forn (tt, t) {
	    scanf("%d%d\n", &h, &w);
		forn (i, h)
			gets(s[i]);
		bool possible = 1;
		g.clear();
		usedDfs.clear();
		forn (i, h)
			forn (j, w)
				used[i][j] = 0;
		forn (i, h)
			forn (j, w)
				if (isShoot(i, j)) {
					int ok = 0;
				    path.clear();
					int dir = 0;
				 	go(i + TURN[dir][0], j + TURN[dir][1], dir);
					dir = 2;
				 	go(i + TURN[dir][0], j + TURN[dir][1], dir);
				 	if (isOkPath(path))
				 		ok ^= 1;
				    path1 = path;

				    path.clear();
					dir = 1;
				 	go(i + TURN[dir][0], j + TURN[dir][1], dir);
					dir = 3;
				 	go(i + TURN[dir][0], j + TURN[dir][1], dir);
				 	if (isOkPath(path))
				 		ok ^= 2;
				 	path2 = path;
				 	
                    if (ok == 0)
				    	possible = 0;
				    if (ok == 1) {
				     	for (auto np : path1)
				     		used[np.fs][np.sc] = 1;
				     	s[i][j] = '-';
				    }
				    if (ok == 2) {
				     	for (auto np : path2)
				     		used[np.fs][np.sc] = 1;
				     	s[i][j] = '|';
				    }
				    if (ok == 3) {
				     	s[i][j] = '?';
				    }
				}
		forn (i, h)
			forn (j, w)
				if (s[i][j] == '.' && !used[i][j]) {
					//printf("%d %d\n", i, j);
					int ok = 0;
				    path.clear();
					int dir = 0;
				 	go(i, j, dir);
					dir = 2;
				 	go(i, j, dir);
				 	if (!isOkPath(path))
				 		ok ^= 1;
				    path1 = path;

				    path.clear();
					dir = 1;
				 	go(i, j, dir);
					dir = 3;
				 	go(i, j, dir);
				 	if (!isOkPath(path))
				 		ok ^= 2;
				 	path2 = path;
				 					
				    if (ok == 0)
				    	possible = 0;
				    if (ok == 1) {
				    	forn (i, sz(path1)) { 	
				     	    auto np = path1[i];
				     		if (isShoot(np.fs, np.sc)) {
				     			char symb = get(path1[i].fs - path1[i - 1].fs, path1[i].sc - path1[i - 1].sc);
				     		 	if (s[np.fs][np.sc] != '?' && s[np.fs][np.sc] != symb)
				     		 		possible = 0;
				     		 	else
				     		 		s[np.fs][np.sc] = symb;
				     		}
				     	}
				    }

					if (ok == 2) {
				    	forn (i, sz(path2)) { 	
				     	    auto np = path2[i];
				     		if (isShoot(np.fs, np.sc)) {
				     		 	if (s[np.fs][np.sc] != '?')
				     		 		possible = 0;
				     		 	else
				     		 		s[np.fs][np.sc] = get(path2[i].fs - path2[i - 1].fs, path2[i].sc - path2[i - 1].sc);
				     		}
				     	}
				    }

					if (ok == 3) {
					 	pii l1, l2;
					 	for (auto np : path1)
					 		if (isShoot(np.fs, np.sc))
					 			l1 = np;
					 	for (auto np : path2)
					 		if (isShoot(np.fs, np.sc))
					 			l2 = np;
					 	g[l1].pb(l2);
					 	g[l2].pb(l1);
					}
					//printf("%d\n", possible);				  
				}
		forn (i, h)
			forn (j, w)
				if (!usedDfs[mp(i, j)] && isShoot(i, j) && s[i][j] != '?')
					dfs(i, j, s[i][j], possible);
		forn (i, h)
			forn (j, w)
				if (!usedDfs[mp(i, j)] && isShoot(i, j))
					dfs(i, j, '-', possible);
		printf("Case #%d: ", tt + 1);
		if (!possible)
			puts("IMPOSSIBLE");
	   	else {
	   	 	puts("POSSIBLE");
	   	 	forn (i, h)
	   	 		puts(s[i]);
	   	}
	}	

	return 0;
}