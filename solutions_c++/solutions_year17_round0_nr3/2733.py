#include <iostream>
#include <map>

using namespace std;
typedef long long int Z;

int main() {
	int tc;
	cin >> tc;
	for(int t = 0; t < tc; ++t) {
		Z n, k;
		cin >> n >> k;
		
		map<Z, Z> counts;
		counts[n + 1] = 1;
		auto it = counts.begin();
		Z total = 0;
		Z v = -1;
		while(total < k) {
			v = it->first;
			counts[v/2] += it->second;
			counts[(v+1)/2] += it->second;
			total += it->second;
			--it;
		}
		
		cout << "Case #" << t + 1 << ": " << (v+1)/2 - 1 << " " << v/2 - 1 << '\n';
	}
	
	return 0;
}
