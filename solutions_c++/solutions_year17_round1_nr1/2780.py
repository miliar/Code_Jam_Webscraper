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
        int r, c;
        cin >> r >> c;
        vector<string> cake(r);
        vector<pair<int, int>> pos;
        vector<bool> exist(26, false);
        vector<int> starti(26, 10000);
        vector<int> startj(26, 10000);
        vector<int> endi(26, -1);
        vector<int> endj(26, -1);
        FOR(i, 0, r)
            cin >> cake[i];

        FOR(i, 0, r) {
            FOR(j, 0, c) {
                if (cake[i][j] == '?')
                    pos.push_back(make_pair(i, j));
                else {
                    int mojiidx = cake[i][j] - 'A';
                    exist[mojiidx] = true;
                    starti[mojiidx] = min(starti[mojiidx], i);
                    startj[mojiidx] = min(startj[mojiidx], j);
                    endi[mojiidx] = max(endi[mojiidx], i);
                    endj[mojiidx] = max(endj[mojiidx], j);
                }
            }
        }
        FOR(moji, 0, 26) {
            if (!exist[moji])
                continue;
            IFOR(i, starti[moji], endi[moji]) {
                IFOR(j, startj[moji], endj[moji])
                    cake[i][j] = moji + 'A';
            }
        }

        FOR(moji, 0, 26) {
            if (!exist[moji])
                continue;
            // left->top->right->bottom
            RFOR(l, startj[moji] - 1, 0) {
                bool ok = true;
                IFOR(i, starti[moji], endi[moji]) {
                    if (!(cake[i][l] == '?' || cake[i][l] == moji + 'A')) {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                    IFOR(i, starti[moji], endi[moji]) {
                    cake[i][l] = moji + 'A';
                    startj[moji] = l;
                }
                else
                    break;
            }

            FOR(R, endj[moji] + 1, c) {
                bool ok = true;
                IFOR(i, starti[moji], endi[moji]) {
                    if (!(cake[i][R] == '?' || cake[i][R] == moji + 'A')) {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                    IFOR(i, starti[moji], endi[moji]) {
                    cake[i][R] = moji + 'A';
                    endj[moji] = R;
                }
                else
                    break;
            }
        }
        FOR(moji, 0, 26) {
            if (!exist[moji])
                continue;
            RFOR(t, starti[moji] - 1, 0) {
                bool ok = true;
                IFOR(j, startj[moji], endj[moji]) {
                    if (!(cake[t][j] == '?' || cake[t][j] == moji + 'A')) {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                    IFOR(j, startj[moji], endj[moji]) {
                    cake[t][j] = moji + 'A';
                    starti[moji] = t;
                }
                else
                    break;
            }


            FOR(u, endi[moji] + 1, r) {
                bool ok = true;
                IFOR(j, startj[moji], endj[moji]) {
                    if (!(cake[u][j] == '?' || cake[u][j] == moji + 'A')) {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                    IFOR(j, startj[moji], endj[moji]) {
                    cake[u][j] = moji + 'A';
                    endi[moji] = u;
                }
                else
                    break;
            }

        }

        cout << endl;
        for (auto t : cake)
            cout << t << endl;

    }
    return 0;
}