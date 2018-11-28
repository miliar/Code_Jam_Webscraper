#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main(){
	ll a,b,t,k,n;
	cin>>t;
	for(int p=1; p<=t; p++){
		ll ct=1;
		cin>>n>>k;
		map<ll,ll> M;
		map<ll,ll>::iterator i;
		b=(n-1)/2;
		a=n-b-1;
		M[a]++;
		M[b]++;
		while(ct<k){
			//cout<<a<<" "<<b<<endl;
			//cout<<ct<<endl;
			i=--M.end();
			b=((*i).first-1)/2;
			a=(*i).first-b-1;
			ct+=(*i).second;
			M[a]+=(1*(*i).second);
			M[b]+=(1*(*i).second);
			M.erase(i);
		}
		
		cout<<"Case #"<<p<<": "<<a<<" "<<b<<"\n";
	}
	return 0;
}
