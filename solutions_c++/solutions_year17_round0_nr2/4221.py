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
int n;

int main()
{
	ios_base::sync_with_stdio(false);

	int nt;
	cin >> nt;
	for(int ti=1; ti<=nt; ++ti) {
		string s;
		cin >> s;
		int n = s.size();
		cout << "Case #" << ti << ": ";

		int ind = 1;
		while(ind<n && s[ind-1] <= s[ind])
			++ind;
		if(ind==n)
			cout << s << endl;
		else {
			--ind;
			int j = ind-1;
			while(j>=0 && s[ind]==s[j])
				--j;
			for(int i=0; i<=j; ++i)
				cout << s[i];
			if(s[ind] != '1')
				cout << (s[ind]-'0')-1;
			for(int i=j+2; i<n; ++i)
				cout << 9;
			cout << endl;
		}
	}

	return 0;
}





