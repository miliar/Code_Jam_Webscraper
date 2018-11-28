#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <utility>
struct triplet {
	long long int l;
	long long int r;
	long long int count;

};
using namespace std;
int main(int argc, char const *argv[]) {
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		long long int N = 0, K = 0, p = 0;
		triplet sol = {0, 0, 1};
		scanf("%lld %lld", &N, &K);
		map<pair<long long int, long long int>, long long int> m;
		if(N%2 == 1) {
			m[make_pair(N/2, N/2)] = 1;
		}
		else {
			m[make_pair((N - 1)/2, (N + 1)/2)] = 1;
		}

		while(!m.empty()) {

			map<pair<long long int, long long int>, long long int>::reverse_iterator it = m.rbegin();
			long long int _l = it->first.first, _r = it->first.second, _count = it->second;
			if((K > p) && (K <= p + _count)) {
				sol = {max(_l, _r), min(_l, _r), _count};
			}
			p = p + _count;
			m.erase(it->first);
			
			// printf("size: %lld, l: %lld, r: %lld, count: %lld p: %lld\n", m.size(), _l, _r, _count, p);
			if(_l == 0 && _r == 0) {
				continue;
			}
			N = max(_l, _r);
			if(N%2 == 0) {
				pair<long long int, long long int> temp_pair = make_pair((N + 1)/2, (N - 1)/2);
				if(m.find(temp_pair) != m.end()) {
					m[temp_pair] += _count;
				} else {
					m[temp_pair] = _count;
				}
				
			} else {
				pair<long long int, long long int> temp_pair = make_pair((N)/2, (N)/2);
				if(m.find(temp_pair) != m.end()) {
					m[temp_pair] += _count;
				} else {
					m[temp_pair] = _count;
				}
			}
			N = min(_l, _r);
			if(N%2 == 0) {
				pair<long long int, long long int> temp_pair = make_pair((N + 1)/2, (N - 1)/2);
				if(m.find(temp_pair) != m.end()) {
					m[temp_pair] += _count;
				} else {
					m[temp_pair] = _count;
				}
				
			} else {
				pair<long long int, long long int> temp_pair = make_pair((N)/2, (N)/2);
				if(m.find(temp_pair) != m.end()) {
					m[temp_pair] += _count;
				} else {
					m[temp_pair] = _count;
				}
			}

			
		}
		printf("Case #%d: %lld %lld\n", (t + 1), max(sol.l, sol.r), min(sol.l, sol.r));	
	}
	return 0;
}