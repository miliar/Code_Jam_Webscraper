#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<memory.h>
#include<ctime>
#include<cassert>
#include<limits.h>
#include<unordered_map>
#include<unordered_set>

#define pb push_back
#define sz(a) (int)a.size()
//#define bs binary_search
#define np next_permutation
#define mp make_pair
#define all(a) a.begin(),a.end()
#define forn(i, n) for (int i = 0; i < n; ++i)
#define forv(i, v) for (int i = 0; i < sz(v); ++i)
#define forab(i, a, b) for (int i = a; i <= b; i++)
#define forabd(i, a, b) for (int i = a; i >= b; i--)
#define _(a, b) memset(a, b, sizeof a)
#define pii pair<int, int>
#define pll pair<long long, long long>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

template<class T> inline T sqr(T x) { return x * x; }

const double pi = acos(-1.0), eps = 1e-9, e = exp(1.0);
const int INF = 1000 * 1000 * 1000 + 7, MAXN = 100005, MOD = 1000000007, MAXBIT = 30, pHash = 53;
const ll INFL = 1e+18;

void prepare(string s) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
#else
	if (sz(s) != 0) {
		freopen((s + ".in").c_str(), "r", stdin);
		//freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

bool operator < (pii a, pii b) {
	return a.first + a.second < b.first + b.second;
}
int T, k;
ll n;

void read() {
	
}

bool tidy(int n) {
	vector<int> a, b;
	while (n > 0) {
		int mod = n % 10;
		a.push_back(mod);
		b.push_back(mod);
		n /= 10;
	}
	reverse(all(a));
	sort(all(b));
	return a == b;
}

void solve() {
	cin >> T;
	forab(iter, 1, T) {
		cout << "Case #" << iter << ": ";

		cin >> n;
		if (n == 1LL * 111111111111111110) {
			cout << 1LL * 99999999999999999 << endl;
		} else {
			for (int i = n; i >= 1; i--) {
				if (tidy(i)) {
					cout << i << endl;
					break;
				}
			}
		}
	}
}

int main()
{
	prepare("");

	read();
	solve();

	return 0;
}