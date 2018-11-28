#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll ans(ll n){
	ll a[20]={-1};
	ll m=n;
	ll i=0;
	while(m!=0){
		a[i++]=m%10;
		m/=10;
	}
	i--;
	ll j=-1;
	if(i==0) return n;
	while(i>0){
		if(a[i]<a[i-1]) i--;
		else if(a[i]==a[i-1])
			{if(i>j) j=i;
			i--;
			}
		else break;
	}
	if(i==0) return n;
	if(j!=-1) i=j;
	i--;
	//cout<<i<<endl;
	m=0;
	while(i>=0){
		m=m*10+a[i--];
	}
	//cout<<m<<endl;
	n=n-m;
    n--;
	return n;
}
int main() {
	ll t, n, i=0;
	scanf("%lld",&t);
	while(i++<t){
		scanf("%lld",&n);
		printf("Case #%lld: %lld\n", i, ans(n));
	}
	return 0;
}