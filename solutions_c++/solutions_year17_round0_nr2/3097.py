#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	int t;
	cin>>t;
	ll x;
	int v[20],g;
	for(int T=1;T<=t;T++){
		cin>>x;
		for(int i=0;i<20;i++)v[i]=0;
		g=0;
		while(x>0){
			v[g]=x%10;
			x=x/10;
			g++;
		}
		v[g]=-1;
		for(int i=1;i<g;i++){
			if(v[i]>v[i-1]){
				v[i]--;
				for(int j=i-1;j>=0;j--)v[j]=9;
			}
		}
		v[g]=0;
		while(v[g]==0)g--;
		cout<<"Case #"<<T<<": ";
		for(int i=g;i>=0;i--)cout<<v[i];
		cout<<endl;
	}
	return 0;
}
