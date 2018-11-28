#include <bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int y=0;y<t;y++){
		string str;cin>>str;
		int k;cin>>k;
		int cou=0;
		for(int i=0;i<str.length();i++){
			if(str[i]=='-' && i<=str.length()-k){
				cou++;
				str[i]='+';
				for(int j=i+1;j<i+k;j++){
					if(str[j]=='+')
						str[j]='-';
					else
						str[j]='+';
				}
			}
		}
		int mark=0;
		for(int i=0;i<str.length();i++){
			if(str[i]=='-'){
				mark=1;
				break;
			}
		}
		if(mark==1){
			cout<<"Case #"<<y+1<<": "<<"IMPOSSIBLE\n";
		}
		else
			cout<<"Case #"<<y+1<<": "<<cou<<endl;
	}
	return 0;
}