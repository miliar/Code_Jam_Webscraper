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
        int N, M, C;
        cin >> N >> C >> M;
        vector<int> promotions(M+1);
        map<int, int> pcnts, scnts;
        rep(i, M) {
            int s, p;
            cin >> s >> p;
            pcnts[p]++;
            scnts[s]++;
        }
        int Mp = 0;
        for (auto p : pcnts) maxi(Mp, p.second);
        rep(i, Mp) promotions[i] = -1;
        int seated = 0;
        range(i, 1, N+1) {
            int toseat = scnts[i];
            seated += toseat;
            rep(j, M+1) if (promotions[j] >= 0) {
                if (seated <= j * i) {
                    promotions[j] += max(0, toseat - j);
                } else promotions[j] = -1;
            }
        }
        
        cout << "Case #" << casenum << ": ";
        rep(i, M+1) if (promotions[i] >= 0) {
            cout << i << ' ' << promotions[i] << endl;
            break;
        }
    }
    return 0;
}
