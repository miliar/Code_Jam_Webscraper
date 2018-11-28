#include <iostream>
#include <algorithm>
using namespace std;

double K[1001];
double S[1001];
long double R[1001];

int main(){
	int zes;
	cin>>zes;
	for(int i = 1; i <= zes; i++){
		int D, N;
		cin>>D>>N;
		for(int i = 0; i < N; i++){
			cin>>K[i];
			cin>>S[i];
		}
		
		for(int i = 0; i < N; i++){
			R[i] = (D - K[i]) / S[i]; 
		}
		sort(R, R + N);
		cout<<"Case #"<<i<<": ";
		cout.precision(6); 
		cout<<fixed<<D/R[N-1]<<endl; 
	}
}
