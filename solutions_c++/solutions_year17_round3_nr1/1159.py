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

const char probname = 'A';
const bool largeset = true;
const char* suffix = "";// "-practice";

int main() {
    char buffer[1234];
    sprintf(buffer, "../data/%c-%s%s.in", probname, largeset ? "large" : "small", suffix);
    ifstream fin(buffer);
    sprintf(buffer, "../data/%c-%s%s.out", probname, largeset ? "large" : "small", suffix);
    ofstream fout(buffer);

    int testCases;
    fin >> testCases;


    REP(testCase, testCases) {
        int n, k;
        fin >> n >> k;

        vector < pair <double, double > > p(n);

        REP(i, n) {
            fin >> p[i].first >> p[i].second;
        }

        vector < pair < double, double > > s(n);
        REP(i, n) {
            s[i].first  = p[i].first*p[i].second;
            s[i].second = i;
        }

        sort(s.begin(), s.end(), greater < pair<double, int> >());

        double res = -numeric_limits<double>::infinity();
        REP(i, n) {
            int cnt = 1;
            double r1 = p[i].first;
            double area = r1*r1 + 2*r1*p[i].second;

            REP(j, s.size()) {
                if (cnt == k) break;
                if (s[j].second != i && p[s[j].second].first < r1 + 1e-9) {
                    area += 2*s[j].first;
                    cnt++;
                }
            }

            if (cnt == k) {
                res = max(res, area);
            }
        }

        fout << "Case #" << testCase + 1 << ": " << std::fixed << std::setprecision(15) << M_PI*res << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
