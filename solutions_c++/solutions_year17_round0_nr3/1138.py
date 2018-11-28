#include <iostream>
using namespace std;

int T;
unsigned long long K, N;

int main(){
	cin>>T;
	for(int cs = 1; cs<=T; ++cs){
		unsigned long long lres, rres;
		cin>>N>>K;
		int t = 0;
		while (K > ((1ULL<<t)-1))
			++t;
		--t;
		unsigned long long piece = (1ULL << t) ;
		unsigned long long mod = (N - piece + 1) % piece;
		unsigned long long left = (N - piece + 1) / piece;
		K = K - piece + 1;
		if ( K <= mod)
			++left;
		--left;
		lres = rres = left >> 1;
		if (left & 1)
			++ rres;
		cout<<"Case #"<<cs<<": "<<rres<<' '<<lres<<endl;
	}

	return 0;
}
