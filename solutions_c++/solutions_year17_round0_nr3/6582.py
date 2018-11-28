#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = a; i < (b); ++i)
#define rrep(i,a,b) for(int i = b; i --> (a);)
#define all(v) v.begin(),v.end()
#define trav(x,v) for(auto &x : v)
#define sz(v) (int)(v).size()
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

void solve(){
	int n, k;
	cin >> n >> k;
	priority_queue<int> ko;
	ko.push(n);
	while(--k){
		int a = ko.top();
		ko.pop();
		ko.push((a-1)/2), ko.push(a/2);
	}
	int a = ko.top();
	cout << a/2 << ' ' << (a-1)/2 << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin >> n;
	rep(t,1,n+1){
		cout << "Case #" << t << ": ";
		solve();
	}
}