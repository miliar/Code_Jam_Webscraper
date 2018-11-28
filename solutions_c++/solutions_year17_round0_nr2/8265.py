#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll M[20][500];
ll g(int n, char d){
	if(n==0)return 1LL;
	if(M[n][d]!=-1LL)return M[n][d];
	M[n][d]=0LL;
	for(char dd=d;dd<='9';dd++)
		M[n][d]+=g(n-1,dd);
	return M[n][d];
}
ll ff(ll x){
	string s;
	stringstream st;
	st<<x;
	st>>s;
	ll sum=0LL;
	for(int i=1;i<s.size();i++){
		if(s[i]<s[i-1])return 0;
	}
	return 1;
}
ll f(ll x){
	string s;
	stringstream st;
	st<<x;
	st>>s;
	ll sum=0LL;
	for(int i=0;i<s.size();i++){
		char ini='0';
		if(i>0){
			ini=s[i-1];
			if(s[i-1]>s[i])break;
		}
		for(char d=ini;d<s[i];d++)
			sum+=g(s.size()-i-1,d);
	}
	if(ff(x))sum++;
	return sum;
}
int main(){
	int test;cin>>test;
	ll n;
	memset(M,-1,sizeof M);
	for(int te=1;te<=test;te++){
		cin>>n;
		ll x=f(n);
		
		ll a=0,b=n,c;
		while(b-a>1){
			c=(a+b)/2;
			if(f(c)==x)b=c;
			else a=c;
		}
		
		printf("Case #%d: %lld\n",te,b);
	}
	return 0;
}