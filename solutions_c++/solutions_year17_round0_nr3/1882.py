#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int, int> mii;
typedef map<string, int> msi;

#define zero(arr) memset((arr), 0, sizeof (arr))
#define init(arr) memset((arr), -1, sizeof (arr))

map<ll, ll> mp;
set<ll> st;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	
	cin>>t;
	
	for(int cs = 1; cs <= t; cs++) {
		ll n, k;
		
		cin>>n>>k;
		
		mp.clear();
		st.clear();
		mp[n] = 1;
		
		priority_queue<ll> q;
		q.push(n);
		
		ll l = 0, r = 0;
		
		while(!q.empty()) {
			ll cur = q.top();
			q.pop();
			
			k -= mp[cur];
			
			
			if(k <= 0) {
				l = cur/2;
				r = cur/2;
				if(cur%2==0)
					r--;
				break;
			}
			
			if(cur%2 == 0) {
				mp[cur/2] += mp[cur];
				mp[cur/2-1] += mp[cur];
				
				if(st.find(cur/2) == st.end()) {
					q.push(cur/2);
					st.insert(cur/2);
				}
				if(st.find(cur/2-1) == st.end()) {
					q.push(cur/2-1);
					st.insert(cur/2-1);
				}
			}
			else {
				mp[cur/2] += 2*mp[cur];
				if(st.find(cur/2) == st.end()) {
					q.push(cur/2);
					st.insert(cur/2);
				}
			}
		}
		
		cout<<"Case #"<<cs<<": "<<l<<' '<<r<<endl;
	}
		
	return 0;
}

