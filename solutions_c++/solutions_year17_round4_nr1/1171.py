#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <complex>
#include <exception>
#include <initializer_list>
#include <locale>
#include <tuple>
#include <typeinfo>
#include <type_traits>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
const int MAX_N = 100, MAX_P = 4;
int n_test, n, p, a[MAX_N + 1], cnt[MAX_P + 1], f[MAX_N + 1][MAX_N + 1][MAX_N + 1][MAX_P + 1], ans;

int Dp(int cnt1, int cnt2, int cnt3, int md) {
	if(cnt1 == 0 && cnt2 == 0 && cnt3 == 0) {
		return 0;
	}
	if(f[cnt1][cnt2][cnt3][md] != -1) {
		return f[cnt1][cnt2][cnt3][md];
	}
	f[cnt1][cnt2][cnt3][md] = 0;
	if(cnt1 > 0) {
		f[cnt1][cnt2][cnt3][md] = max(f[cnt1][cnt2][cnt3][md], Dp(cnt1 - 1, cnt2, cnt3, (md + 1) % p));
	}
	if(cnt2 > 0) {
		f[cnt1][cnt2][cnt3][md] = max(f[cnt1][cnt2][cnt3][md], Dp(cnt1, cnt2 - 1, cnt3, (md + 2) % p));
	}
	if(cnt3 > 0) {
		f[cnt1][cnt2][cnt3][md] = max(f[cnt1][cnt2][cnt3][md], Dp(cnt1, cnt2, cnt3 - 1, (md + 3) % p));
	}
	if(md == 0) {
		f[cnt1][cnt2][cnt3][md]++;
	}
	return f[cnt1][cnt2][cnt3][md];
}

int main() {
    ifstream cin("a.inp");
    ofstream cout("a.out");
    std::cin.rdbuf(cin.rdbuf());
    std::cout.rdbuf(cout.rdbuf());
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n_test;
    for(int i_test = 1; i_test <= n_test; i_test++) {
    	cin >> n >> p;
    	for(int i = 1; i <= n; i++) {
    		cin >> a[i];
    	}
    	fill(cnt, cnt + MAX_P + 1, 0);
    	fill(f[0][0][0], f[n + 1][0][0], -1);
    	for(int i = 1; i <= n; i++) {
    		cnt[a[i] % p]++;
    	}
    	ans = cnt[0] + Dp(cnt[1], cnt[2], cnt[3], 0);
    	cout << "Case #" << i_test << ": " << ans << "\n";
    }
    return 0;
}
