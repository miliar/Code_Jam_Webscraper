#include <bits/stdc++.h>
using namespace std;
int P;
map<pair<array<int, 4>, int>, int> cache;
int rec(array<int, 4> lef, int res){
    if(cache.count({lef, res})) return cache[{lef, res}];
    int ret = -1e6;
    for(int i=0;i<4;++i){
        if(lef[i]){
            auto re = lef;
            --re[i];
            ret = max(ret, rec(re, (res+P-i)%P));
        }
    }
    ret+= (res==0);
    ret=max(ret, 0);
    cache[{lef, res}]=ret;
    return ret;
}

int main()
{
    freopen("inA.txt", "r", stdin);
    freopen("outA.txt", "w", stdout);
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
    int Tests; cin >> Tests;
    for(int cas=1;cas<=Tests;++cas){
        cout << "Case #" << cas << ": ";
        cache.clear();
        int N, a;
        cin >> N >> P;
        array<int, 4> lef;
        for(auto &e:lef) e=0;
        for(int i=0;i<N;++i){
            cin >> a;
            ++lef[a%P];
        }
        int ans = rec(lef, 0);
        cout << ans;
        cerr << ans << "\n";

        cout << "\n";
    }


    return 0;
}
