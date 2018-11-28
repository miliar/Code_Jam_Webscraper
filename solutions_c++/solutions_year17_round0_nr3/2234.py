#include<bits/stdc++.h>
#define int long long
const int inf=1145141919;
const int mod=1000000007;
const int dd[]={0,-1,0,1,0};
using namespace std;
int a,b,c,d;
signed main(){
	int i,j;
	cin>>a;
	for(i=0;i<a;i++){
		int u,v;
		cin>>u>>v;
		int x;
		for(x=1;(1ll<<x)-1<v;x++);
		x--;
		x=(1ll<<x)-1;
		v-=x;
		int y=(u-x)/(x+1);
		int gu,ki;
		if(y%2==0){
			ki=(u-x)%(x+1);
			gu=(x+1)-ki;
			cout<<"Case #"<<i+1<<": ";
			if(v<=ki)
				cout<<y/2<<" "<<y/2<<endl;
			else
				cout<<y/2<<" "<<y/2-1<<endl;
		}else{
			gu=(u-x)%(x+1);
			ki=(x+1)-gu;
			cout<<"Case #"<<i+1<<": ";
			if(v<=gu)
				cout<<y/2+1<<" "<<y/2<<endl;
			else
				cout<<y/2<<" "<<y/2<<endl;
		}
	}
}
