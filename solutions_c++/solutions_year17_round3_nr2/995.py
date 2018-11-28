#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <climits>
#include <cmath>

using namespace std;

struct task { int c, d, e; };

int elapse(int d, int c) {
    return (d - c + 1440) % 1440;
}

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int AC, AJ;
        cin >> AC >> AJ;
        vector<task> AT;
        for (int i = 0; i < AC; i++) {
            int c, d;
            cin >> c >> d;
            AT.push_back({c, d, 0});
        }
        for (int i = 0; i < AJ; i++) {
            int c, d;
            cin >> c >> d;
            AT.push_back({c, d, 1});
        }
        int AA = AC + AJ;
        int mincount;
        if (AA == 1) {
            mincount = 2;
        }
        else if (AT[0].e == AT[1].e) {
            if (elapse(AT[1].d, AT[0].c) > 720 && elapse(AT[0].d, AT[1].c) > 720) {
                mincount = 4;
            }
            else {
                mincount = 2;
            }
        }
        else {
            mincount = 2;
        }
        cout << "Case #" << testcase << ": ";
        cout << mincount << endl;
    }
    return 0;
}

// vim: sw=4:
