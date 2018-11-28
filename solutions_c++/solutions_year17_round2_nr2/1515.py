#include <bits/stdc++.h>

using namespace std;

#define f first
#define s second

char out = '?';

int cmp(pair<int, char> p1, pair<int, char> p2){
    if(p1.f == p2.f){
        return p1.s == out;
    }
    return p1.f > p2.f;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for(int tn = 1; tn <= tt; tn++){
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        int mx = max(r, max(b, y));
        if(mx > n - mx){
            cout << "Case #" << tn << ": IMPOSSIBLE" << endl;
            continue;
        }
        char cur = '?';
        string xs = "";
        vector<pair<int, char>> ss;
        ss.push_back({r, 'R'});
        ss.push_back({o, 'O'});
        ss.push_back({y, 'Y'});
        ss.push_back({g, 'G'});
        ss.push_back({b, 'B'});
        ss.push_back({v, 'V'});
        for(int i = 0; i < n; i++){
            sort(ss.begin(), ss.end(), cmp);
            for(int j = 0; j < 6; j++){
                if(cur != ss[j].s){
                    xs += ss[j].s;
                    cur = ss[j].s;
                    ss[j].f -= 1;
                    if(i == 0){
                        out = ss[j].s;
                    }
                    break;
                }
            }
        }
        cout << "Case #" << tn << ": " << xs << endl;
    }

    return 0;
}
