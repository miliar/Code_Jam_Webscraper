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

bool not_empty(vector<priority_queue<int>> &qs) {
    for (auto q : qs) if (q.empty()) return false;
    return true;
}

pair<int, int> miniMax(int r, int q) {
    int M = q/r;
    int m = M + 1;
    while (m * r * 110 >= q * 100) --m;
    while (M * r * 90 <= q * 100) ++M;
    return {m+1, M-1};
}

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
        int N, P;
        cin >> N >> P;
        vector<int> rs(N);
        rep(i, N) cin >> rs[i];
        vector<priority_queue<int>> qs(N);
        rep(i, N) {
            rep(j, P) {
                int a; cin >> a;
                int m, M;
                tie(m, M) = miniMax(rs[i], a);
                //cout << i << ": " << m << ", " << M << endl;
                if (m <= M) qs[i].push(-a);
            }
        }
        int cnt = 0;
        while (not_empty(qs)) {
            int m = 0, M = INT_MAX, mMi = -1;
            rep(i, N) {
                int a = -qs[i].top();
                int m_, M_; tie(m_, M_) = miniMax(rs[i], a);
                //cout << i << ": " << m_ << ", " << M_ << endl;
                maxi(m, m_);
                if (M_ < M) {
                    M = M_;
                    mMi = i;
                }
            }
            if (M == 0) {
                break;
            } else if (M >= m) {
                ++cnt;
                rep(i, N) qs[i].pop();
            } else {
                qs[mMi].pop();
            }
        }
		cout << "Case #" << casenum << ": " << cnt << endl;
	}
	return 0;
}
