#include<bits/stdc++.h>
#include<assert.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
const int N = 1007;
int n, R, O, Y, G, B, V;
string gao(string a, string b, int n) {
	stringstream ss;
	ss << a;
	rep(i, 0, n)
		ss << b << a;
	return ss.str();
}
vector<string> gen(int a, int b, string A, string B) {
	vector<string> ret;
	if (b)
		ret.push_back(gao(A, B, b));
	rep(i, b > 0, a - b)
		ret.push_back(A + "");
	return ret;
}
vector<string> merge(const vector<string> &a, const vector<string> &b) {
	vector<string> c;
	int i = 0, j = 0;
	while (i < sz(a) || j < sz(b)) {
		if (i < sz(a))
			c.push_back(a[i++]);
		if (j < sz(b))
			c.push_back(b[j++]);
	}
//	cout << "c: ";rep(i, 0, sz(c)) cout << c[i];cout << endl;
	return c;
}
vector<string> solve() {
	vector<string> ret;
	if (O + B == n) {
		if (O != B)
			return ret;
		rep(i, 0, B)
			ret.push_back("B"), ret.push_back("O");
		return ret;
	}
	if (G + R == n) {
		if (G != R)
			return ret;
		rep(i, 0, R)
			ret.push_back("R"), ret.push_back("G");
		return ret;
	}
	if (V + Y == n) {
		if (V != Y)
			return ret;
		rep(i, 0, Y)
			ret.push_back("Y"), ret.push_back("V");
		return ret;
	}
	if ((O && O >= B) || (G && G >= R) || (V && V >= Y))
		return ret;				
	vector<string> vec[3];	
	vec[0] = gen(B, O, "B", "O"); 
	vec[1] = gen(R, G, "R", "G");
	vec[2] = gen(Y, V, "Y", "V");	
	int id[3];
	rep(i, 0, 3) id[i] = i;
	rep(i, 0, 3)
		rep(j, i + 1, 3)
			if (sz(vec[id[i]]) > sz(vec[id[j]]))
				swap(id[i], id[j]);
//	rep(k, 0, 3) rep(i, 0, sz(vec[id[k]])) cout << vec[id[k]][i];cout << endl;
	if (sz(vec[id[0]]) + sz(vec[id[1]]) < sz(vec[id[2]]))
		return ret;
	ret = merge(vec[id[2]], vec[id[1]]);
	reverse(ret.begin(), ret.end());
	ret = merge(vec[id[0]], ret);
	return ret;
}
int main() {
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
		vector<string> ans = solve();			
		cout << "Case #" << cas + 1 << ": ";
		if (sz(ans) > 0) {
			int len = 0;
			rep(i, 0, sz(ans)) {
				cout << ans[i];
				len += ans[i].length();
			}
			assert(len == n);
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
