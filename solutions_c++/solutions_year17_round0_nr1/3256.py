#include <iostream>
#include <string>
#include <queue>
#include <tuple>

using namespace std;

int main() {
    int T, k;
    string S;
    cin >> T;

    for (int n = 1; n <= T; n++) {
        cin >> S >> k;
        queue<tuple<int, int, string> > q;
        q.push(make_tuple(0, -1, S));
        bool possible = false;
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            int depth = get<0>(p);
            int index = get<1>(p);
            string s = get<2>(p);
            bool done = true;
            for (int i = 0; i < s.length(); i++) {
                if (s[i] == '-') {
                    done = false;
                    break;
                }
            }

            if (done) {
                cout << "Case #" << n << ": " << depth << endl;
                possible = true;
                break;
            }

            for (int i = index + 1; i <= s.length() - k; i++) {
                string stmp = s;
                for (int j = i; j < i + k; j++) {
                    stmp[j] = stmp[j] == '-' ? '+' : '-';
                }
                q.push(make_tuple(depth + 1, i, stmp));
            }
        }

        if (!possible) {
            cout << "Case #" << n << ": IMPOSSIBLE" << endl;
        }
    }
}
