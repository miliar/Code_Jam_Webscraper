#include <bits/stdc++.h>
using namespace std;

constexpr double PI = 3.1415926535;

void solve(){
	int K,N;
	cin >> K >> N;	
	vector<long long> R(K),H(K);
	for(int i=0;i<K;i++){
		cin >> R[i] >> H[i];
	}


	double ans = 0;
	for(int i=0;i<K;i++){
		long long sur = R[i] * R[i];
		vector<long long> hh;
		for(int j=0;j<K;j++) if(i!=j){
			hh.push_back(2*R[j]*H[j]);
		}
		sort(hh.begin(),hh.end());
		reverse(hh.begin(),hh.end());
		for(int j=0;j<N-1;j++){
			sur += hh[j];
		}

		sur += 2*R[i]*H[i];
		ans = max(ans,sur*PI);
	}
	printf("%.20lf\n",ans);
}

int main(){
	int T;
	cin  >>  T;
	for(int i=1;i<=T;i++){
		printf("Case #%d: ",i);
		solve();
	}

}
