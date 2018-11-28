#include <iostream>
#include <algorithm>
#include <utility>
#include <iomanip>

using namespace std;

bool cross(pair<int, int>, pair<int, int>, int d);

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for (int i_t = 0; i_t < t; i_t++) {
        int n;
        pair<int, char> c[6];
        cin >> n;
        for (int i = 0; i < 6; i++) {
            cin >> c[i].first;
        }
        c[0].second = 'R';
        c[1].second = 'O';
        c[2].second = 'Y';
        c[3].second = 'G';
        c[4].second = 'B';
        c[5].second = 'V';
        sort(c, c + 6, greater<pair<int, char>>());
        string res;
        if (c[0].first > c[1].first + c[2].first) {
            cout << "Case #" << i_t + 1  << ": IMPOSSIBLE\n";
            continue;
        }
        if ((c[1].first + c[2].first - c[0].first) % 2 == 1) {
            res.push_back(c[1].second);
            c[1].first--;
        }
        int diff = (c[1].first + c[2].first - c[0].first) / 2;
        for (int i = 0; i < c[0].first; i++) {
            res.push_back(c[0].second);
            if (c[0].first - i + diff > c[2].first) {
                res.push_back(c[1].second);
            } else {
                res.push_back(c[2].second);
            }
        }
        for (int i = 0; i < diff; i++) {
            res.push_back(c[1].second);
            res.push_back(c[2].second);
        }
        cout << "Case #" << i_t + 1  << ": "<< res << "\n";
    }
    return 0;
}
