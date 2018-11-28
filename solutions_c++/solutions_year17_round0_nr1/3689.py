#include <bits/stdc++.h>

#define fi first
#define se second
#define flip(c) c = (c == '+' ? '-' : '+');
#define therms(type, func) type, vector<type>, func 

using namespace std;

typedef pair<int, int> ii;
typedef pair<string, ii> sii;
typedef struct cmp { bool operator()(const sii& a, const sii& b) const 
    { return a.se.fi > b.se.fi; } } cmp;

int main()
{
    int T, k, ans;
    string s;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        cin >> s >> k;

        string ans1(s.size(), '+');

        priority_queue <therms(sii, cmp)> Q;
        if(s[0] == '+')
            Q.push(sii(s, ii(0, 1))); //str flip pos
        else {
            for (int i = 0; i < k; i++) flip(s[i]);
            Q.push(sii(s, ii(1, 1)));
        }
        
        ans = -1;
        while (!Q.empty()) {
            sii fr = Q.top(); Q.pop();
            //cout << fr.se.fi << endl;
            if (fr.fi == ans1) {
                ans = fr.se.fi;
                break;
            }

            if (fr.se.se + k == s.size() + 1) continue;

            if (fr.fi[fr.se.se] == fr.fi[fr.se.se - 1]) {
                Q.push(sii(fr.fi, ii(fr.se.fi, fr.se.se + 1))); 
            } else {
                if (fr.fi[fr.se.se] == '+') continue;
                for (int j = 0; j < k; j++)
                    flip(fr.fi[fr.se.se + j]);
                Q.push(sii(fr.fi, ii(fr.se.fi + 1, fr.se.se + 1))); 
            }
        }

        if (ans == -1) cout << "IMPOSSIBLE\n";
        else cout << ans << endl;
    }

    return 0;
}