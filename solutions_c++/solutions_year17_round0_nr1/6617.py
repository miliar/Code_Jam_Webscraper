#include <bits/stdc++.h>
#define ll long long
using namespace std;

string flip(string s,int k,int start){
	int i;
	if(start+k>s.length())
		return " ";
	for(i=start;i<start+k;i++){
		if(s[i] == '-')
			s[i] = '+';
		else
			s[i] = '-';
	}
	return s;
}
int getIndex(string s,int k){
	int i,l=s.length();
	if(k>l)
		return -2;
	for(i=0;i<l;i++){
		if(s[i]=='-')
			return i;
	}
	return -1;
}
main(){
	int t,i,j,k,l,count,index,x,f;
	string s,ns;
	cin>>t;
	x=1;
	while(t--){
		count=1;
		f=0;
		cin>>s>>k;
		l = s.length();
		index = getIndex(s,k);
		//cout<<"index "<<index<<endl;
		if(index == -2){
			f=1;
		}
		else if(index == -1){
			count = 0;
		}
		else{
		ns = s;
		while(1){
			ns = flip(ns,k,index);
			//cout<<ns<<endl;
			if(ns[0] == ' '){
				f=1;
				break;
			}
			else{
				index = getIndex(ns,k);
				//cout<<index<<endl;
				if(index==-1)
					break;
				count++;
			}
		}
	}
		if(f==0)
			cout<<"Case #"<<x<<": "<<count<<endl;
		else 
			cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
		x++;
	}
	
}