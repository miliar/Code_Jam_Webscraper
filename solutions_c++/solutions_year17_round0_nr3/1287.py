#include <bits/stdc++.h>

using namespace std;

#define llu long long unsigned

map <llu, map < llu, llu > > BIG;

map<llu, llu> dfs(const llu &n){
    if(BIG[n][1] || n == 0){
        return BIG[n];
    }
    BIG[n][n]++;
    if(n > 1){
        map <llu, llu> m1 = dfs(n / 2);
        map <llu, llu> m2 = dfs((n - 1) / 2);
        for(auto it : m1){
            BIG[n][it.first] += it.second;
        }
        for(auto it : m2){
            BIG[n][it.first] += it.second;
        }
    }
    return BIG[n];
}

int main(){
    ifstream fin("home.in");
    ofstream fout("home.out");
    int T, test;
    fin>>T;
    for(test = 1;test <= T;test++){
        llu n,k,sum;
        fin>>n>>k;
        map <llu, llu> m = dfs(n);
        sum = 0;
        fout<<"Case #"<<test<<": ";
        for(auto it = m.rbegin(); it != m.rend(); it++){
            if(it->first){
                sum += it->second;
                if(k <= sum){
                    fout << it->first / 2 << ' ' << (it->first - 1) / 2 << '\n';
                    break;
                }
            }
        }
    }
    return 0;
}
