#include <iostream>
#include <vector>

using namespace std;
#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define FOR(i, a, b) for(int i = (a); i <= (b); i++)
#define RE(i, n) FOR(i,1,n)
#define REP(i, n) FOR(i,0,(int)(n)-1)
#define R(i, n) REP(i,n)
#define VI vector<int>
#define PII pair<int,int>
#define LD long double
#define FI first
#define SE second
#define st FI
#define nd SE
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define cerr if(0) cout

#include <cassert>

template<class C>
void mini(C &_a4, C _b4) { _a4 = min(_a4, _b4); }

template<class C>
void maxi(C &_a4, C _b4) { _a4 = max(_a4, _b4); }

//template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
//template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
//    while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
//}

template<class T>
ostream &operator<<(ostream &os, vector<T> V) {
    os << "[";
    for (auto &vv : V) os << vv << ",";
    os << "]";
    return os;
}

struct solution {
    int N, P;

    void solve_case(int case_num) {
        cin >> N >> P;
        VI counts(P, 0);

//        REP(p, P) cerr << p << ": " << counts[p] << endl;

        REP(n, N) {
            int g;
            cin >> g;
            counts[g % P]++;
        }

//        REP(p, P) cerr << p << ": " << counts[p] << endl;

        int result = 0;
        result += counts[0];
        counts[0] = 0;

//        REP(p, P) cerr << p << ": " << counts[p] << endl;

        if (P == 2) {
            if (counts[1] > 0)
                result += (counts[1] - 1) / 2 + 1;
        } else {
            int q = min(counts[1], counts[P - 1]);
            result += q;
            counts[1] -= q;
            counts[P - 1] -= q;

            assert(counts[1] == 0 or counts[P - 1] == 0);

            if (P == 4) {
                q = counts[2] / 2;
                counts[2] -= 2 * q;
                result += q;
            }

            cerr << "----: " << result << endl;
            REP(p, P) cerr << counts[p] << endl;

            if (P == 4 and counts[3] > 0) {
                if (counts[2] == 1) {
                    result += (counts[3] + 1) / 4 + 1;
                } else {
                    result += (counts[3] + 3) / 4;
                }
            } else if (P == 4 and counts[1] > 0) {
                if (counts[2] == 1) {
                    counts[1] += 2; // BAD IDEA!!!
                }
            }

            if (P > 2 && counts[2] > 0)
                result += (counts[2] - 1) / P + 1;

            if (P > 1 && counts[1] > 0)
                result += (counts[1] - 1) / P + 1;
        }

        cout << "Case #" << case_num << ": " << result << "\n";
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