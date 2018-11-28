#include <bits/stdc++.h>
 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define all(v) (v).begin(),(v).end()
 
#define PII pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define pb push_back
#define lint long long int
#define VI vector<int>
 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debug2(x,y) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y <<endl; } 
#define debug3(x,y,z) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y << ", " << #z << " = " << z <<endl; } 
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define debugt(t,n) {{cerr <<#t <<" = "; FOR(it,0,(n)) cerr <<t[it] <<", "; cerr <<endl; }}
 
#define make( x) int (x); scanf("%d",&(x));
#define make2( x, y) int (x), (y); scanf("%d%d",&(x),&(y));
#define make3(x, y, z) int (x), (y), (z); scanf("%d%d%d",&(x),&(y),&(z));
#define make4(x, y, z, t) int (x), (y), (z), (t); scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define makev(v,n) VI (v); FOR(i,0,(n)) { make(a); (v).pb(a);} 
#define IOS ios_base::sync_with_stdio(0)
#define HEAP priority_queue
 
#define read( x) scanf("%d",&(x));
#define read2( x, y) scanf("%d%d",&(x),&(y));
#define read3(x, y, z) scanf("%d%d%d",&(x),&(y),&(z));
#define read4(x, y, z, t) scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define readv(v,n) FOR(i,0,(n)) { make(a); (v).pb(a);}
#define jeb fflush(stdout)
 
 
using namespace std;
 
#define max_n 100015

char s[max_n];


void solve() {
	make(n);
	make3(r,o,y);
	make3(g,b,v);
	if (v == y && n==v+y) {
		FOR(i,0,v) cout<<"VY";
		cout<<endl;
		return;
	}
	if (o==b && n == o+b) {
		FOR(i,0,o) {
			cout << "BO";
		}
		cout << endl;
		return;
	}
	if (r==g && n == r+g) {
		FOR(i,0,r) {
			cout <<"RG";
		}
		cout<<endl;
		return;
	}

	if ( (v >= y && v > 0) || (o >= b && o > 0) || (g >= r && g > 0)) {
		printf("IMPOSSIBLE\n");
		return;
	}
	int ny = y-v, nb = b-o, nr = r-g;
	if (ny > nb + nr || nb > nr + ny || nr > nb + ny) {
		printf("IMPOSSIBLE\n");
		return;
	}
	int m = ny+nb+nr;
	vector<pair<int, char> > w;
	w.pb(mp(ny,'Y')); w.pb(mp(nb,'B')); w.pb(mp(nr,'R'));
	sort(all(w));
	reverse(all(w));
	VI poz;
	for (int i = 0;i < m; i+=2) {
		poz.pb(i);
	}
	for (int i = 1; i <m; i+=2) {
		poz.pb(i);
	}
	int act = 0;
	FOR(i,0,3) 
		FOR(j,0,w[i].st) { 
			s[poz[act]] = w[i].nd;
			act++;
		}
	
	FOR(j,0,m) {
		if (s[j]=='Y' && v!=0) {
			FOR(x,0,v) cout<<"YV";
			cout<<"Y";
			v = 0;
		} else if (s[j]=='B' && o!=0) {
			FOR(x,0,o) cout<<"BO";
			cout<<"B";
			o = 0;
		} else if (s[j]=='R' && g!=0) {
			FOR(x,0,g) cout<<"RG";
			cout<<"R";
			g = 0;
		} else {
			putchar(s[j]);
		}
	}
	cout << endl;
		
	
}


int main() {
	make(z);
	FOR(test,1,z+1) {
		printf("Case #%d: ", test);
		solve();
	}
}	
