#include <bits/stdc++.h>

#define ll long long
#define __(x) cout << #x << " : " << x << endl;
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < n; i++)
#define N 1111

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

void print(int test, int ans) {
	cout << "Case #" << test << ": " << ans << endl;
	//printf("Case #%d: %d\n", test, ans);
}

void print(int test, string ans) {
	cout << "Case #" << test << ": " << ans << endl;
}

void gen() {
	freopen("input.txt", "w", stdout);
	
}

bool check(string ans, int n) {
	string t_ans = ans + ans[0];
	bool ok = true;
	for (int i = 1; i < n; i++) {
		if (t_ans[i] == t_ans[i - 1] || t_ans[i] == t_ans[i + 1]) {
			ok = false;
		}
	}
	return ok;
}

int main()
{
#ifdef INOUT
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		int n;
		cin >> n;
		int a, b, c, x, y, z;
		cin >> a >> z >> b >> x >> c >> y;
		if (a + b < c || b + c < a || c + a < b) {
			print(test, "IMPOSSIBLE");
			continue;
		}
//		if (x + y < c || x + z < b || z + y < a) {
//			print(test, "IMPOSSIBLE");
//		} else {
//			string ans = "";
//			int pos = 0;
//			while (pos < n) {
//				int len = ans.length();
//				if (a > 0 && (len == 0 || ans[len - 1] != 'R')) {
//					ans = ans + 'R';
//					a--;
//				} else {
//					if (b > 0 && (len == 0 || ans[len - 1] != 'Y')) {
//						ans = ans + 'Y';
//						b--;
//					} else {
//						if (c > 0 && (len == 0 || ans[len - 1] != 'B')) {
//							ans = ans + 'B';
//							c--;
//						} else {
//							break;
//						}
//					}
//				}
//				pos++;
//			}
//			while (pos < n) {
//				int len = ans.length();
//				for (int i = 0; i < len - 1; i++) {
//					if (a > 0 && ans[i] != 'R' && ans[i + 1] != 'R') {
//						ans = ans.substr(0, i + 1) + 'R' + ans.substr(i + 1, len - i - 1);
//						a--;
//						break;
//					} else {
//						if (b > 0 && ans[i] != 'Y' && ans[i + 1] != 'Y') {
//							ans = ans.substr(0, i + 1) + 'Y' + ans.substr(i + 1, len - i - 1);
//							b--;
//							break;
//						} else {
//							if (c > 0 && ans[i] != 'B' && ans[i + 1] != 'B') {
//								ans = ans.substr(0, i + 1) + 'B' + ans.substr(i + 1, len - i - 1);
//								c--;
//								break;
//							}
//						}
//					}
//				}
//				pos++;
//			}
			string ans = "";
			for (int i = 0; i < a; i++) {
				ans = ans + 'R';
			}
			for (int i = 0; i < b; i++) {
				ans = ans + 'Y';
			}
			for (int i = 0; i < c; i++) {
				ans = ans + 'B';
			}
			while (!check(ans, n)) {
				for (int i = 0; i < n - 1; i++) {
					if (ans[i] != ans[n - 1] && ans[i + 1] != ans[n - 1]) {
						ans = ans.substr(0, i + 1) + ans[n - 1] + ans.substr(i + 1, n - i - 2);
						break;
					}
				}
			}
			print(test, ans);
//		}
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}
