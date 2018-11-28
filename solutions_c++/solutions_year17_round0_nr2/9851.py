#include <bits/stdc++.h>
#define ll long long int
using namespace std;
ll maximo;

ll potencia(ll p){
	if(!p) return 1;
	ll res=10;
	for(int i=1;i<p;i++){
		res*=10;
	}
	return res;
}

ll tidy(ll ini, ll val, ll pot, ll& n){
	//cout<<"Entrada "<<ini<<" "<<val<<" "<<pot <<endl;
	maximo=max(maximo, val);
	ll aux=potencia(pot);
	ll maxlocal=0;
	if(aux+val < n) ;
	for(int i=ini; i>0; i--){
		//cout<<aux*i<<" "<<val<<" "<<maximo<<endl;
		//if(aux*i+val<maximo) return maximo;
		if(aux*i+val<=n) {
			tidy(i , aux*i+val, pot+1, n);
		//	cout<<endl;
		}
	}
}
int main(){
	int t;
	cin>>t;
	long long int n;
	for(int i=1;i<=t;i++){
		cin>>n;
		maximo=-1;
		tidy(9,0,0,n);
		cout<<"Case #"<<i<<": "<<maximo<<'\n';
	}
	return 0;
}