#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

string s[55];
int id[55][55];
int u[55][55];

int it=0;

vector<int> cv[55][55];

int r,c;

void path(int y, int x, int dy, int dx, vector<pair<int, int> >& p){
	if (y<0||x<0||y>=r||x>=c) return;
	if (u[y][x]==it) return;
	assert((dy==0)^(dx==0));
	u[y][x]=it;
	p.push_back({y, x});
	if (s[y][x]=='#'||s[y][x]=='-'){
		return;
	}
	else if (s[y][x]=='/'){
		if (dy==0){
			if (dx==1) path(y-1, x, -1, 0, p);
			else path(y+1, x, 1, 0, p);
		}
		else if(dy==1) path(y, x-1, 0, -1, p);
		else path(y, x+1, 0, 1, p);
	}
	else if(s[y][x]=='\\'){
		if (dy==0){
			if (dx==1) path(y+1, x, 1, 0, p);
			else path(y-1, x, -1, 0, p);
		}
		else if(dy==-1) path(y, x-1, 0, -1, p);
		else path(y, x+1, 0, 1, p);
	}
	else if(s[y][x]=='.'){
		path(y+dy, x+dx, dy, dx, p);
	}
	else{
		assert(0);
	}
}

struct SCC {
	vector<int> used;
	vector<vector<int> > g2;
	void dfs1(vector<int>* g, int x, vector<int>& ns) {
		if (used[x]==1) return;
		used[x]=1;
		for (int nx:g[x]) {
			g2[nx].push_back(x);
			dfs1(g, nx, ns);
		}
		ns.push_back(x);
	}
	void dfs2(int x, vector<int>& co) {
		if (used[x]==2) return;
		used[x]=2;
		co.push_back(x);
		for (int nx:g2[x]) dfs2(nx, co);
	}
	SCC(vector<int>* g, int n, vector<vector<int> >& ret) : used(n+1), g2(n+1) {
		vector<int> ns;
		for (int i=1;i<=n;i++) dfs1(g, i, ns);
		for (int i=n-1;i>=0;i--) {
			if (used[ns[i]]!=2) {
				ret.push_back(vector<int>());
				dfs2(ns[i], ret.back());
			}
		}
	}
};

vector<int> g[1010];

void addc(int a, int b){
	g[a^1].push_back(b);
	g[b^1].push_back(a);
}

int isbad(vector<pair<int, int> >& pt){
	for (auto t:pt){
		assert(t.F>=0&&t.S>=0&&t.F<r&&t.S<c);
		if (s[t.F][t.S]=='-') return 1;
	}
	return 0;
}

int fo[101010];
int t[101010];

void solve(){
	cin>>r>>c;
	vector<pair<int, int> > bs;
	for (int i=0;i<r;i++){
		cin>>s[i];
		for (int ii=0;ii<c;ii++){
			cv[i][ii].clear();
			u[i][ii]=0;
			if (s[i][ii]=='-'||s[i][ii]=='|'){
				s[i][ii]='-';
				bs.push_back({i, ii});
			}
		}
	}
	assert(bs.size()<=100);
	for (int i=0;i<2*(int)bs.size()+6;i++){
		g[i].clear();
	}
	it=1;
	for (int i=0;i<(int)bs.size();i++){
		fo[i+1]=0;
		int tv=(i+1)*2;
		vector<pair<int, int> > pt1,pt2,pt3,pt4;
		it++;
		path(bs[i].F-1, bs[i].S, -1, 0, pt1);
		it++;
		path(bs[i].F, bs[i].S+1, 0, 1, pt2);
		it++;
		path(bs[i].F+1, bs[i].S, 1, 0, pt3);
		it++;
		path(bs[i].F, bs[i].S-1, 0, -1, pt4);
		it++;
		
		int bad1=isbad(pt1)||isbad(pt3);
		int bad2=isbad(pt2)||isbad(pt4);
		if (bad1){
			addc(tv^1, tv^1);
		}
		else{
			for (auto a:pt1){
				if (s[a.F][a.S]=='.'){
					cv[a.F][a.S].push_back(tv);
				}
			}
			for (auto a:pt3){
				if (s[a.F][a.S]=='.'){
					cv[a.F][a.S].push_back(tv);
				}
			}
		}
		if (bad2){
			addc(tv, tv);
		}
		else{
			for (auto a:pt2){
				if (s[a.F][a.S]=='.'){
					cv[a.F][a.S].push_back(tv^1);
				}
			}
			for (auto a:pt4){
				if (s[a.F][a.S]=='.'){
					cv[a.F][a.S].push_back(tv^1);
				}
			}
		}
	}
	for (int i=0;i<r;i++){
		for (int ii=0;ii<c;ii++){
			if (s[i][ii]=='.'){
				if (cv[i][ii].size()==0) {
					cout<<"IMPOSSIBLE"<<endl;
					return;
				}
				assert(cv[i][ii].size()<=2);
				if (cv[i][ii].size()==1){
					addc(cv[i][ii][0], cv[i][ii][0]);
				}
				else{
					addc(cv[i][ii][0], cv[i][ii][1]);
				}
			}
		}
	}
	vector<vector<int> > sccs;
	SCC(g, 2*(int)bs.size()+4, sccs);
	for (auto co:sccs){
		sort(co.begin(), co.end());
		for (int i=0;i<(int)co.size();i++){
			if (i>0){
				if ((co[i]^1)==co[i-1]){
					cout<<"IMPOSSIBLE"<<endl;
					return;
				}
			}
			int va=co[i]/2;
			if (fo[va]) continue;
			fo[va]=1;
			if (co[i]%2==0) t[va]=1;
			else t[va]=0;
		}
	}
	for (int i=0;i<(int)bs.size();i++){
		int va=i+1;
		assert(fo[va]);
		if (t[va]==0){
			s[bs[i].F][bs[i].S]='|';
		}
		else{
			s[bs[i].F][bs[i].S]='-';
		}
	}
	cout<<"POSSIBLE"<<endl;
	for (int i=0;i<r;i++){
		cout<<s[i]<<endl;
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}