#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <cstdio>
#include <stack>
#include <list>
#include <cstring>
#include <fstream>
#include <limits>
#include <iomanip>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define REP(i,e) for (int i = 0; i < int(e); ++i)
#define MAX(a,b) ((a) > (b) ? (a):(b))
#define MIN(a,b) ((a) < (b) ? (a):(b))
#define SQR(a) ((a)*(a))

const char probname = 'C';
const bool largeset = false;
const char* suffix = "-1-attempt0";// "-practice";

int main() {
    char buffer[1234];
    sprintf(buffer, "../data/%c-%s%s.in", probname, largeset ? "large" : "small", suffix);
    ifstream fin(buffer);
    sprintf(buffer, "../data/%c-%s%s.out", probname, largeset ? "large" : "small", suffix);
    ofstream fout(buffer);

    int testCases;
    fin >> testCases;


    int n, k;
    REP(testCase, testCases) {
        fin >> n >> k;

        long double u;
        fin >> u;

        vector<long double> probs(n);
        REP(i, n) fin >> probs[i];

        long double p = 0.5;
        long double low = 0;
        long double up  = 1;

        while (true) {
            double sum = 0;
            for (int i = 0; i < probs.size(); ++i) {
                sum += max<long double>(0.0, p - probs[i]);
            }
            if (fabs(sum - u) < 1e-9) break;

            if (sum < u) {
                low = p;
            } else {
                up  = p;
            }
            p = (low + up)/2;
        }

        long double res = 1;
        REP(i, probs.size()) {
            if (probs[i] < p) res *= p;
            else res *= probs[i];
        }

        fout << "Case #" << testCase + 1 << ": " << std::fixed << std::setprecision(15) << res << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
