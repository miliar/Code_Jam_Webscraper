#include<bits/stdc++.h>
using namespace std;
#define endl '\n'

int size_num(long long n){
	int cont;
	while(n>0){
		n/=10;
		cont++;
	}
	return(cont);
}

int main(){
	ios_base::sync_with_stdio(0);cin.tie(NULL);
	int t,l,i,j,tam;
	long long n,k,x;
	cin>>t;
	for(l=1; l<=t; l++){
		cin>>n;
		cout<<"Case #"<<l<<": ";
		tam= size_num(n);
		vector<int> num(tam);
		k= n;
		for(i=tam-1; i>=0; i--){
			x= k%10;
			k/=10;
			num[i]= x;
		}
		for(i=tam-2; i>=0; i--){
			if(num[i]>num[i+1]){
				num[i]--;
				for(j=i+1; j<tam; j++){
					num[j]= 9;
				}
			}
		}
		for(i=0; i<tam; i++){
			if(i!=0 || num[i]!=0)
			cout<<num[i];
		}
		cout<<endl;
	}
}
