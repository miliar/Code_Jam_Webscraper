#include <iostream>
#include <stdio.h>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
bool check(string s){
	for(int i=0;i<(int)s.length();i++){
		if(s[i]=='-') return false;
	}
	return true;
}
int main(){
	int T;
	ios_base::sync_with_stdio(0);
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-practice.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++){
		int k;
		string s;
		cin>>s>>k;
		int n=s.length();
		int ans=0;
		for(int i=0;i<n;i++){
			if(s[i]=='-' && i+k<=n){
				for(int j=i;j<i+k;j++) s[j]=(s[j]=='+'?'-':'+');
				ans++;
			}
		}
		//cout<<s<<endl;
		if(check(s)) cout<<"Case #"<<t<<": "<<ans<<endl;
		else cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
	}
}

