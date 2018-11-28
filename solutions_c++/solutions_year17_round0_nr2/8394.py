#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
const int N = 105;
typedef long long ll;
#define prev blgxbvds
int t;
map<ll,ll> vis;
inline int getback(ll x){
	return x%10;
}
inline string to_string(ll x){
	stringstream ss;
	ss << x;
	string res = ss.str();
	return res;
}
inline bool check(ll x){
	string S = to_string(x);
	string Y = S;
	sort(S.begin(),S.end());
	return (S==Y);
}
int main(){
#ifdef srinu73
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
#endif
	queue<ll> q;
	vector<ll> res;
	res.push_back(0);
	q.push(0);
	vis[0]=1;
	while(!q.empty()){
		ll u = q.front();q.pop();
		if(u >= 1e18) break;
		int x = getback(u);
		rep(i,0,9)if(i >= x){
			ll tmp = u*(ll)10 + i;
            if(tmp >= 0 && vis.count(tmp)==0){
				res.push_back(tmp);
				q.push(tmp);
            }
		}
	}
	sort(res.begin(),res.end());
	scanf("%d",&t);
	rep(i,1,t){
		ll n;
		cout << "Case #" << i << ": ";
		cin >> n;
		if(check(n)) cout << n << "\n";
		else {
			auto x = upper_bound(res.begin(),res.end(),n);--x;
			cout << *x << "\n";
		}
	}
}
