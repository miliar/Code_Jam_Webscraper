#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>

 
using namespace std; 
 
typedef long long ll; 
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const long double PI = 3.14159265358979323846;  
//const long double eps = 1e-5;
//const int INF = 50000;
//const int N = 1000 * 1000 * 1000 + 10;


void solve() {
    int n, c, m;
    cin >> n >> c >> m;
    vector<int> ticByPos(n), ticByPers(c);
    for (int i = 0; i < m; ++i) {
        int p, b;
        cin >> p >> b;
        --p, --b;
        ++ticByPos[p], ++ticByPers[b];
    }
    int res = 0;
    for (int i = 0; i < c; ++i) {
        res = max(res, ticByPers[i]);
    }
    int sumT = 0;
    for (int i = 0; i < n; ++i) {
        sumT += ticByPos[i];
        res = max(res, (sumT + i) / (i + 1));
    }
    cout << res << " ";
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += max(0, ticByPos[i] - res);
    }
    cout << ans << endl;

    
}

int main() {
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
		std::cerr << i << endl;
	}
	return 0;
}