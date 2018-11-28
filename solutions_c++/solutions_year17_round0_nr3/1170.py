#include <cstdio>
#include <cstring>
#include <map>
#include <queue>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define for_iter(i,n) for (__typeof(n.begin())i=n.begin();i!=n.end();++i)
typedef long long ll;
map<ll,ll> M,inq;
priority_queue<ll> Q;
ll n,k,ans;

void decomp(ll n) {
	while (!Q.empty()) Q.pop();
	M[n]=1;
	Q.push(n);
	ll sum=0;
	while (!Q.empty()) {
		n=Q.top();
		sum+=M[n];
		if (sum>=k) {
			ans=n;
			return;
		}
		Q.pop();
		if (n==1) continue;
		n--;
		if (!inq[n-n/2]) {
			Q.push(n-n/2);
			inq[n-n/2]=true;
		}
		M[n-n/2]+=M[n+1];
		if (n/2>0 && !inq[n/2]) {
			Q.push(n/2);
			inq[n/2]=true;
		}
		M[n/2]+=M[n+1];
	}
}

ll solve() {
	M.clear();
	inq.clear();
	decomp(n);
	/*
	for (auto i : M) {
		printf("%lld %lld\n", i.first, i.second);
	}
	*/
	return ans;
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%lld%lld\n",&n,&k);
		ll x=solve()-1;
		printf("%lld %lld\n",x-x/2,x/2);
	}
	return 0;
}
