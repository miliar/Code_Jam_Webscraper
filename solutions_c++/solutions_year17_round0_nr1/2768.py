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

int used[2000];

int main(){
	fast_io();
	int tc; cin >> tc;
	int k;
	string s;
	for(int tt = 1; tt <= tc; ++tt){
		cin >> s >> k;
		int len = sz(s);
		for(int i = 0; i < len; ++i) 	
			if(s[i] == '+') used[i] = 0;
			else used[i] = 1;
		int cnt = 0;
		for(int i = 0; i <= (len - k); ++i){
			if(used[i]) cnt++;
			int apply = used[i]; 
			for(int j = i; j < (i + k); ++j) used[j] ^= apply; 
		}

		for(int i = 0; i < len; ++i) 
			if(used[i]) cnt = -1;
		print(tt);
		if(cnt == -1){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout << cnt << endl; 
		}
		
	}
	return 0;
}


















