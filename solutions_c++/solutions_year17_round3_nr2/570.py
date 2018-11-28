#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;

template<class T>
void printcontainer(T& con) {
    bool first = true;
    for (auto &t : con) {
        if (first)
            first = false;
        else
            cout << " ";
        cout << t;
    }
    cout << endl;
}
int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        int ac, aj;
        cin >> ac >> aj;
        vector<pair<int, int>> c(ac), j(aj);
        FOR(i, 0, ac) {
            cin >> c[i].first >> c[i].second;
        }
        FOR(i, 0, aj) {
            cin >> j[i].first >> j[i].second;
        }
        vector<pair< pair<int, int>, int>> tasks(ac + aj);
        FOR(i, 0, ac) {
            tasks[i] = make_pair(c[i], 0);
        }
        FOR(i, 0, aj) {
            tasks[i + ac] = make_pair(j[i], 1);
        }
        sort(tasks.begin(), tasks.end());
        int n = ac + aj;
        int cnt = 0;
        vector<int> cbridge, jbridge;
        int crest = 720, jrest = 720;
        FOR(i, 0, n) {
            int kukan = tasks[i].first.second - tasks[i].first.first;

            int name = tasks[i].second;
            int name2 = tasks[(i + 1) % n].second;
            if (name == 0)
                crest -= kukan;
            else
                jrest -= kukan;
            int diff = tasks[(i + 1) % n].first.first - tasks[i].first.second;
            diff = (diff + 1440) % 1440;
            if (name != name2)
                cnt++;
            else {
                if (name == 0)
                    cbridge.push_back(diff);
                else
                    jbridge.push_back(diff);
            }
        }
        sort(cbridge.begin(), cbridge.end());
        sort(jbridge.begin(), jbridge.end());


        int i, jj;

        for (i = 0; i < cbridge.size(); i++) {
            if (crest < cbridge[i])
                break;
            crest -= cbridge[i];
        }
        for (jj = 0; jj < jbridge.size(); jj++) {
            if (jrest < jbridge[jj])
                break;
            jrest -= jbridge[jj];
        }
        cout << 2*(cbridge.size() - i + jbridge.size() - jj) + cnt << endl;


    }
    return 0;
}