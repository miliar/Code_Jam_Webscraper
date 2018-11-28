#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define sz size()
#define pii pair< ll ,ll >
#define mp make_pair
#define ff first
#define ss second
#define all(v) (v).begin(),(v).end()

pii f(ll n)
{
	if(n%2 == 0){

		return mp(n/2LL,(n/2LL)-1LL);
	}
	n--;
	return mp(n/2LL,n/2LL);
}

void get(ll x,ll y,ll &n1,ll &n2,ll &t1,ll &t2)
{
	ll mn,mx;
	pii a,b;
	a = f(x);
	b = f(y);

	mn = min(a.ss,b.ss);
	mx = max(a.ff,b.ff);

	ll r1=0,r2=0;

	if(a.ff == mx)r1++;
	if(a.ss == mx)r1++;

	if(b.ff == mx)r2++;
	if(b.ss == mx)r2++;

	ll q = t1;
	t1 = (t1*r1) + (t2*r2);
	t2 = (q* (2LL-r1)) + (t2 * (2LL-r2));

	n1 = mx;
	n2 = mn;
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);
	
	ll t,n,k;

	cin >> t;

	for(int cases  = 1;cases <= t;cases++){

		cin >> n >> k;

		cout << "Case #" << cases << ": ";

		if(k == n){

			cout << 0 << ' ' << 0 << endl;
			continue;
		}
		if(k == 1){

			pii ans = f(n);
			cout << ans.ff << ' ' << ans.ss <<endl;
			continue;
		}
		ll n1=n,n2=n;
		ll t1=1,t2=1,cur=1;
		int p=1;

		while(1){

			//cout << n1 << ' ' <<n2 << ' '<< t1 << ' ' << t2 << ' '<< cur << endl;

			if(p==1){

				n1 = f(n).ff;
				n2 = f(n).ss;
				t1 = t2 = 1LL;
			}
			else get(n1,n2,n1,n2,t1,t2);

			if(cur+t1 >= k){

				pii ans = f(n1);
				cout << ans.ff << ' '<< ans.ss << endl;
				break;
			}
			cur +=t1;
			if(cur+t2 >= k){

				pii ans = f(n2);
				cout << ans.ff << ' '<< ans.ss << endl;
				break;
			}
			cur += t2;
			p++;
		}
	}
	return 0;
}