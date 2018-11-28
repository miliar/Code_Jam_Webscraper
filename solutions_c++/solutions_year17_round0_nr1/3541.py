#include<bits/stdc++.h>
#define int long long
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define INF (1ll<<60)
typedef pair<int, int> pii;
#define FI first
#define SE second
#define all(s) s.begin(),s.end()
#define RREP(i,n) for(int i=(n)-1;i>=0;--i)
#define pb push_back
#define mp make_pair
#define l_b lower_bound
#define u_b upper_bound

struct BIT {
	int N;int dat[2200];
	void init(int n) {
		N = n;
		memset(dat, 0, sizeof(dat));
	}
	//0indexed
	void add(int a, int x) {
		a++; //1indexed
		while (a <= N) {
			dat[a] += x;
			a += a & -a;
		}
	}
	//[0,a)
	int sum(int a) {
		a++; //[1,a)1indexed
		a--; //[1,a]
		int s = 0;
		while (a > 0) {
			s += dat[a];
			a -= a & -a;
		}
		return s;
	}
};
int K;
int L; //length
BIT bit;
int solve() {
	int res = 0;
	rep(i,L-K+1)
	{
		if (bit.sum(i + 1) % 2 == 0) {
			//happy
		} else {
			//black
			bit.add(i, 1);
			bit.add(i + K, -1);
			res++;
		}
	}
	for (int i = L - K + 1; i < L; ++i) {
		if (bit.sum(i + 1) % 2 == 1)
			return -1;
	}
	return res;
}
signed main() {
	int t;
	cin >> t;
	rep(i,t)
	{
		string s;
		cin >> s >> K;
		bit.init(s.length() + 2);
		L = s.length();
		rep(j,s.length())
		{
			if (s[j] == '-') {
				bit.add(j, 1);
				bit.add(j + 1, -1);
			}
		}
		int tmp = solve();
		if (tmp == -1)
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i + 1 << ": " << tmp << endl;
	}
}
