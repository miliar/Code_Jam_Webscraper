#include <bits/stdc++.h>
using namespace std;

int R, C;
vector<string> v;

void rec(int a, int b, int x, int y){
    vector<pair<int, int> > o;
    for(int i=a;i<x;++i){
        for(int j=b;j<y;++j){
            if(v[i][j]!='?'){
                o.emplace_back(i, j);
            }
        }
    }
    assert(!o.empty());
    if(o.size()==1){
        for(int i=a;i<x;++i){
            for(int j=b;j<y;++j){
                v[i][j] = v[o.back().first][o.back().second];
            }
        }
        return;
    }
    pair<int, int> l=o[0], r=o[1];
    if(l.first!=r.first){
        int m = 1+min(l.first, r.first);
        rec(a, b, m, y);
        rec(m, b, x, y);
    } else {
        assert(l.second!=r.second);
        int m = 1+min(l.second, r.second);
        rec(a, b, x, m);
        rec(a, m, x, y);
    }

}

int main()
{
    freopen("inA.txt", "r", stdin);
    freopen("outA.txt", "w", stdout);
    cin.tie(0);ios_base::sync_with_stdio(false);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ":\n";

        cin >> R >> C;
        v.clear();v.resize(R);
        for(int i=0;i<R;++i) cin >> v[i];
        rec(0, 0, R, C);

        for(int i=0;i<R;++i) cout << v[i] << "\n";
    }


    return 0;
}

