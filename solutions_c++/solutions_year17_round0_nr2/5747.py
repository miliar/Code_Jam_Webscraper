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
string t;

void fix(){
	for (int i = sz(t)-1; i > 0; i--){
		if (t[i-1] > t[i]) {
			REP(j,i,sz(t)) t[j] = '9';
			t[i-1]--;
		}
	}
}

int main(){
	fast_io();
	cin >> tc;
	REP(cn,1,tc+1){
		cin >> t;
		fix();
		cout << "Case #" << cn << ": ";
		int flg = 0;
		for (auto c: t){
			if (c != '0') flg = 1;
			if (flg) cout << c;
		}
		cout << endl;
	}
	return 0;
}

