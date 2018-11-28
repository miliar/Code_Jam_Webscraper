#include <iostream>
#include <vector>
#include <limits>
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

//#define cerr cout
#define cerr if(0)cout

#define max_servings(recipe, quant) ((10*(quant)) / (9*(recipe)))
#define min_servings(recipe, quant) ((10*(quant)) / (11*(recipe)) + ((10*(quant)) % (11*(recipe)) > 0))

struct solution {
    int N, P;
    VI grams;
    vector<VI> pkg;
    void solve_case(int case_num) {
        cin >> N >> P;
        int g;
        REP(i, N) {
            cin >> g;
            grams.push_back(g);
            pkg.push_back(VI());
        }

        cerr << "HERE" << endl;

        int MAX_SERVINGS = 0;
        REP(n, N) {
            pkg[n] = VI(P);
            REP(p, P) {
                cin >> g;
                pkg[n][p] = g;
            }
            sort(ALL(pkg[n]), std::greater<int>());
            MAX_SERVINGS = max(MAX_SERVINGS, max_servings(grams[n], pkg[n][0]));
        }

        cerr << "P2" << endl;

        vector<VI> push;
        vector<VI> pop;
        VI current;
        VI pops_ignore;

        REP(n, N) {
            pop.push_back(VI((unsigned long) (MAX_SERVINGS + 1), 0));
            push.push_back(VI((unsigned long) (MAX_SERVINGS + 1), 0));
            current.push_back(0);
            pops_ignore.push_back(0);
            REP(p, P) {
                int quant = pkg[n][p];
                int min = min_servings(grams[n], quant);
                int max = max_servings(grams[n], quant);

                push[n][max] += 1;
                pop[n][min-1] += 1;
            }
        }

        cerr << "P3" << endl;

        int res = 0;

        for (int s = MAX_SERVINGS; s > 0; --s) {
            int min_available = std::numeric_limits<int>::max();
            REP(n, N) {
                int pops = pop[n][s];
                if (pops_ignore[n] > pops) {
                    pops_ignore[n] -= pops;
                    pops = 0;
                } else {
                    pops -= pops_ignore[n];
                    pops_ignore[n] = 0;
                }
                current[n] += push[n][s];
                current[n] -= pops;

                min_available = min(min_available, current[n]);
//                pops[n] -=
            }

            res += min_available;

            REP(n, N) {
                current[n] -= min_available;
                pops_ignore[n] += min_available;
            }
        }

        cout << "Case #" << case_num << ": " << res << "\n";
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