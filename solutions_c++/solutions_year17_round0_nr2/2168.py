#include<bits/stdc++.h>
#define int long long
const int inf=1145141919;
const int dd[]={0,-1,0,1,0};
using namespace std;
int a,b,c,d;
int solve(int u){
	int v=u,x,y=10,z=1;
	while(v){
		int x=v%10;
		if(x>y){
			u=v*z-1;
			y=x-1;
		}else
			y=x;
		v/=10;
		z*=10;
	}
	return u;
}
signed main(){
	cin>>a;
	int i,j;
	for(i=0;i<a;i++){
		int u;
		cin>>u;
		cout<<"Case #"<<i+1<<": "<<solve(u)<<endl;
	}
}
