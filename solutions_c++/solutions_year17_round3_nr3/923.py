#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int N,K;
		double U;
		double prob[51];
		cin>>N>>K;
		prob[N]=1;
		cin>>U;
		for(int n=0;n<N;n++){
			cin>>prob[n];
		}
		sort(&prob[0], &prob[N]);
		for(int i=1;i<K+1;i++){
			if(i*(prob[i]-prob[i-1])<U){
				U-=i*(prob[i]-prob[i-1]);
				for(int j=0;j<i;j++){
					prob[j]=prob[i];
				}
			}
			else{
				for(int j=0;j<i;j++){
					prob[j]+=U/i;
				}
				break;
			}
		}
		double ans=1;
		for(int i=0;i<K;i++){
			ans*=prob[i];
		}
		if(ans>=1) ans=0.999999999;
		cout.precision(9);
		cout<<"Case #"<<t<<": "<<fixed<<ans<<endl;
	}
	return 0;
}
