#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
vector<int>topush;
void recur(int N, int D, int K, int& Kleft){
	int minus = pow(2,D);
	if(minus >= K){
		Kleft = K;
		topush.push_back(N);
		return;
	} 
	if(N%2==0){
		recur(N/2, D+1, K-minus, Kleft);
		recur(N/2-1, D+1, K-minus, Kleft);
	}
	else{
		recur(N/2, D+1, K-minus, Kleft);
		recur(N/2, D+1, K-minus, Kleft);
	}
}
int main(){
	int tcase = 0;
	int N, K, D=0,left=0,right=0, Kleft = 0, Nfinal = 0;
	cin>>tcase;
	for(int i = 0; i < tcase; ++i){
		cin>>N;
		cin>>K;
		D=0;
	/*	if(K > N/2){
			cout<<"Case #"<<i+1<<": "<<0<<" "<<0<<endl;
			continue;
		}*/
		recur(N, D, K, Kleft);
		sort(topush.begin(), topush.end());
		reverse(topush.begin(), topush.end());
		Nfinal = topush[Kleft-1];
		if(Nfinal%2==0){
			cout<<"Case #"<<i+1<<": "<<Nfinal/2<<" "<<Nfinal/2-1<<endl;
		}
		else{
			cout<<"Case #"<<i+1<<": "<<Nfinal/2<<" "<<Nfinal/2<<endl;
		}
		topush.clear();
		
	}
	return 0;
}
