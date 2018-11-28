#include<bits/stdc++.h>
using namespace std;
#define endl '\n'

int main(){
	ios_base::sync_with_stdio(0);cin.tie(NULL);
	int t,k,tam,lim,nlim,cont,l,i,j;
	string cad;
	cin>>t;
	for(l=1; l<=t; l++){
		cin>>cad>>k;
		cout<<"Case #"<<l<<": ";
		tam= cad.length();
		lim= tam-k;
		cont= 0;
		for(i=0; i<=lim; i++){
			if(cad[i]=='-'){
				cont++;
				nlim= i+k;
				for(j=i; j<nlim; j++){
					if(cad[j]=='+')
					cad[j]= '-';
					else
					cad[j]= '+';
				}
			}
		}
		for(i=0; i<tam; i++){
			if(cad[i]=='-')
			break;
		}
		if(i<tam)
		cout<<"IMPOSSIBLE"<<endl;
		else
		cout<<cont<<endl;
	}
}
