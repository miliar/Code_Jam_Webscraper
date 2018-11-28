#include <bits/stdc++.h>
  
using namespace std;
  
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
  
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
 
const int INF = 1e9;
const ll MOD = 1e9 + 7;
double EPS = 1e-8;

int main(){
	int mCase;
	scanf("%d", &mCase);
	
	for(int Case = 1; Case <= mCase; Case++){
		ll n, k;
		scanf("%ld %ld", &n, &k);
		//cout << n << " " << k << endl;
		priority_queue<ll> q;
		q.push(n);
		ll num = 0LL;
		ll t = n;
		map<ll, ll> mp;
		mp[n] = 1LL;
		for(ll i = 0LL; i < k; i++) {
			t = q.top();
			num += mp[t];
			//cout << " " << i << " " << num << endl;
			if(num >= k) break;
			q.pop();
			if(t & 1) {
				if(mp.count(t/2) == 0) q.push(t/2);
				mp[t/2] += mp[t] * 2LL;
			}
			else {
				if(mp.count(t/2-1) == 0) q.push((t-1)/2);
				if(mp.count(t/2) == 0) q.push(t/2);
				mp[t/2] += mp[t];
				mp[t/2-1] += mp[t];
			}
			//mp.erase(t);
		}
		//int t = q.top();
		printf("Case #%d: %ld %ld\n", Case, t/2, (t-1)/2);
	}
}