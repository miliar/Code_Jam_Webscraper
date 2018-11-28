//-----------EL FUTURO ES INCIERTO---------//
#include <bits/stdc++.h>
#include <sstream>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);
#define clr(a,v) memset(a, v, sizeof(a))
#define trace(x) cerr << #x << ": " << x << '\n'
#define trace2(x,y) cerr << #x << ": " << x << " | " << #y << ": " << y << '\n';
#define trace3(x,y,z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << '\n';
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sz(v) ((int)v.size())
#define REP(i,x,y) for(long long (i)=(x);(i)<(y);(i)++)
#define RREP(i,x,y) for(long long (i)=(x);(i)>=(y);(i)--)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define mp make_pair
#define mt(x,y,z) mp((x),mp((y),(z)))
#define fst first
#define snd second
#define ones(x) __builtin_popcountll(x)
#define gcd __gcd
#define MOD 1000000007
#define oo 1e8
#define itm1 fst
#define EPS 1e-3
#define itm2 snd.fst
#define itm3 snd.snd
typedef unsigned long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef pair<ll,ii> tri;
typedef vector<tri> vt;

bool ok(string& s, int& pos){
	REP(i,0,sz(s)-1){
		if(s[i] > s[i+1]){
			pos = i; return false;
		}
	}
	return true;
}

int main(){
	fastio;
	int t; cin >> t;
	REP(tc,1,t+1){
		cout << "Case #" << tc << ": ";
		string s; cin >> s;
		int pos = -1;
		while(!ok(s,pos)){
			s[pos]--;
			REP(i,pos+1,sz(s)) s[i] = '9';
		}
		while(s[0] == '0') s.erase(0,1);
		cout << s << endl;
	}
	return 0;
}