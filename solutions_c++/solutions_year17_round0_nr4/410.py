#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

struct Change {
    char m;
    int r;
    int c;
};

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        int N, M;
        cin >> N >> M;
        vector<string> stage;
        forn(r, N) {
            string s(N, '.');
            stage.push_back(s);
        }
        forn(i, M) {
            char m;
            int r, c;
            cin >> m >> r >> c;
            stage[r-1][c-1] = m;
        }
        vector<string> stage_orig = stage;
        /* forn(r, N) { */
        /*     cout << stage[r] << endl; */
        /* } */
        /* cout << "*************************************************************************" << endl; */
        /* make sure there is an 'o' in first row */
        int ocol = -1;
        forn(c, N) {
            if (c == N-1 || stage[0][c] == 'x' || stage[0][c] == 'o') {
                stage[0][c] = 'o';
                ocol = c;
                break;
            }
        }

        /* set the rest to '+' */
        forn(c, N) {
            if (c != ocol) stage[0][c] = '+';
        }
        if (ocol == N-1) {
            for (int r = N-1, c = 0; r > 0; --r, ++c) {
                stage[r][c] = 'x';
            }
        } else {
            for (int r = 1, c = 0; r < N; ++r, ++c) {
                if (c == ocol) ++c;
                stage[r][c] = 'x';
            }
        }
        for (int c = 1; c < N-1; ++c) {
            stage[N-1][c] = '+';
        }

        /* checks */
        map<int, int> rdiags, ldiags;
        forn(r, N) {
            forn(c, N) {
                if (stage[r][c] != 'x' && stage[r][c] != '.') {
                    ++rdiags[r-c];
                    ++ldiags[r+c];
                }
            }
        }
        for (auto p : rdiags) if (p.second > 0) assert(p.second <= 1);
        for (auto p : ldiags) if (p.second > 0) assert(p.second <= 1);
        forn(r, N) {
            int cnt = 0;
            forn(c, N) if (stage[r][c] != '+' && stage[r][c] != '.') ++cnt;
            assert(cnt <= 1);
        }
        forn(c, N) {
            int cnt = 0;
            forn(r, N) if (stage[r][c] != '+' && stage[r][c] != '.') ++cnt;
            assert(cnt <= 1);
        }
        /* end checks */


        int score = 0;
        vector<Change> changes;
        forn(r, N) {
            forn(c, N) {
                switch (stage[r][c]) {
                    case 'o': ++score;
                    case 'x':
                    case '+':
                        ++score;
                    default:
                        break;
                }
                if (stage[r][c] != stage_orig[r][c]) {
                    changes.push_back(Change{stage[r][c], r+1, c+1});
                }
            }
        }

        /* forn(r, N) { */
        /*     cout << stage[r] << endl; */
        /* } */
        cout << "Case #" << casenum << ": " << score << ' ' << changes.size() << endl;
        for (Change c : changes) {
            cout << c.m << ' ' << c.r << ' ' << c.c << endl;
        }
    }
    return 0;
}

