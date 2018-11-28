#include<bits/stdc++.h>
using namespace std;
#define endl '\n'

int main(){
	ios_base::sync_with_stdio(0);cin.tie(NULL);
	int p,l,n,i;
	long long d,k,s;
	double D,K,V,vel,tmax,t;
	cin>>p;
	for(l=1; l<=p; l++){
		cin>>d>>n;
		cout<<"Case #"<<l<<": ";
		tmax=0;
		D=d;
		for(i=0; i<n; i++){
			cin>>k>>s;
			K=k;
			V=s;
			t=(D-K)/V;
			if(t>tmax)
			tmax= t;
		}
		vel= D/tmax;
		cout<<fixed<<setprecision(6)<<vel<<endl;
	}
}
