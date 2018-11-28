#include<iostream>
#include<iomanip>
using namespace std;
double K[1001],S[1001],D;
double T[1001];
int N;

double max(){
	double max=0.0000000;
	for(int i=0;i<N;i++){
		if(max < T[i])
			max=T[i];
	}
	return max;
}

int main(){
	int t;
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>D>>N;
		for(int j=0;j<N;j++){
			cin>>K[j]>>S[j];
			T[j] = (double) (( D - K[j]) / S[j] );
		//	cout<<T[j]<<endl;
		}
		cout<<"Case #"<<i<<": ";
		cout<<fixed<<setprecision(10)<<(double)(D/max())<<endl;
	}
}