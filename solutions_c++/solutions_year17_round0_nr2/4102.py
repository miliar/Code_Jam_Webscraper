#include<bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int n,m;cin>>n;m=n;
		for(int i=1,x=10;(x<=m)&&(x>0);x*=10,i++){
			//cout<<(i<10?"00":"0")<<i<<" ";
			int m1=(m%(x*10))/(x),m2=(m%(x))/(x/10);
			//m1=m1/(x);m2=m2/(x/10);
			//cout<<m1<<" "<<m2;
			if(m1>m2){
				//cout<<" [if] ";
				m/=(x);//cout<<" "<<m;
				m*=(x);//cout<<" "<<m;
				m--;//cout<<" "<<m;
			}
			//cout<<" "<<m<<" "<<x<<endl;
		}
		//cout<<endl;
		cout<<"Case #"<<t<<": "<<m<<endl;//<<endl;
	}
	return 0;
}
