#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
using namespace std;


struct Activity {
    int start;
    int end;
    int type;
};


bool isAllowed(const vector<int>& types, int type, int minute) {
    if (minute >= types.size()) return false;
    return types[minute] != type;
}


int calcMinSwitches(vector<Activity> activities) {
    const int dayLength = 24 * 60;
    const int INF = 1e8;
    vector<int> types(dayLength, -1);
    for (const auto& a : activities) {
        for (int i = a.start; i < a.end; ++i) types[i] = a.type;
    }
    vector<vector<vector<int>>> ms0(dayLength / 2 + 1, vector<vector<int>>(dayLength / 2 + 1, vector<int>(2, INF)));
    vector<vector<vector<int>>> ms1(dayLength / 2 + 1, vector<vector<int>>(dayLength / 2 + 1, vector<int>(2, INF)));
    ms0[0][0][0] = 0;
    ms1[0][0][1] = 0;
    for (int m0 = 0; m0 <= dayLength / 2; ++m0) {
        for (int m1 = 0; m1 <= dayLength / 2; ++m1) {
            for (int t = 0; t < 2; ++t) {
                if (ms0[m0][m1][t] != INF) {
                    for (int tn = 0; tn < 2; ++tn) {
                        if (isAllowed(types, tn, m0 + m1)) {
                            int _m0 = m0 + int(tn == 0);
                            int _m1 = m1 + int(tn == 1);
                            if (_m0 > dayLength / 2 || _m1 > dayLength / 2) continue;
                            int upd = ms0[m0][m1][t] + int(t != tn);
                            ms0[_m0][_m1][tn] = min(ms0[_m0][_m1][tn], upd);
                        }
                    }
                }
                if (ms1[m0][m1][t] != INF) {
                    for (int tn = 0; tn < 2; ++tn) {
                        if (isAllowed(types, tn, m0 + m1)) {
                            int _m0 = m0 + int(tn == 0);
                            int _m1 = m1 + int(tn == 1);
                            if (_m0 > dayLength / 2 || _m1 > dayLength / 2) continue;
                            int upd = ms1[m0][m1][t] + int(t != tn);
                            ms1[_m0][_m1][tn] = min(ms1[_m0][_m1][tn], upd);
                        }
                    }
                }
            }
        }
    }
    int m = dayLength / 2;
    int result = INF;
    result = min(result, ms0[m][m][0]);
    result = min(result, ms1[m][m][1]);
    result = min(result, ms0[m][m][1] + 1);
    result = min(result, ms1[m][m][0] + 1);
    return result;
}


int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    for (int tId = 0; tId < numTests; ++tId) {
        int nA, nB;
        cin >> nA >> nB;
        vector<Activity> activities(nA + nB);
        for (auto& a : activities) {
            cin >> a.start >> a.end;
            a.type = nA-- > 0;
        }
        cerr << tId << endl;
        cout << "Case #" << tId + 1 << ": " << calcMinSwitches(activities) << endl;
    }
    return 0;
}
