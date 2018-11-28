#include <iostream>
#include <vector>
using namespace std;
#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define RE(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(int)(n)-1)
#define R(i,n) REP(i,n)
#define VI vector<int>
#define PII pair<int,int>
#define LD long double
#define FI first
#define SE second
#define st FI
#define nd SE
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())

template<class C> void mini(C& _a4, C _b4) { _a4 = min(_a4, _b4); }
template<class C> void maxi(C& _a4, C _b4) { _a4 = max(_a4, _b4); }

//template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
//template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
//    while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
//}

template<class T> ostream& operator<<(ostream& os, vector<T> V) {
    os << "["; for (auto& vv : V) os << vv << ","; os << "]";
    return os;
}

struct solution {
    int C, R;
    vector<vector<char>> b;

    void solve_case(int case_num) {
        cin >> R >> C;
        char ch, last;

        int blank_rows = 0;
        bool initial_empty = true;
        REP(r, R) {
            b.push_back(vector<char>());
            last = '?';
            int blank_cols = 0;

            REP(c, C) {
                cin >> ch;
                if (ch == '?') {
                    if (last == '?') blank_cols++;
                    ch = last;
                }
                last = ch;
                b[r].push_back(ch);
            }

            bool empty_row = last == '?';
            if (!empty_row) {
                initial_empty = false;
                REP(c, blank_cols) b[r][c] = b[r][blank_cols];
            }
            if (initial_empty) {
                blank_rows++;
            } else if (empty_row) {
                b[r] = b[r-1];
            }
        }

        cout << "Case #" << case_num << ": \n";
        REP(r, blank_rows) {
            REP(c, C) {
                cout << b[blank_rows][c];
            }
            cout << endl;
        }
        FOR(r, blank_rows, R-1) {
            REP(c, C) {
                cout << b[r][c];
            }
            cout << "\n";
        }
    }
};

int32_t main() {
    int t;
    cin >> t;
    RE(case_num, t) {
        solution s;
        s.solve_case(case_num);
    }
    return 0;
}