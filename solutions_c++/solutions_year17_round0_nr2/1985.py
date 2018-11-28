#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	int t;
	cin>>t;int cs=0;
	while(t--){
		cs++;
		string x;
		cin>>x;
		char c=x[0];
		bool f=1;
		for (int i=1;i<x.size();i++)
			if (x[i]<c){
				int t=0;
				for (t=i-1;t>=1;t--)if (x[t]!=x[t-1])break;
				x[t]--;
				for (int j=t+1;j<x.size();j++)x[j]='9';
				break;
			}
			else c=x[i];
		if (x[0]!='0')
			cout<<"Case #"<<cs<<": "<<x<<endl;
		else{
			cout<<"Case #"<<cs<<": ";
				for (int i=1;i<x.size();i++)cout<<x[i];
			cout<<endl;
		}
	}
}
