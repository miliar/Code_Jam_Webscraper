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

const int N = 1000*1000 + 3;
int n, k;
set<pii> st;

void insert(int l, int pos) {
	if(l)
		st.insert(pii(-l, pos));
}

int main()
{
	ios_base::sync_with_stdio(false);

	int nt;
	cin >> nt;
	for(int ti=1; ti<=nt; ++ti) {
		cerr << ti << endl;
		cin >> n >> k;
		int l1, l2;
		st.clear();
		insert(n, 1);
		while(k--) {
			pii p = *st.begin();
			int l = -p.F, pos = p.S;
			st.erase(st.begin());
			l1 = (l - 1) / 2, l2 = l / 2;
			insert(l1, pos);
			insert(l2, pos+l1+1);
		}

		cout << "Case #" << ti << ": " << l2 << ' ' << l1 << endl;
	}

	return 0;
}





