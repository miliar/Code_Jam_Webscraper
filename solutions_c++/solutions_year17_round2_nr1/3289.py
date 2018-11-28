#include <iostream>
#include <cstdio>
using namespace std;
#define MAX 10100
#define INF 1000000000000000000
long horse[3][MAX], N, D;

bool isPossible(double time){
    int i;
    double dist;
    for(i = 0; i < N; i++){
        dist = 1.0 * time * horse[1][i];
        dist = dist + horse[0][i];
        if(dist < 1.0 * D)
            return false;
    }
    return true;
}

void solve(){
    int T, t, i;
    double inf, sup, mid, ans;
    cin >> T;
    for(t = 1; t <= T; t++){
        cin >> D >> N;
        for(i = 0; i < N; i++)
            cin >> horse[0][i] >> horse[1][i];

        inf = 0.0, sup = INF;
        for(i = 0; i < 120; i++){
            mid = (inf + sup) / 2.0;
            if(isPossible(mid)){
                ans = mid;
                sup = mid;
            } else {
                inf = mid;
            }
        }
        printf("Case #%d: %.10lf\n", t, (1.0 * D / ans) );
    }
}

int main(){
    solve();
    return 0;
}
