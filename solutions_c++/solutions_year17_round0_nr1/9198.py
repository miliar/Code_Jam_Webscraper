#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("out112.txt");
string s;
int k;
int main()
{
	int t;fin>>t;
	for(int te=1;te<=t;te++){
		fin>>s;
		fin>>k;
		int ans=0;
		bool flag=true;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				ans=ans+1;
				if((i+k)<=s.length()){
					for(int j=i;j<(i+k);j++){
						if(s[j]=='-'){
							s[j]='+';
						}
						else{
							s[j]='-';
						}
					}
				}
				else{
					flag=false;
				}
			}
			if(flag==false){
				break;
			}
		}
		if(flag==true){
			for(int i=0;i<s.length();i++){
				if(s[i]=='-'){
					flag=false;
					break;
				}
			}
		}
		if(flag==true){
			fout<<"Case #"<<te<<": "<<ans<<"\n";
		}
		else{
			fout<<"Case #"<<te<<": IMPOSSIBLE\n";
		}
	}
	return 0;
}
