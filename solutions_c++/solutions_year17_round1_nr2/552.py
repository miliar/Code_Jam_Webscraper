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
const int MAXN = 50, MAXM = 50, MAXLH = 2000000;
int n_test, n, m, a[MAXN + 9], b[MAXN + 9][MAXM + 9], ans, low[MAXN + 9][MAXM + 9], high[MAXN + 9][MAXM + 9];
bool used[MAXN + 9][MAXM + 9];

bool Intersect(int l, int h, int ll, int hh) {
	return max(l, ll) <= min(h, hh);
}

bool Dfs(int x, int y, int l, int h) {
	if(used[x][y]) {
		return false;
	}
	used[x][y] = true;
	if(x == n) {
		return l <= h;
	}
	for(int j = 1; j <= m; j++) {
		if(Intersect(l, h, low[x + 1][j], high[x + 1][j]) && Dfs(x + 1, j, max(l, low[x + 1][j]), min(h, high[x + 1][j]))) {
			return true;
		}
	}
	return false;
}

int main() {
    //ifstream cin("b.inp");
    //ofstream cout("b.out");
    std::cin.rdbuf(cin.rdbuf());
    std::cout.rdbuf(cout.rdbuf());
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n_test;
    for(int i_test = 1; i_test <= n_test; i_test++) {
    	cin >> n >> m;
    	for(int i = 1; i <= n; i++) {
    		cin >> a[i];
    	}
    	for(int i = 1; i <= n; i++) {
    		for(int j = 1; j <= m; j++) {
    			cin >> b[i][j];
    		}
    		sort(b[i] + 1, b[i] + m + 1);
    		for(int j = 1; j <= m; j++) {
    			low[i][j] = (b[i][j] * 10 + a[i] * 11 - 1) / (a[i] * 11);
    			high[i][j] = (b[i][j] * 10) / (a[i] * 9);
    		}
    	}
    	fill(used[0], used[n + 1], false);
    	ans = 0;
    	for(int j = 1; j <= m; j++) {
    		if(Dfs(1, j, low[1][j], high[1][j])) {
    			ans++;
    		}
    	}
    	cout << "Case #" << i_test << ": " << ans << "\n";
    }
    return 0;
}
