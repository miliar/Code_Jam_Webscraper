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

void print_case(int test) {
	cout << "Case #" << test << ": ";
}

pair <int, int> a[111], b[111];

int main()
{
#ifdef INOUT
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> a[i].first >> a[i].second;
		}
		sort(a, a + n);
		for (int i = 0; i < k; i++) {
			cin >> b[i].first >> b[i].second;
		}
		sort(b, b + k);
		print_case(test);
		if (n + k == 1) {
			cout << 2 << endl;
		} else {
			if (n == 1 && k == 1) {
				cout << 2 << endl;
			} else if (n == 2) {
				if (a[1].second - a[0].first > 720 && a[0].second + 1440 - a[1].first > 720) {
					cout << 4 << endl;
				} else {
					cout << 2 << endl;
				}
			} else {
				if (b[1].second - b[0].first > 720 && b[0].second + 1440 - b[1].first > 720) {
					cout << 4 << endl;
				} else {
					cout << 2 << endl;
				}
			}
		}
	}
	
	cerr << endl << (double) clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
