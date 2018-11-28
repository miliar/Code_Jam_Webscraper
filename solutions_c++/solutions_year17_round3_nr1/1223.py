#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define INF 1e9
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define __(x) cout << #x << " : " << x << endl;
#define y1 laksjhaasg
#define y2 alsfkhgmnsd
#define md 1000000007

using namespace std;

#define INOUT

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair <U, V> &a) {
	s << "(" << a.first << ", " << a.second << ")";
	return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &a) {
	s << "{";
	bool was = false;
	for (auto it: a) {
		if (was) {
			s << ", ";
		}
		s << it;
		was = true;
	}
	s << "}";
	return s;
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const map<U, V> &a) {
	s << "{";
	bool was = false;
	for (auto it: a) {
		if (was) {
			s << ", ";
		}
		s << it.first << ": " << it.second;
		was = true;
	}
	s << "}";
	return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &a) {
	s << "[";
	bool was = false;
	for (auto it: a) {
		if (was) {
			s << ", ";
		}
		s << it;
		was = true;
	}
	s << "]";
	return s;
}

#define PI ()(long double) 3.141592653589793)

void print_case(int test) {
	cout << "Case #" << test << ": ";
}

bool cmp(pair <int, long double> a, pair <int, long double> b) {
	return a.second < b.second;
}

vector < pair < ll, ll> > a;

int main()
{
#ifdef INOUT
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, k;
		cin >> n >> k;
		a.resize(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].first >> a[i].second;
		}
		ll ans = 0;
		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());
		for (int i = 0; i < n - k + 1; i++) {
			ll s = a[i].first * a[i].first + 2 * a[i].first * a[i].second;
			vector < ll > heights;
			for (int j = i + 1; j < n; j++) {
				heights.pb(2 * a[j].first * a[j].second);
			}
			sort(heights.begin(), heights.end());
			reverse(heights.begin(), heights.end());
			for (int j = 0; j < k - 1; j++) {
				s += heights[j];
			}
			ans = max(ans, s);
		}
		print_case(test);
		printf("%.7Lf\n", (long double) M_PI * ans);
	}
	
	cerr << endl << (double) clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
