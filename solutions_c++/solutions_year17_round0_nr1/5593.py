#include<fstream>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		string str;
		int k;
		cin>>str>>k;
		//string str2;
		int count=0;
		for(int j=0;j<=str.length()-k;j++){
			if(str[j]=='-'){
				for(int x=j;x<k+j;x++){
					if(str[x]=='-')
						str[x]='+';
					else
						str[x]='-';
				}
				//j=j+k-1;
				count++;
			}
		}
		bool is=true;
		for(int j=0;j<str.length();j++){
			if(str[j]=='-'){
				is=false;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(is)
			cout<<count<<endl;
		else
			cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
