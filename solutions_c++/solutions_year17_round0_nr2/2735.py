#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sqr(x) ((x)*(x))
#define mp make_pair
#define ones(x) __builtin_popcount(x)
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define debug(x) cout << #x << ": " << x << endl;
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(auto it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define sz(v) int(v.size())

typedef pair<int,int> ii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair< ii, int > tri;
typedef unsigned int uint;

const double PI = acos(-1);
const int  INF = 2e9;
const ll LINF = 1e18 + 5;
const ll MOD = 1e9 + 7;
const int MAXN = 1e5 + 5;
const int MN = 1e6 + 2;



void print(int tt){
	cout << "Case #" << tt << ": ";
}


bool ok(string s){
	int len = sz(s);
	for(int i = 1; i < len; ++i){
		if(s[i] < s[i - 1]) return 0;
	}
	return 1;
}


ll convert(string s){
	ll r = 0;
	int len = sz(s);
	for(int i = 0; i < len; ++i){
		r *= 10;
		r += s[i] - '0';
	}
	return r;
}

int main(){
	fast_io();
	int tc; cin >> tc;
	vector< string > ans;
	vector< ll > num; 
	string s;
	string ss;
	for(int tt = 1; tt <= tc; ++tt){
		cin >> s;
		int len = sz(s);
		ans.clear(); 
		if(ok(s)) ans.pb(s);
		for(int i = 0; i < len - 1; ++i){
			ss = "";
			for(int j = 0; j <= i; ++j) ss.pb(s[j]);
			if(s[i + 1] != '0'){
				ss.pb(s[i + 1] - 1);
				for(int j = i + 2; j < len; ++j)
				ss.pb('9');
			}
			
			if(s[i + 1] != '0' && ok(ss) && ss <= s) ans.pb(ss);
		}
		if(s[0] != '1'){
			ss = "";
			ss.pb(s[0] - 1);
			for(int i = 1; i < len; ++i) ss.pb('9');
			ans.pb(ss); 
		}
		else{
			ss = "";	
			for(int i = 1; i < len; ++i) ss.pb('9');
			if(ss != "") ans.pb(ss); 
		}

		num.clear(); 
		for(int i = 0; i < sz(ans); ++i){
			string tr = ans[i];
			if(tr != ""){
				ll ret = convert(tr);
				num.pb(ret); 
			}
		}
		assert(sz(num) != 0);
		sort(all(num));
		print(tt); 
		cout << num[sz(num) - 1] << endl;
	
	}
	return 0;
}




















