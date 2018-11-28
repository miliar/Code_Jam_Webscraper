#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

pair <long long, long long> func(long long n) {
	if(n % 2 == 1) return {n / 2, n / 2};
	else return {(n / 2) - 1, n / 2}; 
}

struct cmp {
	bool operator()(long long a, long long b) {
		return func(a) > func(b);
	}
};

int main() {
	ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for(int it = 1; it <= tt; ++it) {
		map <long long, long long, cmp> A;
		long long n, k;
		cin >> n >> k;
		
		A[n] = 1;
		k--;
		while(k > 0) {
			long long m = (*A.begin()).first;
			long long ile = min(A[m], k);
			A[m] -= ile;
			k -= ile;
			if(A[m] == 0) A.erase(A.begin());
			if(func(m).first > 0) A[func(m).first] += ile;
			if(func(m).second > 0) A[func(m).second] += ile;
		}
		long long m = (*A.begin()).first;
		cout << "Case #" << it << ": " << func(m).second << ' ' << func(m).first << '\n';
	}
	return 0;
}
