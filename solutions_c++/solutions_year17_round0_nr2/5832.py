#include <bits/stdc++.h>
using namespace std;
int main(){
	int tc;
	cin>>tc;
	for(int test=1;test<=tc;test++){
		string s;
		cin>>s;
		reverse(s.begin(),s.end());
		for(int i=0;i<s.size()-1;i++){
			if(s[i]<s[i+1]){
				int pos=i;
				for(int j=0;j<=pos;j++){
					s[j]='9';
				}
				s[pos+1]=s[pos+1]-1;
				if(s[pos]=='0')s.pop_back();
			}
		}
		while(s[s.size()-1]=='0'){
			s.pop_back();
		}
		reverse(s.begin(),s.end());
		printf("Case #%d: %s\n",test,s.c_str());
	}
	return 0;
}
