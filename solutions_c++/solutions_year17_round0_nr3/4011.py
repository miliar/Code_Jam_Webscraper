#include<bits/stdc++.h>
using namespace std;
#define endl '\n'

int main(){
	ios_base::sync_with_stdio(0);cin.tie(NULL);
	int t,n,k,lg,pot,z,mod,p,x,y,l,i;
	cin>>t;
	for(l=1; l<=t; l++){
		cin>>n>>k;
		cout<<"Case #"<<l<<": ";
		lg= log2(k);
		pot= pow(2,lg);
		z= (n+1-pot)/pot;
		mod= (n+1-pot)%pot;
		k= k+1-pot;
		if(mod>=k)
		p= z+1;
		else
		p= z;

		x= p/2;
		y= (p-1)/2;
		cout<<x<<" "<<y<<endl;
	}
}
