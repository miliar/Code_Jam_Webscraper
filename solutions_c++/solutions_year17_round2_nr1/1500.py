#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

#define EPS 1e7

ld max_time;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int T, N;
    ld D, S, G;
    cin >> T;
    for (int i = 1; i <= T; ++i){
        max_time = 0;
        cout << "Case #" << i << ": ";
        cin >> D >> N;
        for (int j = 1; j <= N; ++j){
            cin >> S >> G;
            max_time = max(max_time,(D-S)/G);
        }
        cout << fixed << setprecision(8) << D/max_time << '\n';

    }
}
