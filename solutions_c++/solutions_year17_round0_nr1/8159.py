#include <iostream>
#include <cstring>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <bitset>

using namespace std;
int n, t;
string s;
int res;
void small_test() {
    //bfs solution
    map<int, int> f;
    queue<int> q;
    int st = 0;
    int en = 0;
    // cout << s << endl;
    // cout << s.size() << endl;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '+')
            st |= (1 << i);
        en |= (1 << i);
    }
    q.push(st);
    f.insert({st,0});
    while (!q.empty()) {
        int fr=q.front();
        q.pop();
        // cerr << bitset<8>(fr) << endl;
        for (int i = 0; i <s.size()-n+1; ++i) {
            int next = fr;
            for (int j = 0; j < n; ++j)
                next ^= (1 << (i+j));
            if (f.find(next) == f.end()) {
                f[next] = f[fr] + 1;
                q.push(next);
            }
        }
    }
    // for (auto & x : f)
    //     cout << bitset<8>(x) << endl;
    if (f.find(en) == f.end()) res = -1;
    else res = (f.find(en))->second;
}
void big_test() {
    res = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            int pos = min((int)s.size()-n, i);
            for (int j = 0; j < n; ++j) {
                if (s[pos+j] == '-') s[pos+j] = '+';
                else s[pos+j] = '-';
            }
            res++;
        }
        // cerr << s << endl;
    }
    // cerr << endl;
    for (int i = 0; i < s.size(); ++i) 
        if (s[i] == '-') res = -1;
}
void fun() {
    // small_test();
    big_test();
}
int main()
{
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        cin >> s >> n;
        fun();
        cout << "Case #" << test << ": ";
        if (res == -1) cout << "IMPOSSIBLE\n";
        else cout << res << endl;
    }
    return 0;
}
