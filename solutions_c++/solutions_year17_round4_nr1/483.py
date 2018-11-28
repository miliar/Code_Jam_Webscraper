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
        int N, P;
        cin >> N >> P;
        vector<int> Gs(P);
        rep(i, N) {
            int g;
            cin >> g;
            Gs[g%P]++;
        }
        int cnt = Gs[0];
        if (P == 2) cnt += (Gs[1] + 1) /2;
        else if (P == 3) {
            int m = min(Gs[1], Gs[2]); 
            cnt += m;
            Gs[1] -= m;
            Gs[2] -= m;
            cnt += (Gs[1] + 2) / 3;
            cnt += (Gs[2] + 2) / 3;
        } else if (P == 4) {
            int m = min(Gs[1], Gs[3]); 
            cnt += m;
            Gs[1] -= m;
            Gs[3] -= m;
            m = Gs[2]/2;
            cnt += m;
            Gs[2] -= 2*m;
            if (Gs[2]) {
                if (Gs[1] >= 2) {
                    ++cnt;
                    Gs[1] -= 2;
                } else if (Gs[3] >= 2) {
                    ++cnt;
                    Gs[3] -= 2;
                } else {
                    ++cnt;
                    Gs[1] = 0;
                    Gs[3] = 0;
                }
            }
            cnt += (Gs[1] + 3) / 4;
            cnt += (Gs[3] + 3) / 4;
        } else {
            assert(0);
        }
        cout << "Case #" << casenum << ": " << cnt << endl;
    }
    return 0;
}
