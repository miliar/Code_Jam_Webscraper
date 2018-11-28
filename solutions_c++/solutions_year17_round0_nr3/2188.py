#include <bits/stdc++.h>
#define N 10
#define M 18

using namespace std;
typedef long long ll;
int t;
string s;
ll n,k;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>t;
	for(int c=1;c<=t;++c) {
		cin>>n>>k;
		ll i = 1;
		ll p = n;
		ll cnt1 = 1;
		ll cnt2 = 0;
		while(k>i) {
			ll new_cnt1 = 0;
			ll new_cnt2 = 0;
			if(p%2==1) {
			 	new_cnt1 = 2*cnt1+cnt2;
				new_cnt2 = cnt2;
			} else {
				new_cnt1 = cnt1;
				new_cnt2 = cnt1+2*cnt2;
			}
			cnt1 = new_cnt1;
			cnt2 = new_cnt2;
			p = (p-1)/2;
			k-=i;
			i = (i<<1);
		}
		if(k<=cnt2) {
			ll ans1 = p/2;
			ll ans2 = p-ans1;
			if(ans2>=ans1)
				swap(ans1,ans2);
			cout<<"Case #"<<c<<": "<<ans1<<" "<<ans2<<"\n";
		} else {
			ll ans1 = (p-1)/2;
			ll ans2 = p-1-ans1;
			if(ans2>=ans1)
				swap(ans1,ans2);
			cout<<"Case #"<<c<<": "<<ans1<<" "<<ans2<<"\n";
		}
	}
	return 0;
}
