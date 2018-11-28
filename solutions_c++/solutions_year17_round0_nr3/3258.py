using namespace std;
#include <stdio.h>
#include <iostream>
long long int loga2(const long long int& K);
long long int expBin2(const long long int& K);
long long int techo(const long long int& K,const long long int& Q);
int main(){
	int T;
	long long int N,K;
	long long int nP,lP;
	scanf("%d",&T);
	for(int c1=0;c1<T;++c1){
		cin >> N >> K;
		if(K==1){
			cout << "Case #" << c1+1 << ": " << techo(N-1,2) << " " << (N-1)/2 << endl;
			continue;
		}
		nP=expBin2(loga2(K));
		lP=techo(N-K+1,nP);
		cout << "Case #" << c1+1 << ": " << techo(lP-1,2) << " " << (lP-1)/2 << endl;
	}
}
long long int loga2(const long long int& K){
	long long int A=K;
	int R;
	for(R=0;A!=1;++R)A=A/2;
	return R;
}
long long int expBin2(const long long int& K){
	if(K==0)return 1;
	if(K==1)return 2;
	long long int R=expBin2(K/2);
	if(K%2==0)return R*R;
	return R*R*2;
}
long long int techo(const long long int& K,const long long int& Q){
	if(K%Q==0)return K/Q;
	return (K/Q)+1;
}
