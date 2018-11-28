#include <cstdio>
#include <map>
#include <queue>

using namespace std;
typedef long long int Long;

int t;
Long ls, rs,
	 n, k, s, oc;
map<Long, Long> M;
priority_queue<Long> Q;

int main() {
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		M.clear();
		while(!Q.empty()) { Q.pop(); }
		
		scanf("%lld%lld", &n, &k);
		Q.push(n);
		M[n] = 1;
		
		while(!Q.empty() && k) {
			s = Q.top(); Q.pop();
		    oc = M[s];
		    M[s] = 0;
			
			ls = rs = (s>>1);
			if(!(s&1)) --ls;
			
			if(oc >= k) {
				break;
			}
			
			k -= oc;
			
			if(ls) {
				if(!M[ls]) Q.push(ls);
				M[ls] += oc;
			}
			if(!M[rs]) Q.push(rs);
			M[rs] += oc;
		}
		
		printf("Case #%d: %lld %lld\n", tc, rs, ls);
	}
	
	return 0;
}
