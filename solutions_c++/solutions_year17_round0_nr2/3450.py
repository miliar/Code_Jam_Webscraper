#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long LL;

LL N,Ans;

void Check(LL X){
	//cerr<<X<<"\n";
	for(LL b=10;b<=X;b*=10){
		LL dhigh=(X/b)%10;
		LL dlow=(X/(b/10))%10;
		if(dhigh>dlow) return;
	}
	if(X>Ans) Ans=X;
}

void Solve(){
	Ans=1;
	Check(N);
	for(LL b=1;b<=N;b*=10){
		LL d=(N/b)%10;
		if(d>0) Check((N/b)*b-1);
	}
}

int main(){
	int Test;
	cin>>Test;
	for(int i=1;i<=Test;i++){
		cin>>N;
		Solve();
		cout<<"Case #"<<i<<": "<<Ans<<"\n";
	}
}