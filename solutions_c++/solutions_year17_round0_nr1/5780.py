#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb(x) push_back(x)
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(auto it = (A.begin()); it!=A.end();it++)
#define FOR(x,A) for(auto x: A)
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0); 
#define fst first
#define snd second
#define sz(v) ((int)v.size())
typedef vector<int> vi;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<ii> vii;

const int INF = 1e9;

int tc;
string s;
int k;
set<int> b;
int ans;

int main(){
	fast_io();
	cin >> tc;
	REP(cn,1,tc+1){
		cin >> s;
		cin >> k;
		b.clear();
		ans = 0;
		REP(i,0,sz(s)){
			char c = s[i];
			int a = ((c == '-') + sz(b)) % 2;
			if (a) {
				ans++;
				b.insert(i+k-1);
			}
			while (!b.empty() && *(b.begin()) <= i) b.erase(b.begin());
		}
		if (!b.empty()) ans = INF;
		cout << "Case #" << cn << ": ";
		if (ans == INF) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}

