#include <iostream>
#include <algorithm>

#define X first
#define Y second


using namespace std;

typedef pair<long long, long long> point;

point f(long long k, long long n) {
	// cerr << k <<" : " << n << endl;
	if (k == 1) {
		return make_pair((n)/2, (n-1)/2);
	} else {
		if (n % 2)
			return f((k)/2, (n-1)/2);
		else if (k % 2)
			return f(k/2, (n-1)/2);
		else
			return f(k/2, n/2);
	}
}


int main(){
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		long long k, n;
		cin >> n >> k;
		cout << "Case #" << test+1 <<": ";
		point result = f(k, n);
		cout << result.X << " " << result.Y << endl;
	}
}