#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <iomanip>
#include <unordered_map>
#include <string>
#define INF 1000000000
#define HAND_TYPE 1
#define TEST 10
#define SMALL 100
#define LARGE 1000
#define INPUT_SITUATION LARGE
#define MAKE_OUTFILE
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,N,P,ans,res;
int g;
int counts[4];
unordered_map<int, int> dp;
int max_count(int k) {
	if (k == 0)
		return 0;
	if (dp.count(k))
		return dp[k];
	int x = 0, y;
	for (int i=0; i<P; ++i) {
		if (((k>>(8*i))&255) == 0) continue;
		y = max_count(k - (1<<(8*i)));
		if (y > x)
			x = y;
	}
	int ct = 0;
	for (int i=0; i<P; ++i) {
		ct += i*((k>>(8*i))&255);
	}
	ct %= P;
	if (ct == res) {
		dp[k] = x+1;
		return x+1;
	} else {
		dp[k] = x;
		return x;
	}
}
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("A-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("A-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		dp.clear();
		cin >> N >> P;
		for (int i=0; i<4; ++i) {
			counts[i] = 0;
		}
		for (int i=0; i<N; ++i) {
			cin >> g;
			counts[g%P]++;
		}
		res = 0;
		for (int i=0; i<P; ++i)
			res += i*counts[i];
		res %= P;
		cout << "Case #" << cas+1 << ": " << max_count(counts[0]+(counts[1]<<8)+(counts[2]<<16)+(counts[3]<<24)) << '\n';
	}
	return 0;
}
