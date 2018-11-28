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


//ll mod = 1000000009;




void solve() {
    int n, p;
    cin >> n >> p;
    vector<int> a(n);
    vector<int> c(p);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        ++c[a[i] % p];
    }
    int res = c[0];
    if (p == 2) {
        res += (c[1] + 1) / 2;
    }
    else {
        if (p == 3) {
            res += min(c[1], c[2]);
            int x = c[1] + c[2] - 2 * min(c[1], c[2]);
            res += (x + 2) / 3;
        }
        else {
            res += min(c[1], c[3]);
            int x = c[1] + c[3] - 2 * min(c[1], c[3]);
            int y = x / 2 + c[2];
            int r = x & 1;
            res += (y / 2);
            if ((r) || (y & 1))
                ++res;
        }
    }
    cout << res << endl;
   
    
}

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
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