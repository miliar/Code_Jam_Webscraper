#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

int main(){
		
	int T;
	cin >> T;
	
	for(int t = 0; t < T; t++){
		long long N, K;
		
		cin >> N >> K;
		
		cout << "Case #" << t+1 << ": ";
		
		map<long long, long long, greater<long long> > M;
		
		M[N] = 1;
		
		long long num = 0;
		
		while(true){
		
			auto p = *M.begin();
			num += p.second;
			
			long long pos = (p.first - 1) / 2;
			
			//cout << p.first << " " << p.second << " " << pos << endl;
			//getchar();
			if (num >= K){
				long long L = pos;
				long long R = p.first - pos - 1;
				cout << max(L,R) << " " << min(L,R) << endl;
				break;
			}
			
			if (p.first % 2 == 1){
				M[pos];
				M[pos] += p.second * 2;
			} else {
				M[pos];
				M[pos] += p.second;
				M[pos+1] += p.second;
			}
			M.erase(p.first);
		}
		
	}
}