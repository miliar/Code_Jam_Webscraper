#include <bits/stdc++.h>

using namespace std;
map<string, int> visit;

int brute(string s, int k) {
    queue<string> q;

    visit.clear();
    q.push(s);
    visit[s] = 0;

    while(!q.empty()) {
        string c = q.front(); q.pop();
        int d = visit[c];

        for(int i = 0; i <= c.size() - k; ++i) {
            string aux(c);
            for(int j = 0; j < k; ++j)
                aux[j + i] = (aux[j + i] == '+' ? '-' : '+');

            if(visit.count(aux) == 0) {
                visit[aux] = d + 1;
                q.push(aux);
            }
        }
    }

    for(int i = 0; i < s.size(); ++i)
        s[i] = '+';

    if( visit.count(s) == 0 ) return -1;
    else return visit[s];
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    string s;
    int k, T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cin >> s >> k;
        int ans = brute(s, k);
        cout << "Case #" << t << ": ";

        if(ans == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << '\n';
    }
}
