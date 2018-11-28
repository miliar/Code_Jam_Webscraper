#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++) {
		ll n1,k;
		cin>>n1>>k;
		ll n2=n1-1;
		ll cnt1=1;
		ll cnt2=0;
		while (cnt1+cnt2<k) {
			k-=cnt1+cnt2;
			ll nn1=n1/2;
			ll nn2=nn1-1;
			ll ccnt1=cnt1;
			ll ccnt2=cnt2;
			if (n1%2==1) ccnt1+=cnt1+cnt2;
			else ccnt2+=cnt1+cnt2;
			n1=nn1;
			n2=nn2;
			cnt1=ccnt1;
			cnt2=ccnt2;
		}
		cout<<"Case #"<<tc<<": ";
		if (cnt1>=k) cout<<n1/2<<" "<<(n1-1)/2<<"\n";
		else cout<<n2/2<<" "<<(n2-1)/2<<"\n";
	}
}
