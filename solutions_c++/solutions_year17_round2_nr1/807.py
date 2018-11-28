#include <iostream>
using namespace std;
typedef long long ll;

ll T, D, N;
double maxTime;

void Process_horse(ll pos, ll speed){
	double time = (double(D-pos))/(double(speed));
	maxTime = maxTime > time ? maxTime : time;
}

int main(){
	cin>>T;
	cout << fixed;
	cout.precision(7);
	for(int i=1; i<=T; i++){
		cin>>D>>N;
		ll K, S;
		maxTime=0;
		for(int j=0; j<N; j++){
			cin>>K>>S;
			Process_horse(K,S);
		}
		cout<<"Case #"<<i<<": "<<double(D)/maxTime<<endl;
	}
}