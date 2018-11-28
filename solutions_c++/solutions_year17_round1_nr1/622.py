#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;
vector<string> fill(vector<string> &m) {
    vector<string> ans(m);
    for (auto &s: ans) {
        int p = 0;
        while (s[p] == '?' && p < s.size() ) p++;
        if (p==s.size()) continue;
        int q = p-1;
        while (q>=0) {s[q] = s[q+1]; q--;};
        while (p < s.size()) {
           if (s[p] == '?') s[p] = s[p-1];
           p++;
        }
    }
    return ans;
}
vector<string> tr(vector<string> m) {
    vector<string> ans;
    ans.resize(m[0].size());
    for (auto &s:m) {
        for (int i = 0 ; i < s.size(); i++)
            ans[i].push_back(s[i]);
    }
    return ans;
}
int main() {
    int nn;
    cin >> nn;
    for (int i = 1 ; i <= nn; i++) {
        printf("Case #%d:\n",i);
        int n,w;
        cin >> n >> w;
        vector<string> m;
        for (int a = 0; a < n; a++) {
            string s;
            cin >> s;
            m.push_back(s);
        }
        vector<string> VP = fill(m);
        VP = tr(VP);
        VP = fill(VP);
        VP = tr(VP);
        for (auto &s: VP) {
            cout << s << endl;
        }


    }
}
