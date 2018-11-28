#include <bits/stdc++.h>

using namespace std;

#define EPS 1e-8

typedef long double ld;

const ld pi = 3.141592653589;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int T, N, K;
    vector<pair<ld,ld> > RH;
    cin >> T;
    for (int i = 1; i <= T; ++i){
        cin >> N >> K;
        pair<ld,ld> k;
        for (int j = 1; j <= N; ++j){
            cin >> k.first >> k.second;
            RH.push_back(k);
        }
        sort(RH.begin(),RH.end(),greater<pair<ld,ld> >());
        ld best = 0, cur = 0;
        for (int j = 0; j <= N-K; ++j){
            cur = RH[j].first*RH[j].first*pi + 2*RH[j].first*RH[j].second*pi;
            multiset<ld> M;
            for (int l = j+1; l < N; ++l){
                M.insert(2*RH[l].first*RH[l].second*pi);
            }
            for (int l = 1; l <= K-1; ++l){
                cur += *(--M.end());
                M.erase(--M.end());
            }
            best = max(best,cur);
        }
        cout << fixed << setprecision(8) << "Case #" << i << ": " << best << '\n';
        RH.clear();
    }
    return 0;
}
