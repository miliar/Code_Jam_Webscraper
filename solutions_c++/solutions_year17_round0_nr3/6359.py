
#include <iostream>

#include <stdio.h>
#include <string.h>

using namespace std;

long log2(long n){
	long number = n;
	long log = 0;
	while (number >>= 1) log++;
	return log;
}

void bathroom(long N, long K){
	long level = log2(K);
	long Kr = K - (1 << level); // K = 2^level + Kr

	// Before the people with same level, there are still Nr remaining stalls
	// Nr = N + 1 - 2^level
	long Nr = N + 1 - (1 << level);

	// There are 2^level banks of stalls available
	// There sizes are either Nr/2^level or Nr/2^level+1
	// There are P oversized banks

	long minSize = Nr / (1 << level);
	long P;
	if(minSize!=0) P = Nr - minSize*(1 << level);
	else P = Nr;
	long bank;

	if(Kr < P) bank = minSize + 1;
	else bank = minSize;

	//printf("%ld %ld %ld %ld %ld\n", level, K, Kr, N, Nr);

	//printf("%ld %ld %ld\n", minSize, P, bank);

	printf("%ld %ld\n", bank/2, (bank-1)/2);
	
}

int main() {
	long t, k, n;
	cin >> t;

	for (long i = 1; i <= t; i++){
		cin >> n >> k;
		printf("Case #%ld: ", i);
		bathroom(n,k);
	}

	return 0;
}