#include<bits/stdc++.h>
#define int long long
const int inf=1145141919;
const int dd[]={0,-1,0,1,0};
using namespace std;
int a,b,c,d;
void solve(string s,int u){
	int v=0,i;
	for(i=0;i<s.size()-u+1;i++){
		if(s[i]=='-'){
			v++;
			for(int j=0;j<u;j++){
				if(s[i+j]=='+')
					s[i+j]='-';
				else
					s[i+j]='+';
			}
		}
	}
	for(;i<s.size();i++)
		if(s[i]=='-'){
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
	cout<<v<<endl;
}
signed main(){
	cin>>a;
	for(int i=0;i<a;i++){
		string s;
		cin>>s;
		int u;
		cin>>u;
		cout<<"Case #"<<i+1<<": ";
		solve(s,u);
	}
}
