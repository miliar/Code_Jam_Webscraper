#include<bits/stdc++.h>
using namespace std;
#define fi first
#define sec second
#define pi 3.1415926535897932384
#define mp make_pair
#define ll long long
multiset< double >se;
pair<ll,ll>a[10005];
int main()
{
	ll i,j,k,l,m,n,t,cnt;
	pair<ll,ll> pa;
	cin >> t;
	multiset< double > :: iterator it;
	double ma,an;
	for(l = 1;l <= t;l++){
		cin >> n >> k;
		for(i = 0;i < n;i++){
			cin >> a[i].fi >> a[i].sec;
		}
		cout << "Case #" << l << ": ";
		sort(a,a+n);
		se.clear();
		for(i = 0;i < n;i++){
			se.insert(2*pi*a[i].sec*a[i].fi);
		}
		ma = 0;
		reverse(a,a+n);
//		cout << "hey" << endl;
		for(i = 0;i < n;i++){
			se.erase(se.find(2*pi*a[i].sec*a[i].fi));
//			cout << i << endl;
			if(se.size() < k-1){
				break;
			}
			it = se.end();
			if(se.size() != 0)
			it--;
			an = pi*a[i].fi*a[i].fi;
			an += 2*pi*a[i].sec*a[i].fi;
			cnt = 1;
			for(;cnt != k;cnt++,it--){
				an += *it;
			}
			if(ma < an){
				ma = an;
			}
//			cout << i << endl;
		}
		printf("%.9lf\n",ma);
	}
}




