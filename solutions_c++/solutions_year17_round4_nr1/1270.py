#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define NFOR(i,a,b) for(int i = (a); i >= (b); --i)
#define all(x) (x).begin(), (x).end()
#define sz(x) int(x.size())
typedef long long ll; typedef pair <int, int> ii; typedef vector <int> vi; const int inf = 1e9 + 7;
#define pr(...) dbs(#__VA_ARGS__, __VA_ARGS__)
template <class T> void dbs(string str, T t) {cout << str << " : " << t << endl;}
template <class T, class... S> void dbs(string str, T t, S... s) {int idx = str.find(','); cout << str.substr(0, idx) << " : " << t << ","; dbs(str.substr(idx + 1), s...);}
template <class S, class T>ostream& operator <<(ostream& os, const pair<S, T>& p) {return os << "(" << p.first << ", " << p.second << ")";}
template <class T>ostream& operator <<(ostream& os, const vector<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T>ostream& operator <<(ostream& os, const set<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class S, class T>ostream& operator <<(ostream& os, const map<S, T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T> void prc(T a, T b) {cout << "["; for (T i = a; i != b; ++i) {if (i != a) cout << ", "; cout << *i;} cout << "]";cout<<endl;}

int g[101];
int a[4], ac[4];
int dp[2000000], pw[4];
int vis[2000000];
int tc, n, p;
inline int getHash(int a[]) {
	int ans = 0;
	FOR (i, 1, p-1) ans += a[i] * pw[i];
	return ans;
}
inline bool fresh(int a[]) {
	int x = 0;
	FOR (i, 1, p-1) x += a[i] * i;
	return x % p == 0;
}
int f(int a[]) {
	int h = getHash(a);
	int &ans = dp[h];
	if (vis[h] == tc) return ans;
	vis[h] = tc;
	ans = 0;
	bool can = fresh(a);
	FOR (i, 1, p-1) if (a[i] < ac[i]){
		a[i]++;
		ans = max(ans, can + f(a));
		a[i]--;
	}
	return ans;
}
int main()
{
	pw[1] = 1;
	pw[2] = pw[1]*101;
	pw[3] = pw[2]*101;
	ios::sync_with_stdio(0); cin.tie(0);

	int _t; cin >> _t; for (tc = 1; tc <= _t; ++tc) {
		cin >> n >> p;
		FOR (i, 0, n-1) cin >> g[i];
		memset(a, 0, sizeof a);
		memset(ac, 0, sizeof ac);
		FOR (i, 0, n - 1) {
			ac[g[i]%p]++;
		}
		cout << "Case #" << tc << ": " << ac[0] + f(a) << "\n";
	}

	return 0;
}