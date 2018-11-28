#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;

long long find(long long N, long long K){
	if(K == 1) return N;
	else if(K%2 == 0){
		return find(N >> 1, K >> 1);
	}
	else{
		return find((N - 1) >> 1, (K-1) >> 1);
	}
}


int main(int argc, char *argv[]){
	int T = 0;
	cin >> T;
	for(int I = 1; I <= T; I++){
		long long n = 0, k = 0;
		cin >> n >> k;
		long long result = find(n, k);
		cout << "Case #" << I << ": " << (result >> 1) << " " << ((result - 1) >> 1) << endl;
	
	}
	return 0;
}