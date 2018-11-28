#include<bits/stdc++.h>
using namespace std;
int tidy(string str,int l){
	int i;
	for(i=1;i<l;i++){
		if(str[i]<str[i-1])
			return -1;
	}
	return 1;
}
int find(string str,int l){
	int i;
	for(i=1;i<l;i++){
		if(str[i]<str[i-1])
			return i-1;
	}
}
int main(){
	int t,x;
	cin>>t;
	for(x=1;x<=t;x++){
		string str;
		int i,j,l;
		cin>>str;
		l=str.length();
		cout<<"Case #"<<x<<": ";
		while(1){
			if(tidy(str,l)==1){
				if(str[0]=='0')
					i=1;
				else
					i=0;
				for(;i<l;i++){
					cout<<str[i];
				}
				cout<<endl;
				break;
			}
			j=find(str,l);
			//cout<<"j"<<j;
			str[j]--;
			for(i=j+1;i<l;i++)
				str[i]='9';
		}
	}
	return 0;
}
