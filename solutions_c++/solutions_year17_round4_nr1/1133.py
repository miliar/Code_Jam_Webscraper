#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define iinf 2000000000
#define linf 2000000000000000000LL
#define LL long long
#define MOD (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)

const string IMPOSSIBLE = "IMPOSSIBLE\n";
inline void case_print() {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": ";
	
	//cout << ans << "\n";
}

void MAIN() {
	int n , p;
	cin >> n >> p;
	vector<int> a(n + 2);
	
	for (int i = 1; i <= n; i ++) cin >>a[i];
	vector<int> mem[10];
	
	int answer = 0;
	for (int i = 1; i <= n; i ++) {
		mem[a[i] % p].push_back(a[i]);
	}
	vector<int> result;
	for (int i = 0; i < mem[0].size(); i ++){
		result.push_back(mem[0][i]);
		answer++;
	}
	mem[0].clear();
	
	for (int rem = 1; rem < p; rem ++) {
		while (rem != p-rem && mem[rem].size() > 0 && mem[p - rem].size() > 0) {
			result.push_back(mem[rem].back());
			result.push_back(mem[p-rem].back());
			mem[rem].pop_back();
			mem[p-rem].pop_back();
			answer++;
		}
		while (rem == p-rem && mem[rem].size() > 1) {
			result.push_back(mem[rem].back());
			result.push_back(mem[p-rem].back());
			mem[rem].pop_back();
			mem[p-rem].pop_back();
			answer++;
		}
	}
	
	//cerr << result.size() << endl;
	if (p <= 3) {
		while (mem[1].size() > 0) result.push_back(mem[1].back()), mem[1].pop_back();
		while (p == 3 && mem[2].size() > 0) result.push_back(mem[2].back()), mem[2].pop_back();
	}
	if (p == 4) {
		if (mem[2].size() > 0) {
			assert(mem[2].size() == 1);
			result.push_back(mem[2].back());
			mem[2].pop_back();
		}
		while (mem[1].size() > 0) result.push_back(mem[1].back()), mem[1].pop_back();
		while (mem[3].size() > 0) result.push_back(mem[3].back()), mem[3].pop_back();
	}
	assert(result.size() == n);
	answer =0;
	int tmp = 0;
	for (int i = 0; i < n; i ++) {
		if (tmp == 0) answer++;
		tmp += (result[i] % p);
		tmp %= p;
	}
	
	case_print();
	/*for (int i = 0; i + 1< n; i ++)
		cout << result[i] << " ";
	cout << result[n-1] << endl;
	*/
	cout << answer << endl;
}
int main() {
	ios_base::sync_with_stdio(0);
	freopen("A-large.in", "r",stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	while (T --> 0) {
		MAIN();
	}
	
	return 0;
}
