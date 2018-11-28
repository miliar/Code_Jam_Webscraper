// {{{ $VIMCODER$ <-----------------------------------------------------
// vim:filetype=cpp:foldmethod=marker:foldmarker={{{,}}}

#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define range(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define rep_(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define range_(i, f, t) for (int i = (int)(t)-1; i >= (int)(f); --i)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define fst first
#define snd second

using namespace std;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }

typedef long long ll;
typedef pair<int, int> pii;

// }}}

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
        int R, C;
        cin >> R >> C;
        vector<string> cake;
        rep(r, R) {
            string row;
            cin >> row;
            char p = '?';
            rep(c, C) {
                if (p != '?' && row[c] == '?') row[c] = p;
                p = row[c];
            }
            rep_(c, C) {
                if (p != '?' && row[c] == '?') row[c] = p;
                p = row[c];
            }
            cake.push_back(row);
        }
        string p = "?";
        rep(r, R) {
            if (p[0] != '?' && cake[r][0] == '?') cake[r] = p;
            p = cake[r];
        }
        rep_(r, R) {
            if (p[0] != '?' && cake[r][0] == '?') cake[r] = p;
            p = cake[r];
        }
		cout << "Case #" << casenum << ": " << endl;
        rep(r, R) cout << cake[r] << endl;
	}
	return 0;
}
