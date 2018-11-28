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

int A[24*60], B[24*60];
int dp[2][2][24*60][721];
int vis[2][2][24*60][721];
int tc;
int n, m;


int go(int f, int p, int t, int j) {
	if (j < 0) return inf;
	if (t == 24*60) {
		if (j == 0) return f != p;
		return inf;
	}
	int &ans = dp[f][p][t][j];
	if (vis[f][p][t][j] == tc) return ans;
	vis[f][p][t][j] = tc;
	ans = inf;
	if (not A[t]) {
		ans = min(ans, go(t==0?0:f, 0, t+1, j-1) + (t!=0)*(p==1));
	}
	if (not B[t]) {
		ans = min(ans, go(t==0?1:f, 1, t+1, j) + (t!=0)*(p==0));	
	}
	return ans;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);

	int t; cin >> t; while (t--) {
		cin >> n >> m;
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		FOR (i, 0, n - 1) {
			int x, y; cin >> x >> y;
			FOR (j, x, y-1) A[j] = 1;
		}
		FOR (i, 0, m - 1) {
			int x, y; cin >> x >> y;
			FOR (j, x, y-1) B[j] = 1;
		}
		++tc;
		cout << "Case #" << tc << ": " << go(0, 0, 0, 720) << "\n";
	}

	return 0;
}