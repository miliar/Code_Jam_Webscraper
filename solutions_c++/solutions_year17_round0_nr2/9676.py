#include<bits/stdc++.h>
using namespace std;
ifstream fin("B-small-attempt0.in");
ofstream fout("out113.txt");
int main(){
	int t;fin>>t;
	for(int te=1;te<=t;te++){
		string s;fin>>s;
		bool flag=true;
		for(int i=0;i<s.length()-1;i++){
			if(s[i]<=s[i+1]){
				
			}
			else{
				flag=false;
				for(int j=i-1;j>=0;j--){
					if(s[j]!=s[i]){
						flag=true;
						s[j+1]=s[j+1]-1;
						for(int k=j+2;k<s.length();k++){
							s[k]='9';
						}
					}
				}
				if(flag==false){
					s[0]=s[0]-1;
					for(int j=1;j<s.length();j++){
						s[j]='9';
					}
				}
				break;
			}
		}
		if(s[0]=='0'){
			string s1="";
			for(int i=1;i<s.length();i++){
				s1+=s[i];
			}
			fout<<"Case #"<<te<<": "<<s1<<"\n";
		}
		else{
			fout<<"Case #"<<te<<": "<<s<<"\n";
		}
	}
	return 0;
}
