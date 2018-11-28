#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <iomanip>
#include <math.h>
#include <deque>
#include <time.h>
#include <queue>
#include <vector>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <bitset>
#include <cassert>
#include <set>
#include <array>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <random>
#include <complex>


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
//typedef unsigned ll us;
#define mp make_pair
#define runtime clock() * 1.0 / CLOCKS_PER_SEC
#define STOP system("pause")
//#define all(x) (x).begin(), (x).end()
#define all(x) begin(x), end(x)


ll const mod7 = ll(1e9 + 7);
ll const mod9 = ll(1e9 + 9);
ll const mod = 1503991337;
ll const INFll = 2e18;
ld const INFld = 28e14;
ll const INF = ll(2e9);
ld const eps = 1e-6;
ld const pi = acos(-1.0);
int const E3 = 1003;
int const E4 = 10004;
int const E5 = 100005;
int const E6 = 1000006;
int const E7 = 10000007;


ll sqr(ll x) {
	return x*x;
}


using namespace std;


#define TASK "coins"
struct __debug__ {

	__debug__(string filename) {
		ios_base::sync_with_stdio(0);
		//cin.tie(0);
		string filein = filename + ".in";
		string fileout = filename + ".out";
		assert(sizeof(int) == 4);
#ifdef _DEBUG
		//gen();
		freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
		//freopen(filein.c_str(), "r", stdin); freopen(fileout.c_str(), "w", stdout);
		//freopen(TASK".in", "r", stdin);freopen(TASK".out", "w", stdout);
		//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	}
	~__debug__() {
#ifdef _DEBUG
		//cout << "\n\nTIME: " << runtime;
#endif
	}

} __Debug__("decomposition");


void solve(int TestNumber);


int32_t main() {
	int t = 1;
	cin >> t;
	srand(random_device()());
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve(i);
		cout << '\n';
		cerr << i << endl;
	}
}


bool eq(ld a, ld b) {
	return abs(a - b) < eps;
}


ld p[100];
int n, k;
ld a;


bool f(ld x) {
	ld sum = 0;
	for (int i = 0; i < n; i++) {
		if (p[i] < x) {
			sum += x - p[i];
		}
	}
	return sum <= a;
}


void solve(int Test) {
	cin >> n >> k;
	cin >> a;
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}
	ld l = 0;
	ld r = 1;
	int kek = 228;
	while (kek--) {
		ld m = (l + r) / 2;
		if (f(m)) {
			l = m;
		}
		else {
			r = m;
		}
	}
	ld lol = 1;
	for (int i = 0; i < n; i++) {
		lol *= max(p[i], r);
	}
	cout << fixed << setprecision(9) << lol;
}