#include <iostream>
#include <string>
#include <deque>
using namespace std;

// Idiot method

int solve(const string& s, int k) {
    int ans = 0, n = s.length();
    deque<char> q;
    for (int i=0; i<=n; ++i) {
        if (i != n) q.push_back(s[i]);
        while (!q.empty() and q.front() == '+') q.pop_front();
        if (q.size() == k) {
            for (char& x : q) x = (x == '+' ? '-' : '+');
            ++ans;
        }
    }
    return (q.empty() ? ans : -1);
}

int main() {
    int n, k; cin >> n;
    string s;
    for (int i=1; i<=n; ++i) {
        cin >> s >> k;
        int ans = solve(s, k);
        printf("Case #%d: ", i);
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
