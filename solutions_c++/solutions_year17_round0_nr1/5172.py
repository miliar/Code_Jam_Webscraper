#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MOD = 1e9+7;
int solve(){
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    bitset<1000> start,finish;
    for(int i = 0; i < s.size(); ++i)
        if(s[i] == '-')
            start.set(i);
    hash<bitset<1000>> hash_fn;
    int h1 = hash_fn(start);
    unordered_set<int> visited;
    visited.insert(hash_fn(start));
    vector<bitset<1000>> bfs(1,start);
    vector<int> moves(1,0);
    for(int i = 0; i < bfs.size(); ++i){
        if(bfs[i] == finish)
            return moves[i];
        if(moves[i] > 1000)
            return -1;
        int l = 0;
        while(bfs[i][l] != 1)
            ++l;
        int r = l+k-1;
        if(r >= n)
            continue;
        auto nxt = bfs[i];
        for(int j = l; j <= r; ++j)
            nxt.flip(j);
        int hsh = hash_fn(nxt);
        if(!visited.count(hsh)){
            visited.insert(hsh);
            bfs.push_back(nxt);
            moves.push_back(moves[i]+1);
        }
    }
    return -1;
}
int main(){
    int t;
    cin >> t;
    for(int tc = 1; tc <= t; ++tc){
        cout << "Case #" << tc << ": ";
        int ans = solve();
        if(ans == -1)
            puts("IMPOSSIBLE");
        else
            cout << ans << '\n';
    }
}
