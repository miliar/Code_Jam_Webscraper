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

bool dfs(const vector<vi> &G,int v,vector<bool> &visit, vector<int> &match,vector<int> &level){
	visit[v]=true;
	REP(i,G[v].size()){
		int dst=G[v][i];
		int w=match[dst];
		if(w==-1 || (!visit[w] && level[v] < level[w] && dfs(G,w,visit,match,level))){
			match[v]=dst;
			match[dst]=v;
			return true;
		}
	}
	return false;
}
vector<int> bipartite_matching(const vector<vi> &G){
	vector<int> match(G.size(), -1);
	for(int res = 0;;){
		vector<int> level(G.size(),-1);
		queue<int> que;
		REP(i,G.size()){
			if(match[i]==-1){
				que.push(i);
				level[i]=0;
			}
		}
		while(!que.empty()){
			int v=que.front();que.pop();
			REP(i,G[v].size()){
				int dst=G[v][i];
				int w=match[dst];
				if(w != -1 && level[w]<0){
					level[w]=level[v]+1;
					que.push(w);
				}
			}
		}
		vector<bool> visit(G.size());
		int d=0;
		REP(v,G.size()){
			if(match[v]==-1&&dfs(G,v,visit,match,level))d++;
		}
		if(d==0)return match;
		res+=d;
	}
}

int T, n, m;

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	cin >> T;
	REPS(t, T){
		cin >> n >> m;
		vector<int> tate(n), yoko(n), pp(2*n), pn(2*n);
		vector<int> prv(n*n), nxt(n*n);
		REP(i, m){
			char c;
			int y, x;
			cin >> c >> y >> x; y--; x--;
			if(c == 'x' || c == 'o'){
				tate[x] = 1;
				yoko[y] = 1;
			}
			if(c == '+' || c == 'o'){
				pp[x+y] = 1;
				pn[n-1+y-x] = 1;
			}
			nxt[y*n+x] = prv[y*n+x] = (c == 'o') ? 3 : (c == 'x' ? 2 : 1);
		}
		vector<vi> g(4*n);
		REP(y, n)REP(x, n){
			int i = x+y;
			int j = n-1-x+y;
			if(!pp[i] && !pn[j]){
				g[i].pb(2*n+j);
				g[2*n+j].pb(i);
			}
		}
		auto matching = bipartite_matching(g);
		REP(i, 2*n-1){
			if(matching[i] != -1){
				int j = matching[i] - 2*n;
				int x = (i-j+n-1)/2;
				int y = (i+j-n+1)/2;
				nxt[y*n+x] |= 1;
			}
		}
		vector<tuple<char, int, int>> ans;
		REP(y, n)REP(x, n){
			if(!tate[x] && !yoko[y]){
				nxt[y*n+x] |= 2;
				tate[x] = 1;
				yoko[y] = 1;
			}
			if(prv[y*n+x] != nxt[y*n+x]){
				ans.eb(".+xo"[nxt[y*n+x]], y + 1, x + 1);
			}
		}
		int sum = 0;
		REP(y, n){
			REP(x, n){
				sum += __builtin_popcount(nxt[y*n+x]);
			}
		}
		
		cout << "Case #" << t << ": " << sum << " " << ans.size() << endl;
		for(auto it : ans){
			char c;
			int y, x;
			tie(c, y, x) = it;
			cout << c << " " << y << " " << x << endl;
		}
		cerr << n << " " << sum << endl;
	}
	return 0;
}
