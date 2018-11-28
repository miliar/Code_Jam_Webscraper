#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int T, N, M, K, D, S;

int main(){
	cin>>T;
	for(int cs=1; cs<=T; ++cs){
		double res=0;
		cin>>D>>N;
		for (int i = 0; i< N; ++i){
			cin>>K>>S;
			res = max(res, (double)(D - K)/ S);
		}
		res = D / res;
		printf("Case #%d: %.6f\n", cs, res);
		// cout<<"Case #"<<cs<<": "<<res<<endl;
	}
	return 0;
}
