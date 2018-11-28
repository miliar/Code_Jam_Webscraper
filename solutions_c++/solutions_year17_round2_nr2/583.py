#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef long double ld;
using namespace std;

int main() {
    //ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int R, O, Y, G, B, V, N;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        multiset<pair<int, pair<int, char> > > s;
        string res = "";
        vector<int> v;
        v.push_back(0);
        v.push_back(1);
        v.push_back(2);
        bool ok;
        do {
            s.clear();
            s.insert({R, { v[0], 'R', }});
            s.insert({Y, { v[1], 'Y' }});
            s.insert({B, { v[2], 'B' }});
            res = "";
            while (true) {
                auto it = s.end();
                it--;
                if (it->first == 0)
                    break;
                if(!res.empty() && it->second.second == res.back()) {
                    auto it1 = it;
                    it1--;
                    if(it1->first > 0)
                        it = it1;
                }
                res += it->second.second;
                int cnt = it->first;
                char c = it->second.second;
                int num = it->second.first;
                s.erase(it);
                s.insert({cnt - 1, { num, c }});
            }
            ok = true;
            for (int i = 0; i < (int) res.size(); i++) {
                int j = (i + 1) % (int) res.size();
                if (res[i] == res[j])
                    ok = false;
            }
            if(ok)
                break;
        } while(next_permutation(v.begin(), v.end()));
        cout << "Case " << "#" << t << ": ";
        if (!ok)
            cout << "IMPOSSIBLE\n";
        else
            cout << res << "\n";
    }
    return 0;
}