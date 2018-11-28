#include <iostream>
#include <map>
using namespace std;

typedef unsigned long long tint;

map<tint,tint> m;

int main() {
	int T, t;
	tint N, K, curl, curn, left, right;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N >> K;
		
		m.clear(); m[N] = 1;
		while (m.rbegin()->second < K) {
			curl = m.rbegin()->first;
			curn = m.rbegin()->second;
			m.erase(curl);
			left = (curl-1ULL)/2ULL;
			right = curl-1ULL-left;
			m[left] += curn;
			m[right] += curn;
			K -= curn;
		}
		curl = m.rbegin()->first;
		left = (curl-1ULL)/2ULL;
		right = curl-1ULL-left;
		cout << "Case #" << t << ": " << max(left,right) << " " << min(left,right) << endl;
	}

	return 0;
}
