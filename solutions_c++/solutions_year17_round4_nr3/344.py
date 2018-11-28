#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define REPS(i,x) for(int i=1;i<=(int)(x);i++)
#define RREP(i,x) for(int i=((int)(x)-1);i>=0;i--)
#define RREPS(i,x) for(int i=((int)(x));i>0;i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)
#define ALL(container) (container).begin(), (container).end()
#define RALL(container) (container).rbegin(), (container).rend()
#define SZ(container) ((int)container.size())
#define mp(a,b) make_pair(a, b)
#define pb push_back
#define eb emplace_back
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"["; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"]"; return os;
}
template<class T> ostream& operator<<(ostream &os, const set<T> &t) {
os<<"{"; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"}"; return os;
}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class S, class T> pair<S,T> operator+(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first+t.first, s.second+t.second);}
template<class S, class T> pair<S,T> operator-(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first-t.first, s.second-t.second);}

const int INF = 1<<28;
const double EPS = 1e-8;
const int MOD = 1000000007;

int T, n, m;

char s[60][60];
int visited[60][60];
vector<pii> g[60][60];

int d[5] = {0, 1, 0, -1, 0};

void tour(int x, int y, int dir, vector<int> &v){
//	cerr << "start with dir " << dir << endl;
	while(1){
		x += d[dir];
		y += d[dir + 1];
//		cerr << x << ", " << y << ", " << dir << endl;
		if(s[y][x] == '-' || s[y][x] == '|'){
			v.pb(-1); return;
		}
		if(s[y][x] == '#') return;
		if(s[y][x] == '/') dir = 3 - dir;
		if(s[y][x] == '\\') dir ^= 1;
		if(s[y][x] == '.') v.pb(y*m + x);
	}
}

int solve(){
	memset(visited, 0, sizeof(visited));
	memset(s, '#', sizeof(s));
	REPS(i, n - 2)REPS(j, m - 2) g[i][j].clear();
	
	cin >> n >> m; n += 2; m += 2;
	REPS(i, n - 2)REPS(j, m - 2) cin >> s[i][j];
	
	vector<vector<vi>> beam;
	vector<pii> beam_pos;
	int beam_i = 0;
	REPS(i, n-2)REPS(j, m-2){
		if(s[i][j] != '.') visited[i][j] = 1;
		if(s[i][j] == '-' || s[i][j] == '|'){
			vi v0, v1;
			tour(j, i, 0, v0);
			tour(j, i, 2, v0);
			tour(j, i, 1, v1);
			tour(j, i, 3, v1);
			sort(ALL(v0)); UNIQUE(v0);
			sort(ALL(v1)); UNIQUE(v1);
			int f0 = v0.empty() || v0[0] != -1;
			int f1 = v1.empty() || v1[0] != -1;
			cerr << i << ", " << j << endl;
			cerr << v0 << ": " << f0 << endl;
			cerr << v1 << ": " << f1 << endl;
			if(!f0 && !f1){
				cerr << i << ", " << j << " has no choice" << endl;
				return 0;
			}
			if(f0 && f1){
				beam.eb(2);
				beam_pos.eb(i, j);
				for(int x : v0){
					g[x / m][x % m].eb(beam_i, 0);
					beam[beam_i][0].pb(x);
				}
				cerr << v1 << endl;
				for(int x : v1){
					cerr << "! " << x / m << ", " << x % m << " eb " << beam_i << ", " << 1 << endl;
					g[x / m][x % m].eb(beam_i, 1);
					beam[beam_i][1].pb(x);
					cerr << "?" << g[2][2] << endl;
				}
				beam_i ++;
			}else{
				const auto &v = f0 ? v0 : v1;
				for(int x : v){
					visited[x / m][x % m] = 1;
				}
				s[i][j] = f0 ? '|' : '-';
				cerr << i << ", " << j << " 1chosen as " << (f0 ? '|' : '-') << endl;
			}
		}
	}
	queue<int> q;
	REPS(i, n-2)REPS(j, m-2)if(!visited[i][j]){
		if(g[i][j].empty()){
			cerr << i << ", " << j << " has no candidate beams" << endl;
			return 0;
		}
		if(g[i][j].size() == 1) q.push(i*m + j);
	}
	while(1){
		while(!q.empty()){
			int u = q.front(); q.pop();
			int y = u / m, x = u % m;
			visited[y][x] = 1;
			int b, f; tie(b, f) = g[y][x][0];
			s[beam_pos[b].first][beam_pos[b].second] = (f == 0) ? '|' : '-';
			cerr << beam_pos[b].first << ", " << beam_pos[b].second << " chosen as " << ((f == 0) ? '|' : '-') << endl;
			for(int v : beam[b][f]) visited[v / m][v % m] = 1;
			for(int v : beam[b][!f]){
				int y = v / m, x = v % m;
				if(visited[y][x]) continue;
				cerr << y << ", " << x << ": " << g[y][x] << endl;
				auto it = find(ALL(g[y][x]), pii(b, !f));
				if(it != g[y][x].end()) g[y][x].erase(it);
				if(g[y][x].empty()){
					cerr << y << ", " << x << " has finally no candidate beams" << endl;
					return 0;
				}
				q.push(v);
			}
		}
		int f = 0;
		REPS(i, n-2){
			REPS(j, m-2)if(!visited[i][j]){
				assert(g[i][j].size() == 2);
				cerr << i << ", " << j << " pop_back" << endl;
				g[i][j].pop_back();
				q.push(i*m + j);
				f = 1;
				break;
			}
			if(f) break;
		}
		if(q.empty()) return 1;
	}
}

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(t, T){
		if(solve()){
			cout << "Case #" << t << ": " << "POSSIBLE" << endl;
			REPS(i, n-2){
				REPS(j, m-2) cout << s[i][j];
				cout << endl;
			}
		}else{
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		}
		cerr << "------------" << endl;
	}
	return 0;
}
