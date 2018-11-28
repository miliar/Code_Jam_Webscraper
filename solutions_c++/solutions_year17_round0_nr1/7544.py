#include<bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	freopen("cjam.in","r",stdin);
	freopen("cjam.out","w",stdout);
	int t;
	cin>>t;
	for(int te=1;te<=t;te++){
		string s;
		cin>>s;
		int k,cnt=0,flag=0;
		cin>>k;
		for(int i=0;i+k<=s.length();i++){
			if(s[i]=='-'){
				for(int j=i;j<i+k;j++){
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
				cnt++;
			}
		}
		for(int i=0;i<s.length();i++){
			if(s[i]=='-')
				flag=1;
		}
		cout<<"Case #"<<te<<": ";
		if(flag)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<cnt<<"\n";
	}
	return 0;
}
