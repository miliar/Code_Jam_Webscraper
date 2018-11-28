#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;

template<typename T>
using pq_gt = priority_queue<T, vector<T>, greater<T>>;
template<typename T>
using pq_lt = priority_queue<T, vector<T>, less<T>>;

#define se second
#define fi first
#define pb push_back
#define mp make_pair

const long double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

pii R[2000];


long double compu(ll r, ll h) {
	return pi * (long double) (2 * r * h);
}

bool comp(const pii& i, const pii& j) {
	if(compu(i.se, i.fi) == compu(j.se, j.fi)) {
		return i.se > j.se;
	} else return compu(i.se, i.fi) > compu(j.se, j.fi);
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int testcase = 1; testcase <= t; testcase++) {
    	printf("Case #%d: ", testcase);
    	ll k,n;
    	cin>>n>>k;
    	for(int i = 0; i < n; i++) {
    		cin>>R[i].se>>R[i].fi;
    	}
    	sort(R, R+n, comp);
    	long double ans = 0;
    	for(int i = 0; i < n; i++) {
    		int cnt = 1;
    		long double a= 0;
    		//ll r = R[i].se;
    		for(int j = 0; cnt < k; j++) {
    			if(i==j) {
    				continue;
    			}
    			cnt++;
    			a += compu(R[j].se, R[j].fi);
    		}
    		long double temp = compu(R[i].se, R[i].fi);
    		temp += a;
    		temp += pi*R[i].se*R[i].se;
    		ans = max(ans, temp);
    	}
    	cout<<fixed<<setprecision(10)<<ans<<endl;

    }
}