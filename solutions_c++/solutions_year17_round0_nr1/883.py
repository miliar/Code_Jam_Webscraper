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

string solve(){
	string s;
	int K;
	cin >> s;
	cin >> K;
	int times=0;
	queue<int> qu;
	bool isReverse=false;
	REP(i,s.size()+1){
		if(!qu.empty() && qu.front()==i){
			qu.pop();
			isReverse^=true;
		}
		if(i==s.size()) break;
		if(s[i]=='-' xor isReverse){
			times++;
			isReverse^=true;
			qu.push(i+K);
		}
	}
	if(!qu.empty()) return "IMPOSSIBLE";
	return to_string(times);
}
int main(){
	int T;
	cin >> T;
	REP(i,T){
		cout << "Case #"<<i+1 <<": "<< solve() << endl;
	}
	return 0;
}