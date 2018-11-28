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

ll Hd, Hk, B, D;
const size_t HD = 0;
const size_t AD = 1;
const size_t HK = 2;
const size_t AK = 3;
const size_t BB = 4;
const size_t DD = 5;

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
        ll Ad, Ak;
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
        set<vector<ll>> states;
        set<vector<ll>> done;
        states.insert({Hd, Ad, Hk, Ak, B, D});
		cout << "Case #" << casenum << ": ";
        for (int i = 1;; ++i) {
            //cout << i << ',' << states.size() << endl;
            done.insert(all(states));
            set<vector<ll>> nstates;
            for (auto s:states) {
                if (s[HK] <= s[AD]) {
                    cout << i << endl;
                    goto next;
                }
                // Attack
                vector<ll> t = s;
                t[HK] -= t[AD];
                t[HD] -= t[AK];
                t[BB] = 0;
                t[DD] = 0;
                if (t[HD] > 0 && !done.count(t)) nstates.insert(t);

                // Buff
                t = s;
                if (t[BB]) {
                    t[AD] += B;
                    t[HD] -= t[AK];
                    if (t[HD] > 0 && !done.count(t)) nstates.insert(t);
                }

                // Cure
                t = s;
                if (t[HD] < Hd - t[AK]) {
                    t[HD] = Hd;
                    t[HD] -= t[AK];
                    if (t[HD] > 0 && !done.count(t)) nstates.insert(t);
                }

                // Debuff
                t = s;
                if (t[DD]) {
                    t[AK] -= D;
                    t[HD] -= t[AK];
                    if (t[HD] > 0 && !done.count(t)) nstates.insert(t);
                }
            }

            if (nstates.size() == 0) {
                cout << "IMPOSSIBLE" << endl;
                break;
            }
            states = nstates;
        }
next:;
	}
	return 0;
}
