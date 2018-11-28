#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define mp make_pair
#define pb push_back
#define sz(x) ((int) (x).size())
#define db(x) cout << #x" = " << x << endl
#define db2(x,y) cout << #x" = " << x << "; " << #y" = " << y << endl
#define db3(x,y,z) cout << #x" = " << x << "; " << #y" = " << y << "; " << #z" = " << z << endl

#define X first
#define Y second

bool isryb(int r, int y, int b) {
	return max(r, max(y,b)) <= (r+y+b)/2;
}

string solveryb(int r, int y, int b, char R, char Y, char B) {
	int n = r + y + b;
	if (max(r,max(y,b)) > n/2) return "IMPOSSIBLE";
	vector<int> pos;
	for (int i = 0; i < n; i+=2) pos.pb(i);
	for (int j = 1; j < n; j+=2) pos.pb(j);
	string s(n,' ');
	if (r < y) swap(r,y), swap(R,Y);
	if (r < b) swap(r,b), swap(R,B);
	
	for (int i = 0; i < r; i++) s[pos[i]] = R;
	for (int i = 0; i < y; i++) s[pos[i+r]] = Y;
	for (int i = 0; i < b; i++) s[pos[i+r+y]] = B;
	cerr << "s=[" << s << "]" << endl;
	for (int i = 0; i < n; i++) if(s[(i+1)%n] == s[i]) {
		cerr << "i=" << i << endl;
		assert(false);
	}
	return s;
}

vector<string> get(int gg0, int g, char x, char y) {
	vector<string> res;
	for (int i = 0; i < gg0; i++) {
		string cur = "";
		cur.pb(x);
		cur.pb(y);
		cur.pb(x);
		if (i == gg0-1)
		   for (int j = 0; j < g-gg0; j++)
		      {cur.pb(y); cur.pb(x);}
		res.pb(cur);
	}
	return res;
}

string solve(int n, int r, int o, int y, int g, int b, int v) {
	if (n == r + g && r == g) {
		return solveryb(r,g,0,'R','G','-');
	}
	if (n == b + o && b == o) {
		return solveryb(b,o,0,'B','O','-');
	}
	if (n == y + v && y == v) {
		return solveryb(y,v,0,'Y','V','-');
	}
	
	bool found = false;
	int gg0 = -1, go0 = -1, gv0 = -1;
	for (int gg = (g>0?1:0); gg <= g && !found; gg++)
	   for (int go = (o>0?1:0); go <= o && !found; go++)
	      for (int gv = (v>0?1:0); gv <= v && !found; gv++) {
			  if (r >= g + gg && b >= o + go && y >= v + gv
			         && isryb(r-g, y-v, b-o)) {
				  found = true;
				  gg0 = gg;
				  go0 = go;
				  gv0 = gv;
			  }
		  }
	if (!found) return "IMPOSSIBLE";
	string s = solveryb(r-g,y-v,b-o,'R','Y','B');
	//cerr << gg0 << ' ' << go0 << ' ' << gv0 << endl;
	vector<string> rs = get(gg0,g,'R','G'),bs = get(go0,o,'B','O'),
	      ys = get(gv0, v, 'Y', 'V');
	//for (int i = 0; i < sz(rs); i++) cerr << rs[i] << endl;
	//for (int i = 0; i < sz(ys); i++) cerr << ys[i] << endl;
	//for (int i = 0; i < sz(bs); i++) cerr << bs[i] << endl;
	
    string res = "";
    for (int i = 0; i < sz(s); i++) {
		vector<string> &u = rs;
		if (s[i] == 'R') u = rs;
		if (s[i] == 'Y') u = ys;
		if (s[i] == 'B') u = bs;
		if (u.size() > 0) {res += u.back(); u.pop_back();}
		else res += s[i];
		
	}	
	return res;
}

int main()
{
	
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << i << ": " << solve(n,r,o,y,g,b,v) << endl; 
	}
	return 0;
}
