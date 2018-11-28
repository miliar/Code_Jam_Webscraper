#include<bits/stdc++.h>

using namespace std;
string s;
int k;
int caso=1;
int ans;

void doit(){
	for(int i=0;i+k<=s.size();i++){
		if(s[i]=='-'){
			ans++;
			for(int j=i;j<i+k;j++){
				if(s[j]=='-') s[j]='+';
				else s[j]='-';
			}
		}
	}
	for(int i=s.size()-k;i<s.size();i++){
		if(s[i]=='-') ans=-1;
	}	
}

int main(){
	int t;cin>>t;
	while(t--){
		cin>>s>>k;
		ans=0;
		doit();
		cout<<"Case #"<<caso++<<": ";
		if(ans>-1) cout<<ans<<'\n';
		else cout<<"IMPOSSIBLE"<<'\n';
	}
}
