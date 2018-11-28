//By SCJ
//#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
int main()
{
ios::sync_with_stdio(0);
cin.tie(0);
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
	int T;cin>>T;
	for(int ca=1;ca<=T;++ca)
	{
		string s;int k;
		cin>>s>>k;
		int ans=0;
		for(int i=0;i<=s.size()-k;++i)
		{
			if(s[i]=='-'){
				ans++;
				for(int j=0;j<k;++j){
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}
			}
		}
		for(int i=s.size()-k+1;i<s.size();++i)
		{
			if(s[i]=='-'){
				ans=-1;break;
			}
		}
		cout<<"Case #"<<ca<<": ";
		if(ans==-1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
}
