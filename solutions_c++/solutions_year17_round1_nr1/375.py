#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 200010;
const int inf = 1e9;

int n, m, b[N], a[N], ans[N];
map<int, int> cnt;

map<string, int> mp;
string s, words[N];
int n, m;
int dp[N], pre[N];

struct Trie {
    int son[N][26], root, cnt;
    int end[N];
    int cur;
    void init() {
        cnt = 0;
        root = ++cnt;
    }
    void reset() {
        cur = root;
    }
    void step(char ch) {
        cur = son[cur][ch - 'a'];
    }
    int check_end() {
        return end[cur];
    }
    void ins(const string &s, int idx) {
        int x = root;
        for(int i = 0; i < s.length(); ++i) {
            int p = s[i] - 'a';
            if(son[x][p] == 0) son[x][p] = ++cnt;
            x = son[x][p];
        }
        end[x] = idx;
    }
}trie;

inline char _lower(char ch) {
    if(ch >= 'A' && ch <= 'Z') ch += 32;
    return ch;
}
string lower(const string &s) {
    string ret = "";
    for(int i = 0; i < s.length(); ++i) {
        ret += _lower(s[i]);
    }
    return ret;
}
void _main() {
    cin >> n >> s >> m;
    trie.init();
    for(int i = 1; i <= m; ++i) {
        cin >> words[i];
        trie.ins(lower(words[i]), i);
    }
    
    memset(dp, -1, sizeof(dp));
    dp[0] = 0;
    for(int i = 1; i <= s.length(); ++i) {
        trie.reset();
        for(int j = i; j >= 1; --j) {
            trie.step(s[j - 1]);
            if(trie.check_end() && dp[j - 1] != -1) {
                dp[i] = trie.check_end();
                pre[i] = j - 1;
                break;
            }
        }
    }
    vector<int> ans;
    int last = s.length();
    while(last) {
        ans.push_back(dp[last]);
        last = pre[last];
    }
    reverse(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); ++i) {
        printf("%s%c", words[ans[i]].c_str(), i == ans.size() - 1 ? '\n' : ' ');
    }
}
int main() {
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}
