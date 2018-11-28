#include <iostream>
#include <map>
using namespace std;

int N, K, t, x = 1;
bool used[1003];

pair<int, int> solve() {
    int begin = -1, end = -1;
    pair<int, int> max_ = make_pair(-1, -1), tmp, ret;

    while (K--) {
        begin = end = -1;
        max_ = make_pair(-1, -1);

        for (int i = 0; i < N + 2; ++i) {
            if (begin == -1 && used[i] == true) {
                begin = i;
            }
            else if (begin != -1 && end == -1 && used[i] == true) {
                end = i - 1;
                tmp = make_pair(begin, end);
            
                if (tmp.second - tmp.first > max_.second - max_.first) {
                    max_ = tmp;
                    //cout << begin << " & " << end << endl;                
                }
                begin = i;
                end = -1;
            }
        }

        int p = max_.second - max_.first;
        //cout << p << endl;
        //cout << max_.second << " " << max_.first << endl;
        if (p % 2) {
            used[p / 2 + max_.first + 1] = true;
            ret.first = ret.second = p / 2;
        }
        else {
            used[p / 2 + max_.first] = true;
            ret.first = p / 2;
            ret.second = p / 2 - 1;
        }
        
    }

    return ret;
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> t;

    while (t--) {
        cin >> N >> K;

        used[0] = used[N + 1] = true;
        fill(used + 1, used + 1 + N, false);
        /*
        for (int i = 0; i < N + 2; ++i) cout << used[i] << " ";
        cout << endl;
        */

        pair<int, int> ans = solve();

        cout << "Case #" << x << ": " << ans.first << " " << ans.second << "\n";
        x++;
    }

    return 0;
}