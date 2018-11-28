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
int n, r, o, y, g, b, v;
pair<int, char> ar[3];

int main()
{
	ios_base::sync_with_stdio(false);

	int nt;
	cin >> nt;
	for(int ti=1; ti<=nt; ++ti) {

		cin >> n >> r >> o >> y >> g >> b >> v;
//		cin >> r >> y >> b;

		cout << "Case #" << ti << ": ";

		ar[0] = make_pair(r, 'R');
		ar[1] = make_pair(y, 'Y');
		ar[2] = make_pair(b, 'B');

		sort(ar, ar+3);

		if(2*ar[2].F > r+y+b) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		while(ar[2].F) {
			--ar[2].F;
			cout << ar[2].S;
			if(ar[0].F < ar[1].F)
				swap(ar[0], ar[1]);
			--ar[0].F;
			cout << ar[0].S;
		}
		while(ar[1].F){
			--ar[1].F;
			cout << ar[1].S;
			swap(ar[1], ar[0]);
		}
		cout << endl;
	}

	return 0;
}





