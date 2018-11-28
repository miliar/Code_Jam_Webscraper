#include <iostream>
#include <cstdio>
#include <queue>
#include <map>
#include <string>

using namespace std;

typedef pair<int, int> ii;

#define pb push_back
#define fi first
#define se second
#define sqr(x) ((x) * (x))

const char* fin = "quali17a.inp";
const char* fon = "quali17a.out";

#define oo (int) (1e9+7)
#define maxn (int) ()

map<string, int> mp;
string s;
int k;

bool check(string s) {
    for(int i = 0; i < s.size(); ++i) if (s[i] == '-') return false;
    return true;
}

string nxtStr(string s, int pos) {
    for(int i = 1; i <= k; ++i) {
        if (s[pos + i - 1] == '+') s[pos + i - 1] = '-'; else s[pos + i - 1] = '+';
    }
    return s;
}

void buff() {
    queue<string> q;
    mp.clear();
    q.push(s);
    mp[s] = 1;
    while (!q.empty()) {
        string s1 = q.front();
        //cout << s1 << '\n';
        q.pop();
        if (check(s1)) {
            cout << mp[s1] - 1;
            return;
        }
        for(int i = 0; i <= s1.size() - k; ++i) {
            string tmp = nxtStr(s1, i);
            if (mp[tmp] == 0) {
                mp[tmp] = mp[s1] + 1;
                q.push(tmp);
            }
        }
    }

    cout << "IMPOSSIBLE";
}

void sol() {
    int res = 0;
    for(int i = 0; i <= s.size() - k; ++i) {
       // cout << s << '\n';
        if (s[i] == '-') {
            for(int j = 0; j < k; ++j)
                if (s[i + j] == '+') s[i + j] = '-'; else s[i + j] = '+';
            ++res;
        }
    }
    if (check(s)) cout << res; else cout << "IMPOSSIBLE";
}

void inp() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cin >> s;
        cin >> k;
        if (s.size() <= 10) buff();
        else sol();
        cout << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    //freopen(fin, "r", stdin);freopen(fon, "w", stdout);
    inp();
    return 0;
}
