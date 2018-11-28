#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	ifstream fin("in.txt");
	fin>>t;
	ofstream fout("out.txt");
	
	int cnt=1;

	while(t--){
		string s;
		fin>>s;
		
		for(int i=s.length()-1;i>0;i--){
			if(s[i]<s[i-1]){
					s[i-1]=s[i-1]-1;
					for(int j=i;j<s.length();j++)
						s[j]='9';
			}
		}
	
	
		
		string ans;
		int i=0;
		while(s[i]=='0')i++;
		for(;i<s.length();i++)
			ans+=s[i];
		
		fout<<"Case #"<<cnt<<": "<<ans<<endl;
			cnt++;
	}
	return 0;}
