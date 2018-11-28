#include <vector>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

void main2(){
	long long N,K;
	cin>>N>>K;
	long long i=0;
	for(;1<<(i+1)<K+1;i++);
	cerr << K <<' ' << i <<' ';
	N-=(1<<i)-1;
	K-=(1<<i)-1;
	cerr << N << ' ' << K << ' ';
	long long G=N/(1<<i);
	cerr << G << ' ';
	if(N%(1<<i) >= K) G++;
	cerr << G << ' ';
	long long L, R;
	if(G%2){
		L=G/2;
		R=G/2;
	}else{
		L=G/2;
		R=G/2-1;
	}
	cout<<L<<' '<<R;
}

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		main2();
		cout<<endl;
	}
}
