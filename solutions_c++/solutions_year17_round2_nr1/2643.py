#include<bits/stdc++.h>

using namespace std;

int main(){
	int t,x,i;
	double d,n,di,s,time;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>t;
	for(int x=1;x<=t;x++){
		time=0.00;
		cin>>d>>n;
		for(i=0;i<n;i++){
			cin>>di>>s;
			if(((d-di)/s)>time) time=(d-di)/s;

		}
		cout<<"Case #"<<fixed<<setprecision(6)<<x<<": "<<d/time<<endl;
	}
	return 0;
}