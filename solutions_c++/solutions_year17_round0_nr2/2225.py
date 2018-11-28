#include <iostream>
#include <cstring>
using namespace std;

long long T = 0, t = 0;
long long N;

long long solve(long long NN){
	long long D = 1, n = NN, t = 1, last = 10, res = 0;
	while(n){
		if( (n%10) > last){
			t = D;
		}
		last = n%10;
		D *= 10;
		n /= 10;
	}

	if(t == 1) return NN;
	res = solve( NN/t-1 );
	while(t!=1){
		res = res*10 + 9;
		t /= 10;
	}
	return res;
}

int main(){
	//freopen("codejam02_in.txt", "r", stdin);
	//freopen("codejam02_out.txt", "w", stdout);
	cin>>T;
//	T = 3;
	while(t++ < T){
		cin>>N;
		// N = 123;
		// printf("%lld\n", N);
		printf("Case #%lld: %lld\n", t, solve(N));	
	}
	return 0;
}