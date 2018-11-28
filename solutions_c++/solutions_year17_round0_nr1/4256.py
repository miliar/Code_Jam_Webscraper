#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define F first
#define S second
#define X real()
#define Y imag()
#define all(X) (X).begin(),(X).end()
#define MP make_pair

template<class P, class Q> inline bool mmin(P &a, Q b) { if (a > b){ a = b; return true;} return false;}
template<class P, class Q> inline bool mmax(P &a, Q b) { if (a < b){ a = b; return true;} return false;}

typedef long long LL;
typedef pair<int, int> pii;
typedef complex<double> point;

const int N = 100*1000 + 3;
int ar[N];
int n;

int main()
{
	ios_base::sync_with_stdio(false);

	int nt;
	cin >> nt;
	for(int ti=1; ti<=nt; ++ti) {
		int ans = 0, sum = 0;
		bool ok = true;
		string s;
		int n, k;
		cin >> s >> k;
		n = s.size();
		fill_n(ar, n+5, 0);
		for(int i=0; i<n; ++i) {
			int x = s[i]=='+';
			sum ^= ar[i];
			x ^= sum;
			if(!x) {
				if(i+k <= n) {
					++ans;
					sum ^= 1;
					ar[i+k] = 1;
				}
				else
					ok = false;
			}		}

		cout << "Case #" << ti << ": ";
		if(!ok)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;

	}

	return 0;
}





