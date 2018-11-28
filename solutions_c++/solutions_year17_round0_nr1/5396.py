#include <iostream>
#include <string>
#include <set>
#include <queue>
using namespace std;

typedef pair<string, int> P;
int T, K, len;
string str;
set<string> f;

bool is_ok(string s) {
    int flag = true;
    for (int i = 0; i < len; i++) {
        if (s[i] == '-') {
            flag = false;
            break;
        }
    }
    return flag;
}

bool visit(string s) {
    if (f.find(s) == f.end()) {
        f.insert(s);
        return false;
    }
    else return true;
}

void bfs() {
    f.clear();
    queue<P> q;
    q.push(make_pair(str, 0));
    bool flag = false;
    while (!q.empty()) {
        P h = q.front(); q.pop();
        if (is_ok(h.first)) {
            cout << h.second << endl;
            flag = true;
            break;
        }
        for (int i = 0; i < len-K+1; i++) {
            string tmp = h.first;
            for (int j = i; j < i+K; j++) {
                if (tmp[j] == '-') tmp[j] = '+';
                else tmp[j] = '-';
            }
            if (!visit(tmp)) q.push(make_pair(tmp, h.second+1));
        }
    }
    if (!flag) cout << "IMPOSSIBLE" << endl;
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> str >> K;
        len = str.length();
        cout << "Case #" << t << ": ";
        bfs();    
    }
    return 0;
}
