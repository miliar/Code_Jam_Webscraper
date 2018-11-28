#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
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
#include<cassert>
#include<functional>




using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<char, char> pcc;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;

#define show(x) cerr << x
#define debug(x) show(#x << ": " << (x) << endl)

const long double PI = 3.14159265358979323846;
const long double gammama = 0.57721566490153286060;
const long double eps = 1e-5;
const int INF = 1000 * 1000 * 1000 + 1;
const ll LINF = (ll)1000 * 1000 * 1000 * 1000 * 1000 * 1000;
const ll mod = 1000 * 1000 * 1000 + 7;
const ll N = 1001;


void solve() {
    ll n, k;
    cin >> n >> k;
    map<ll, ll> mp;
    mp[n] = 1;
    ll m1 = 0, m2 = 0;

    while (k > 0) {
        pll v = *(mp.rbegin());
        m1 = v.first / 2, m2 = (v.first - 1) / 2;
        if (mp.find(m1) == mp.end())
            mp[m1] = 0;
        if (mp.find(m2) == mp.end())
            mp[m2] = 0;
        mp[m1] += v.second;
        mp[m2] += v.second;
        k -= v.second;
        mp.erase(v.first);
    }
    cout << m1 << " " << m2;
}


int main() {
    //freopen("C-small-2-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
		std::cerr << i << endl;
	}
	return 0;
}
