#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

int pancake(string &s,int k){
	int n=s.length();
	int flag=-1;
	for(int i=0;i<n;i++){
		if(s[i]=='-'){
			flag=i;
			break;
		}
	}
	//cout<<flag<<" "<<n<<" "<<k<<" "<<s<<endl;
	if(flag==-1) return 0;
	if(flag>n-k) return -1;
	for(int i=flag;i<flag+k;i++){
		if(s[i]=='-') s[i]='+';
		else s[i]='-';
	}
	int res=pancake(s,k);
	if(res==-1) return -1;
	return res+1;
}

int main(){
	int n;
	cin>>n;
	vector<string> str;
	vector<int> k;
	for(int i=0;i<n;i++){
		string s;
		int temp;
		cin>>s>>temp;
		str.push_back(s);
		k.push_back(temp);
	}
	for(int i=0;i<n;i++){
		int res=pancake(str[i],k[i]);
		cout<<"Case #"<<i+1<<": ";
		if(res==-1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<res<<endl;
	}
}