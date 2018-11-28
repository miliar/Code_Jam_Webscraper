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
int T;

void read() {
	
}

void solve() {
	cin >> T;
	forab(iter, 1, T) {
		cout << "Case #" << iter << ": ";

		int n, k, cnt = 1;
		priority_queue<pii> q;
		vector<pii> v;
		cin >> n >> k;
		pii p = mp(n / 2, n / 2);
		if (!(n & 1)) {
			p.first--;
		}
		q.push(p);
		v.push_back(p);
		while (cnt < n) {
			int l = q.top().first,
				r = q.top().second;
			q.pop();

			if (l > 0) {
				p = mp(l / 2, l / 2);
				if (!(l & 1)) {
					p.first--;
				}
				q.push(p);
				cnt++;
				v.push_back(p);
			}
			
			if (r > 0) {
				p = mp(r / 2, r / 2);
				if (!(r & 1)) {
					p.first--;
				}
				q.push(p);
				cnt++;
				v.push_back(p);
			}
		}

		sort(all(v));
		reverse(all(v));

		p = v[k-1];
		cout << max(p.first, p.second) << ' ' << min(p.first, p.second) << endl;
	}
}

int main()
{
	prepare("");

	read();
	solve();

	return 0;
}