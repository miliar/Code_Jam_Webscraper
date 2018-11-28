#include <bits/stdc++.h>

using namespace std;

int main(){

	long long TC, N,K,NC = 1;
	cin>>TC;
	while(TC--){
		cin>>N>>K;
		long long L, R;
		map<long long,long long> m1;
		m1[N] = 1;
		int maxSize = 0;
		for(long long i = 1 ; i<=K ;){
			map<long long,long long>::iterator it = m1.end();
			it--;
			long long distance = it->first;
			long long acum = it->second;
			m1.erase(distance);
			
			if(distance%2 == 0){
				L = distance/2;
				R = L + 1;
				L--;
				R--;
				m1[L]+=acum;
				m1[R]+=acum;
			}else{
				L = distance/2;
				R = L;	
				m1[L]+=acum;
				m1[R]+=acum;
			}
			i+=acum;
		}
		cout<<"Case #"<<NC++<<": "<<max(L,R)<<" "<<min(L,R)<<endl;	
	}
	return 0;	
}
