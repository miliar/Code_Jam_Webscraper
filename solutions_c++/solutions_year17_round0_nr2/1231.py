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

#define show(x) cerr << x
#define debug(x) show(#x << ": " << (x) << endl)

const long double PI = 3.14159265358979323846;
const long double gammama = 0.57721566490153286060;
const long double eps = 1e-5;
const int INF = 1000 * 1000 * 1000 + 1;
const ll LINF = (ll)1000 * 1000 * 1000 * 1000 * 1000 * 1000;
const ll mod = 1000 * 1000 * 1000 + 7;
const int N = 1000000;



void solve() {
    ll n;
    cin >> n;
    vector<int> a;
    while (n > 0) {
        a.push_back(n % 10);
        n /= 10;
    }
    reverse(a.begin(), a.end());
    int pos = -1;
    for (int i = 0; i + 1 < a.size(); ++i) {
        if (a[i + 1] < a[i]) {
            pos = i;
            while ((pos > 0) && (a[pos] == a[pos - 1]))
                --pos;
            a[pos] -= 1;
            for (int j = pos + 1; j < a.size(); ++j)
                a[j] = 9;
        }
    }
    pos = 0;
    while (a[pos] == 0)
        ++pos;
    for (int i = pos; i < a.size(); ++i)
        cout << a[i];
    
    
}


int main() {
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
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
