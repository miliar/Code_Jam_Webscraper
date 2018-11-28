#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main(){
	
	int t,len,k,res;
	string en;
	cin>>t;
	t++;
	for(int i=1;i<t;i++){
		cin>>en>>k;
		res=0;
		int j;
		len=en.length();
		int l;
		for(j=0;j<len;j++){
			if(en[j]=='-'){
				res++;
				if(j+k-1>=len){
					break;
				}
				for(l=j+1;l<k+j;l++){
					en[l]=(en[l]=='-')?'+':'-';
				}
			}
		}
		if(j==len){
			cout<<"Case #"<<i<<": "<<res<<endl;
		}
		else{
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	
	return 0;
}
