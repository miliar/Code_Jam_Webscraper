#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	int t,d;
	ll n,i,j,k=0;
	cin>>t;
	while(t--){
		k++;
		cin>>n;
		for(i =n ; i>=1 ; i--){
			j=i;
			d=j%10;
			j=j/10;
			int flag=1;
			while(j>0){
				if(j%10<=d){
					d=j%10;
					j=j/10;
				}
				else{
					flag=0;
					break;
				}
			}
			if(flag){
				cout<<"Case #"<<k<<": "<<i<<endl;
				break;
				}	
			}
		
	}
	return 0;
}