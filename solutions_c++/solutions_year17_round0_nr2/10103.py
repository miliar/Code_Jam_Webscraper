#include<iostream>

using namespace std;

void calc(string k){
	for(int i=1; i<k.length(); i++){
		if(k[i]<k[i-1]){
			for(int j=i; j>0; j--){
				if((k[j-1]>k[j] && k[j-1]>k[j-2] ) || j==1){
					k[j-1]--;
					for(int l=j; l<k.length(); l++){
						k[l]='9';
					}
					break;
				}
			}
			break;
		}
	}
	if(k[0]!='0'){
		cout<<k[0];
	}
	for(int i=1; i<k.length(); i++){
		cout<<k[i];
	}
}

int main(){
	int t;
	cin>>t;
	for(int x=1; x<=t; x++){
		string k;
		cin>>k;
		cout<<"Case #"<<x<<": ";
		calc(k);
		cout<<endl;
	}
	return 0;
}
