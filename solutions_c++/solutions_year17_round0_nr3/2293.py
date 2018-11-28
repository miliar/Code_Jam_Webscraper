#include <iostream>
using namespace std;

long long T = 0, t = 0;
long long N, K;


int main(){
	//freopen("codejam03_in.txt", "r", stdin);
	//freopen("codejam03_out.txt", "w", stdout);
	cin>>T;
	while(t++ < T){
		cin>>N>>K;
		long long m = 1, n = 1;		
		while(m < K){
			n *= 2;
			m += n;
		}
		m -= n;
		long long k = (N-m)/n;
		if( (K-m) <= ( (N-m)%n))
			k++;
		long long minnum = (k-1)/2;
		long long maxnum = k/2;
		printf("Case #%lld: %lld %lld\n", t, maxnum, minnum);	
	}
	return 0;
}