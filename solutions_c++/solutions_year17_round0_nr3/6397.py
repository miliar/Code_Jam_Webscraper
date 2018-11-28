#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())
#define	endl			'\n'

typedef long long		ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>		vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>		vpii;

const int MX = 25;

int main(int argc, char *argv[])
{
#ifdef	HTRINH_UNIT_TEST
	freopen(argv[1],"r",stdin);
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;
	FOR(testcase,1,T+1) {
		int N,K;
		cin >> N >> K;
		if (N == 1) {
			cout << "Case #" << testcase << ": 0 0\n";
			continue;
		}
		set<pii> S;
		S.insert(pii(-N,1));
		int y, z;
		while (K--) {
			pii top = *(S.begin());
			int D = -top.first;
			int i = top.second;
			S.erase(S.begin());

			int d1,d2,idx1,idx2;
			int d = D/2;
			if (D & 1) {
				d1 = d;
				idx1 = i;
				d2 = d;
				idx2 = i+d1+1;
			} else {
				d1 = d-1;
				idx1 = i;
				d2 = d;
				idx2 = i+d1+1;
			}
			y = d2;
			z = d1;
			if (d1) S.insert(pii(-d1,idx1));
			if (d2) S.insert(pii(-d2,idx2));
		}
		cout << "Case #" << testcase << ": " << y << " " << z << endl;
	}
	return 0;
}
