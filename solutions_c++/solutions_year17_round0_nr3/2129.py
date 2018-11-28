#include <cstdio>
#include <map>
#include <algorithm>

using namespace std;

int cases; 
long long N, K;
map<long long, long long> mm;

typedef pair<long long, long long> PLL;

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		mm.clear();
		scanf("%lld%lld", &N, &K);
		mm[N] = 1;
		while(K > 0){
			PLL x = *(mm.rbegin());
			if(K <= x.second) {
				printf("Case #%d: %lld %lld\n", xx, x.first / 2, (x.first - 1) / 2);
				break;
			}
			K -= x.second;
			mm[(x.first - 1) / 2] += x.second;
			mm[x.first / 2] += x.second;
			mm.erase(x.first);
		}
	}
}
