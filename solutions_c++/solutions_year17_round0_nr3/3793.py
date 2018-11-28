// Template by [thunder_blade]
// IIIT ALLAHABAD
// includes :)

#include<bits/stdc++.h>
using namespace std;
#define TEST  int test_case; cin>>test_case; while(test_case--)
#define all(v) (v).begin(),(v).end()
#define fi  first
#define se  second
#define pb push_back
#define mp make_pair
#define ll long long int
#define SPEED ios_base::sync_with_stdio(false);  cin.tie(0);  cout.tie(0);
#define pi(x) printf("%d\n",x)
#define pl(x) printf("%lld\n",x)
#define pf(x) printf("%f\n",x)
#define ps(x) printf("%s\n",x)
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define sf(x) scanf("%f",&x)
#define ss(x) scanf("%s",x)
#define pis(x) printf("%d ",x)
#define pls(x) printf("%lld ",x)
#define pfs(x) printf("%f ",x)
#define pss(x) printf("%s ",x)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define mod 1000000007
multiset<int>se;
multiset<int>::iterator it, it2;
int main()
{
	int t,i;
	si(t);
	for(int te=1;te<=t;te++){
		se.clear();

		ll n,k,a,b;
		sl(n), sl(k);
		se.insert(n);
		FOR(i,2,k+1){
			it=se.end();
			it--;
			int tmp = *it;
			it2 = se.find(tmp);
			se.erase(it2);
			if(tmp%2){
				a=b=tmp/2;
			}
			else{
				a=tmp/2;
				b=(tmp-1)/2;
			}
			se.insert(a), se.insert(b);
		}
		it=se.end();
		it--;
		int tmp = *it;
		if(tmp%2){
			a=b=tmp/2;
		}
		else{
			a=tmp/2;
			b=(tmp-1)/2;
		}
		printf("Case #%d: %lld %lld\n",te,a, b);
	}
	return 0;
}