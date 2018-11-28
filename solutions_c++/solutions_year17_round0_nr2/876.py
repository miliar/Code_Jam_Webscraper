#include <bits/stdc++.h>
#define FOR(i,a,b) for(ut i=(a);i<(ut)(b);i++)
#define REP(i,b) FOR(i,0,b)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define cat //cout << __LINE__ << endl;
using namespace std;
typedef long long LL;
typedef double ld;
typedef LL ut;
typedef vector<ut> VI;
typedef pair<ut,ut> pr;
typedef vector<pr> Vpr;
typedef pair<ut,ut> prs;
bool able(string s){
	REP(i,s.size()){
		if('0'<=s[i] and s[i]<='9'){
			continue;
		}
		return false;
	}
	REP(i,s.size()-1){
		if(s[i]>s[i+1]){
			return false;
		}
	}
	return true;
}
string solve(){
	string s;
	cin >> s;
	FOR(i,1,s.size()){
		if(able(s)) return s;
		s[s.size()-i]='9';
		s[s.size()-i-1]--;	
	}
	if(s[0]=='0') return s.substr(1,s.size()-1);
	return s;
}
int main(){
	int T;
	cin >> T;
	REP(i,T){
		cout << "Case #"<<i+1 <<": "<< solve() << endl;
	}
	return 0;
}