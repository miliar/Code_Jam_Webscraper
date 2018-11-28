#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

long long biggest_tidy(long long N) {
	vector <long long> V;
	while (N > 0) {
		V.push_back( N%10 );
		N /= 10;
	}
	
	reverse(V.begin(), V.end());
	
	long long prefix = 0;
	long long last = 0;
	
	int i = 0;
	
	while (i < V.size() && V[i] >= last) {
		last = V[i];
		prefix = prefix * 10 + V[i];
		
		i++;
	}
	
	if (i == V.size()) return prefix;
 	
	prefix -= 1;
	while (i<V.size()) {
		prefix = prefix * 10 +9;
		i++;
	}
 	
 	
	return prefix;
}

long long biggest_tity_checked(long long N) {
	long long res = 0;
	long long P = 1;
	while (N > 0) {
		N = biggest_tidy(N);
		res += P * (N%10);
		P *= 10;
		N/=10;
	}
	
	
	return res;
}

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		long long N;
		cin >> N;
				
		cout<<"Case #"<<test<<": " << biggest_tity_checked(N) << "\n";
	}
	return 0;
}
