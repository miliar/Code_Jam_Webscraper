#include <fstream>
#include <map>
#include <utility>
#include <functional>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

int main() {
	ifstream f("input.txt");
	ofstream g("output.txt");
	int t;
	f >> t;
	for(int i = 1; i <= t; i++) {
		ull n, k;
		f >> n >> k;
		map<ull, ull> cnt;
		cnt[n] = 1;
		ull ans1, ans2;
		while(k > 0) {
			map<ull, ull>::iterator it = cnt.end();
			it--;
			ull seq = it->first;
			ull seqCnt = it->second;
			ull v1 = (seq - 1) / 2;
			ull v2 = seq / 2;
			ans1 = v2;
			ans2 = v1;
			ull toBeErased = min(it->second, k);
			k -= toBeErased;
			it->second -= toBeErased;
			if(it->second == 0) {
				cnt.erase(it);
			}
			cnt[v1] += toBeErased;
			cnt[v2] += toBeErased;
		}
		g << "Case #" << i << ": " << ans1 << " " << ans2 << '\n';
	}
	f.close();
	g.close();
	return 0;
}
