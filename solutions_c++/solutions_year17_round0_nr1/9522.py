#include <iostream>
#include <map>
#include <queue>

using namespace std;

int solve(const string &start, int num) {
    map<string, int> len;
    len[start] = 0;
    queue <string> q;
    q.push(start);
    while (!q.empty()) {
        string cur = q.front();
        q.pop();
        if (cur.find('-') == string::npos) {
            return len[cur];
        }
        for (int i = 0; i <= start.size() - num; ++i) {
            string next(cur);
            for (int k = i; k < num + i; ++k) {
                next[k] = next[k] == '-' ? '+' : '-';
            }
//            cout << cur << " : " << next << endl;
            if (len.count(next) == 0) {
                len[next] = len[cur] + 1;
                q.push(next);
            }
        }
        for (int i = start.size() - 1; i >= num; --i) {
            string next(cur);
            for (int k = i; k > i - num; --k) {
                next[k] = next[k] == '-' ? '+' : '-';
            }
//            cout << cur << " : " << next << endl;
            if (len.count(next) == 0) {
                len[next] = len[cur] + 1;
                q.push(next);
            }
        }
    }
    return -1;
}

int main() {
    string row;
    int t, num;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> row >> num;
        int ans = solve(row, num);
        if (ans != -1) {
            cout << "Case #" << i << ": " << ans << endl;
        } else {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}