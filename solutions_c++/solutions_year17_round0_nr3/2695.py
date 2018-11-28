
#include<bits/stdc++.h>

using namespace std;

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define pri(x) printf("%d",x)
#define pll(x) printf("%lld",x)
#define sstr(s) scanf("%s",s)
#define nl printf("\n")
#define ll long long int
#define pii pair<int,int>
#define pLL pair<ll,ll>
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define fr first
#define se second
#define FOR(i,x,y) for(int i=x;i<y;i++)
#define mod 1000000007

int main()
{
    freopen("codejam17c3.in","r",stdin);
    freopen("codejam17c3.out","w",stdout);
    int t; si(t);
    int tc=1;
    while(t--) {
	ll n; sll(n);
	set<ll> pq; pq.insert(n);
	map<ll,ll> m; m.clear();
	m[n] = 1;
	ll k; sll(k);
	ll a1,a2;
	ll cnt = 0;
	while(cnt<k) {
	    ll t1 = *(pq.rbegin());
	    pq.erase(*(pq.rbegin()));
	    ll t2; t2 = m[t1];
	    cnt += t2;
	    ll a,b;
	    a = (t1-1)/2;
	    b = (t1-1)-a;
	    if(cnt>=k) {
		a1 = max(a,b);
		a2 = min(a,b);
		break;
	    }
	    m[a] += t2;
	    m[b] += t2;
	    pq.insert(a);
	    pq.insert(b);
	}
	cout<<"Case #"<<tc++<<": "<<a1<<" "<<a2<<endl;
    }
    return 0;
}
