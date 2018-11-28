#include <bits/stdc++.h>

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define FOR(i,n) REP(i,0,(int)n-1)
#define mp make_pair
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define VI vector<int>
#define fi first
#define se second
#define pss pair<short int, short int>

set<int> getDig(int x) {
	set<int> res;
	if(x == 0) res.insert(0);
	while(x>0) {
		res.insert(x%10);
		x/=10;
	}
	return res;
}

void solve() {
	string s;
	int k;
	cin>>s>>k;
	//cout<<s<<"\n"<<k<<"\n";
	int res = 0;
	FOR(i,s.size()) {
		if(i + k - 1 >= s.size()) break;
		if(s[i] == '+') continue;
		else {
			res++;
			for(int j=i; j<i+k; j++) {
				if(s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
		}
		//cout<<s<<"\n";
	}
	FOR(i,s.size()) {
		if(s[i] == '-') {
			cout<<"IMPOSSIBLE\n";
			return;
		}
	}
	cout<<res<<"\n";
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}