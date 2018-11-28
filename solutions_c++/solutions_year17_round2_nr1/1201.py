#include <bits/stdc++.h>

#define ll long long
#define __(x) cout << #x << " : " << x << endl;
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < n; i++)
#define N 1111
#define INF ( (ll) 2e18)

#define INOUT
#define TIME	

using namespace std;

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x)
{
	s << "(" << x.first << ", " << x.second << ")";
	return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &v)
{
	s << "[";
	bool was = false;
	for (auto it : v)
	{
		if (was) 
		{
			s << ", ";
		}
		was = true;
		s << it;
	}
	s << "]";
	return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x)
{
	s << "{";
	bool was = false;
	for (auto it : x)
	{
		if (was)
		{
			s << ", " << endl;
		}
		was = true;
		s << it;
	}
	s << "}";
	return s;
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const map<U, V> &m)
{
	s << "{";
	bool was = false;
	for (auto it : m)
	{
		if (was)
		{
			s << ", " << endl;
		}
		was = true;
		s << it.first << ": " << it.second;
	}
	s << "}";
	return s;
}

void print(int test, double ans) {
	printf("Case #%d: %.6f\n", test, ans);
//	cout << "Case #" << test << ": " << ans << endl;
	//printf("Case #%d: %d\n", test, ans);
}

void print(int test, string ans) {
	cout << "Case #" << test << ": " << ans << endl;
}

void gen() {
	freopen("input.txt", "w", stdout);
	
}

int main()
{
#ifdef INOUT
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		ll n;
		double d;
		cin >> d >> n;
		vector < pair <ll, ll> > a;
		a.resize(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].second >> a[i].first;
		}
		sort(a.begin(), a.end());
		double ans = INF;
		for (int i = 0; i < n; i++) {
			double t = (double) d * a[i].first / (d - a[i].second);
			ans = min(ans, t);
		}
		print(test, ans);
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
