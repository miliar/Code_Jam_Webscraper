#include <iostream>
#include <map>
#include <vector>
#include <cstdlib>

int T;
long long N, K;
std::vector<long long> len;
std::vector<long long> val;
std::map<long long,long long> nxt;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	std::cin >> T;
	for(int tc=1; tc<=T; tc++) {
		std::cin >> N >> K;
		nxt = std::map<long long,long long>();
		nxt[-N] = 1;
		long long ans = -1;
		if(K > N) K = N; 
		while(K > 0) {
			//std::cout << "=========" << nxt.size() << std::endl;
			len = std::vector<long long>();
			val = std::vector<long long>();
			for(std::map<long long,long long>::iterator it=nxt.begin(); it!=nxt.end(); ++it) {
				K -= it->second;
				//std::cout << -it->first << ": " << it->second << std::endl;
				if(K <= 0) {
					ans = -it->first;
					break;
				}
				len.push_back(-it->first);
				val.push_back(it->second);
			}
			if(ans != -1) break;
			int ni = (int)len.size();
			nxt = std::map<long long,long long>();
			for(int i=0; i<ni; i++) {
				nxt[-len[i]/2] += val[i];
				nxt[-(len[i]-1)/2] += val[i];
			}
			//system("pause");
		}
		std::cout << "Case #" << tc << ": " << ans/2 << " " << (ans-1)/2 << std::endl;
	}
	return 0;
}
