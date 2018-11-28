#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back
#define rs resize

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

int r, c;
vector<vector<char> > huis;
vector<vector<vector<multiset<int> > > > besplek;

vvi adj, comps;
vi tidx, lnk, cnr, st;
vector<bool> vis;
int age, ncomps;

void tarjan(int v) {
	tidx[v] = lnk[v] = ++age;
	vis[v] = true;
	st.pb(v);

	for (int w : adj[v]) {
		if (!tidx[w]) tarjan(w), lnk[v] = min(lnk[v], lnk[w]);
		else if (vis[w]) lnk[v] = min(lnk[v], tidx[w]);
	}

	if (lnk[v] != tidx[v]) return;

	comps.pb(vi());
	int w;
	do {
		vis[w = st.back()] = false;
		cnr[w] = ncomps;
		comps.back().pb(w);
		st.pop_back();
	} while (w != v);
	ncomps++;
}

void findSCC(int n) {
	age = ncomps = 0;
	vis.assign(n, false);
	tidx.assign(n, 0);
	lnk.resize(n);
	cnr.resize(n);
	comps.clear();

	for (int i = 0; i < n; i++)
		if (tidx[i] == 0) tarjan(i);
}

void init2sat(int n) { adj.clear(); comps.clear(); tidx.clear(); lnk.clear(); cnr.clear(); st.clear(); vis.clear();
 adj.assign(2 * n, vi()); }

// vl, vr = true -> variable l, variable r should be negated.
void imply(int xl, bool vl, int xr, bool vr) {
	adj[2 * xl + vl].pb(2 * xr + vr);
	adj[2 * xr +!vr].pb(2 * xl +!vl);
}

void satOr(int xl, bool vl, int xr, bool vr) { //cerr << xl << "is " << vl << " or " << xr << " is " << vr << endl; 
imply(xl, !vl, xr, vr); }
void satConst(int x, bool v) { //cerr << x << " is " << v << endl;
 imply(x, !v, x, v); }
void satIff(int xl, bool vl, int xr, bool vr) {
	imply(xl, vl, xr, vr);
	imply(xr, vr, xl, vl);
}

bool solve2sat(int n, vector<bool> &sol) {
	findSCC(2 * n);
	for (int i = 0; i < n; i++)
		if (cnr[2 * i] == cnr[2 * i + 1]) return false;
	vector<bool> seen(n, false);
	sol.assign(n, false);
	for (vi &comp : comps) {
		for (int v : comp) {
			if (seen[v / 2]) continue;
			seen[v / 2] = true;
			sol[v / 2] = v & 1;
		}
	}
	return true;
}

/*
 0
3 1
 2
*/

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

void visit(int a, int up, int x, int y, int rich){
  //cout << a << " " << up << " " << x << " " << y << " " << rich << endl;
  if(besplek[x][y][up].count(a) > 1)
    throw 0;
  besplek[x][y][up].insert(a);
  int nx = x + dx[rich];
  int ny = y + dy[rich];
  //cout << a << " " << up << " " << nx << " " << ny << " " << rich << endl;
  if(nx < 0 || nx >= r || ny < 0 || ny >= c)
    return;
  switch(huis[nx][ny]){
    case '.': visit(a,up,nx,ny,rich); break;
    case '#': return;
    case '-': case '|': visit(a,up,nx,ny,rich); break;
    case '/': visit(a,up,nx,ny,rich^1); break;
    case '\\': visit(a,up,nx,ny, 3-rich); break;
  }
}

void test(){
  besplek.clear();
  cin >> r >> c;
  huis.clear();
  huis.resize(r);
  besplek.rs(r);
  vii bes;
  for(int i = 0 ; i < r ; i++){
    huis[i].resize(c);
    besplek[i].rs(c);
    for(int j = 0 ; j < c ; j++){
      besplek[i][j].rs(2);
      cin >> huis[i][j];
      if(huis[i][j] == '-' || huis[i][j] == '|')
        bes.pb(mp(i,j));
    }
  }
  for(int i = 0 ; i < bes.size(); i++){
    int x = bes[i].first, y = bes[i].second;
    try{
    visit(i,0,x,y,0);
    visit(i,0,x,y,2);
    visit(i,1,x,y,1);
    visit(i,1,x,y,3);
    }
    catch(int e){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  init2sat(bes.size());
  vector<pair<bool, bool> > zet(bes.size());
  for(int i = 0 ; i < bes.size(); i++)
    zet[i].first = zet[i].second = false;
  for(int i = 0 ; i < bes.size(); i++){
    int x = bes[i].first, y = bes[i].second;
    
    for(int j : besplek[x][y][0]){
      if(i == j) continue;
      satConst(j,false);
      zet[j].first = true;
    }
    for(int j : besplek[x][y][1]){
      if(i == j) continue;
      satConst(j,true);
      zet[j].second = true;
    }
   // if
  }
  for(int i = 0 ; i < r ; i++){
    for(int j = 0 ; j < c ; j++){
      if(huis[i][j] != '.')
        continue;
      int a = -1;
      for(int k : besplek[i][j][0]){
        if(zet[k].first)
          continue;
        assert(a == -1);
        a = k;
      }
      int b = -1;
      for(int k : besplek[i][j][1]){
        if(zet[k].second)
          continue;
        assert(b == -1);
        b = k;
      }
      if( a == -1 && b == -1){
        cout << "IMPOSSIBLE" << endl;
        return;
      }
      if( a == -1){
        satConst(b,false);
      }
      else if( b== -1)
        satConst(a,true);
      else
        satOr(a,true,b,false);
    }
  }
  vector<bool> sol;
  if(!solve2sat(bes.size(),sol)){
    cout << "IMPOSSIBLE" << endl;
        return;
  }
  for(int i = 0 ; i < bes.size(); i++){
    int x = bes[i].first, y = bes[i].second;
    huis[x][y] = (sol[i] ? '|' : '-');
  }
  cout << "POSSIBLE" << endl;
  for(int i = 0 ; i < r ; i++){
    for(int j = 0 ; j < c ; j++){
      cout << huis[i][j];
    }
    cout << endl;
  }
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
