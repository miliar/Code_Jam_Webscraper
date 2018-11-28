#include <bits/stdc++.h>
using namespace std;
long T,N;

double MaxT,tt,D,K,S;

int main(){
	cin>>T;
	for (int t=1; t<=T; t++){
		cout<<"Case #"<<t<<": ";
		cin>>D>>N;
		MaxT=-100000;
		while(N--){
			cin>>K>>S;
			tt = (D-K)/S;
			if(MaxT < tt)MaxT=tt;
		}
		cout<<fixed<<setprecision(10)<<D/MaxT<<endl;
	}

}