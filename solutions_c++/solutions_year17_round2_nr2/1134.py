#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
using namespace std;

int T;
int N, R, O, Y, G, B, V;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TC = 1; TC <= T; ++TC) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << TC << ": ";
        if (R > Y + B || Y > R + B || B > R + Y) {
            cout << "IMPOSSIBLE\n";
        } else {
            vector<pair<int, char> > VEC;
            VEC.emplace_back(R, 'R');
            VEC.emplace_back(B, 'B');
            VEC.emplace_back(Y, 'Y');
            sort(VEC.begin(), VEC.end());
            // Put all the large ones...
            list<char> LST;
            for (int a = 0; a < VEC.back().first; ++a) {
                LST.push_back(VEC.back().second);
                if (VEC[1].first) {
                    LST.push_back(VEC[1].second);
                    --VEC[1].first;
                }
                else {
                    LST.push_back(VEC[0].second);
                    --VEC[0].first;
                }
            }
            list<char>::iterator it, it2, it3;
            for (it = next(LST.begin()); it != LST.end(); ++it) {
                if (!VEC[0].first) break;
                it2 = prev(it);
                it3 = next(it);
                if (*it2 != VEC[0].second && *it3 != VEC[0].second) {
                    LST.insert(it, VEC[0].second);
                    --VEC[0].first;
                }
            }
            for (auto E: LST)
                cout << E;
            cout << "\n";
        }
    }
    return 0;
}
