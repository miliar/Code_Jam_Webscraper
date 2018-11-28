#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int check(string s){
	int k;
	for(k=0;k<s.size();k++){
		if(s[k]=='-'){
			return 0;
		}
	}
	return 1;
}

int calculate(string s,int k){
	int c=0,j,flip_count=0;
	while(c<=s.size()-k){
		while(s[c]!='-'){
			c=c+1;
			if(c==s.size()){break;}
		}
		if(c>s.size()-k){break;}
		for(j=c;j<c+k;j++){
			if(j>=s.size()){break;}
			if(s[j]=='+'){s[j]='-';}
			else{s[j]='+';}
			}
			flip_count=flip_count+1;
		}
	if(check(s)==1){
	return (flip_count);}
	else{
		return -1;
	}
}
int main(){
	int t,i,k;
	string s;
	cin>>t;
	int array[t];
	for(i=0;i<t;i++){	
	cin>>s;
	cin>>k;
	array[i]=calculate(s,k);
	}
	for(i=0;i<t;i++){	
		if(array[i]==-1){
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<i+1<<": "<<array[i]<<endl;
		}
	}
	return 0;
}